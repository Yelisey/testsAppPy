from element_helpers.artifacts_helper import get_time
from model.config_support import ConfigSupport

import argparse
import sys


class RunnerTest(object):

    def __init__(self, project_root):
        """
        :param project_root: корень проекта
        :param cmd_args: параметры для скрипта для запуска runner'а
        :param appium_support: вспомогательный класс для обработки различных типов конфигураций (local и server)
        """
        self.project_root = project_root
        self.cmd_args = self.handle_cmd_args()
        self.appium_support = ConfigSupport(
            cmd_args=self.cmd_args,
            project_root=self.project_root
        )

    def handle_cmd_args(self):
        """
        Обработка параметров из скрипта для запуска runner'а
        :param --platform_control: appium
        :param --environment: имя файла __.properties для определенного девайса
        :param --test_directory: директория, где лежат тесты
        :param --smoke: параметр для запуска тестов с маркером smoke
        :param --regress: параметр для запуска тестов с маркером regress
        :param --app: директория приложения
        :rtype dict
        :return: словарь переменных
        """
        parser = argparse.ArgumentParser(
            description='Selenium Python test runner execution arguments.')

        parser.add_argument('--platform_control',
                            help='Platform on which run tests.',
                            dest='test_platform')
        parser.add_argument('--environment',
                            help='Environment for which run tests.',
                            dest='device_environment')
        parser.add_argument('--test_directory',
                            help='Directory where to lookup for tests')
        parser.add_argument('--smoke',
                            help='Run only smoke tests',
                            action='store_true')
        parser.add_argument('--regress',
                            help='Run only regress tests',
                            action='store_true')
        parser.add_argument('--app',
                            help='Path to appium application')
        args = parser.parse_args()
        return vars(args)

    def run_tests(self):
        """
        Запуск тестов с помощью runner'а
        :rtype int
        :return: exit_code: код запуска тестов: 0 - passed или !=0 - failed
        """
        if __name__ == "__main__":
            sys.exit('Runner должен запускаться из проекта с тестами!')
        executor_class = self.appium_support.get_module('platform_execution')
        executor = executor_class(
            self.appium_support,
            get_time("%Y-%m-%d %H-%M-%S-%f"))
        exit_code = executor.run_tests()
        return exit_code
