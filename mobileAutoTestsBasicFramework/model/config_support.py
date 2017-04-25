from importlib import import_module

import configparser
import os
import pytest
import sys


class ConfigSupport(object):

    def __init__(self, cmd_args=None, project_root=None):
        """
        Конструктор для инициализации параметров
        :param args_config: словарь с параметрами для скрипта для запуска runner'а или пустой словарь
        :param used_in_test: словарь с параметрами для скрипта для запуска runner'а
        :param project_root: строка с путем до конфигурационных файлов для разных девайсов
        :param configs: главный конфигурационный файл (main_config.properties)
        :param test_environment:
        :param test_platform:
        :param env_config: конфигурационный файл для определенного девайса
        """
        self.args_config = cmd_args or {}
        self.used_in_test = cmd_args
        self.project_root = project_root or self.find_project_root()
        self.configs = self.load_configs()
        self.device_environment = self.get_opt('device_environment')
        self.test_platform = self.get_opt('test_platform')
        self.device_config = self.get_device_config()

    # TODO поменять имя метода, так как он возвращает не корень проекта, а путь до конфигурационных файлов
    def find_project_root(self):
        """
        Поиск директории с конфигурационными файлами для разных девайсов
        :rtype str
        :return: путь до конфигурационных файлов для разных девайсов
        """
        for path in sys.path:
            config_dir = os.path.join(path, 'config')
            if os.path.exists(config_dir):
                return path
        raise ValueError('Не удалось найти директорию с файлами конфигурации')

    def load_configs(self):
        """
        Загрузка конфигурации main_config.properties
        :rtype list
        :return: параметры из main_config.properties
        """
        config_path = os.path.join(self.project_root, 'config')
        if not os.path.exists(config_path):
            raise ValueError(
                'Директория с файлами конфигурации пустая {0}'.format(config_path))
        configs = []
        config = configparser.ConfigParser()
        main_config = os.path.join(config_path, 'main_config.properties')
        config.read(main_config)
        main_config_vars = dict(config.defaults())
        configs.insert(0, (main_config_vars, 'main config'))
        return configs

    def get_opt(self, *args):
        """
        Получение всех опций из конфигурационного файла
        :param args:
        :rtype str
        :return: value (опция из конфигурационного файла)
        """
        if len(args) > 2 or not args:
            raise TypeError(
                'Неправильное число аргументов при конфигурации, используй 1 либо 2'.format(
                    len(args)))
        if len(args) == 2:
            section, key = args
        else:
            key = args[0]
            section = None
        if section:
            return self.device_config.get(section, key)
        try:
            value = pytest.config.getoption(key)
            if value:
                return value
        except (ValueError, AttributeError):
            pass
        value = self.args_config.get(key)
        if value:
            return value

        for cfg, cfg_name in self.configs:
            value = cfg.get(key)
            if value:
                return value

    def get_device_config(self):
        """
        Получение конфигурационного файла для девайса
        :rtype dict
        :return: конфигурационный файл для определенного девайса
        """
        config = configparser.ConfigParser()
        config_path = os.path.join(
            self.project_root,
            'config',
            self.test_platform,
            self.device_environment +
            '.properties')

        if not os.path.exists(config_path):
            raise ValueError(
                'Конфигурационный файл {0} не найден!'.format(config_path))
        config.read(config_path)
        return config

    def get_module(self, module):
        """
        Определение модулей конфигурации
        :param module:
        :rtype str
        :return: значение модуля
        """
        platform_execution = 'mobileAutoTestsBasicFramework.model.platform_control.appium_test_executor'
        platform_test = 'mobileAutoTestsBasicFramework.model.platform_control.appium_control_test'
        device_environment = 'mobileAutoTestsBasicFramework.model.appium_device.appium_device_enviroment'

        if module == 'platform_execution':
            return getattr(
                import_module(platform_execution),
                'AppiumTestExecution')
        elif module == 'platform_test':
            return getattr(import_module(platform_test), 'AppiumControlTest')
        elif module == 'device_environment':
            return getattr(
                import_module(device_environment),
                'AppiumDeviceEnvironment')

        raise ValueError('Неверный модуль конфигурации')

    def get_test_control(self):
        return self.get_module('platform_test')()
