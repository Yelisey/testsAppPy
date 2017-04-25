from appium import webdriver
from model.base_test import BaseTest

from model.appium_device.base_device_enviroment import BaseDeviceEnvironment


class AppiumDeviceEnvironment(BaseDeviceEnvironment):

    def call_appium_driver(self, config_section):
        """
        Вызов драйвера
        :param config_section: параметры из конфигурационного файла для определенного девайса
        :rtype selenium.webdriver.remote.webdriver.WebDriver
        :return: драйвер
        """
        capabilities = self.get_capabilities(config_section)
        appium_url = self.appium_support.get_opt('appium_url')
        return self.start_driver(capabilities, appium_url)

    def get_capabilities(self, config_section):
        """
        Получение параметров для определенного девайса
        :param config_section: параметры из конфигурационного файла для определенного девайса
        :rtype dict
        :return: параметры для определенного девайса
        """
        capabilities = {}
        get_opt = self.appium_support.get_opt
        app_name = BaseTest().get_app_for_runner(get_opt(config_section, 'app_name'))
        platformName = get_opt(config_section, 'platformName')
        if platformName == 'iOS':
            capabilities.update({'udid': get_opt(config_section, 'udid')})
        capabilities.update({'platformName': platformName})
        capabilities.update({'platformVersion': get_opt(
            config_section, 'platformVersion')})
        capabilities.update({'deviceName': get_opt(
            config_section, 'deviceName')})
        capabilities.update({'app': app_name})
        capabilities.update({'autoAcceptAlerts': True if get_opt(
            config_section, 'autoAcceptAlerts').lower() == 'true' else False})

        return capabilities

    def get_pytest_arguments(self, config_section):
        """
        Получение параметров для pytest'а
        :param config_section: параметры из конфигурационного файла для определенного девайса
        :rtype dict
        :return: параметры для pytest'а
        """
        pytest_args = {
            '--platformName': '--platformName={0}'.format(self.appium_support.get_opt(config_section, 'platformName')),
            '--platformVersion': '--platformVersion={0}'.format(self.appium_support.get_opt(config_section, 'platformVersion')),
            '--deviceName': '--deviceName={0}'.format(self.appium_support.get_opt(config_section, 'deviceName')),
            '--autoAcceptAlerts': '--autoAcceptAlerts={0}'.format(self.appium_support.get_opt(config_section, 'autoAcceptAlerts')),
            '--app_name': '--app_name={0}'.format(self.appium_support.get_opt('app_name') or self.appium_support.get_opt(config_section, 'app_name'))
        }
        if pytest_args.get("--platformName") == "--platformName=iOS":
            pytest_args.update({'--udid': '--udid={0}'.format(self.appium_support.get_opt(config_section, 'udid'))})

        return pytest_args

    def start_driver(self, capabilities, appium_driver_url):
        """
        Запуск драйвера с параметрами
        :param capabilities: параметры из конфигурационного файла для определенного девайса
        :param appium_driver_url: url Appium driver'а
        :rtype selenium.webdriver.remote.webdriver.WebDriver
        :return: Appium driver
        """
        driver = webdriver.Remote(
            command_executor=appium_driver_url,
            desired_capabilities=capabilities,
        )
        return driver
