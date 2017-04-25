from model.config_support import ConfigSupport


class AppiumControlTest(object):

    def __init__(self):
        """
        Конструктор для инициализации параметров
        :param config_support: класс ConfigSupport (обработка конфигурационных файлов для девайсов)
        :param device_environment: appium
        :param driver: драйвер
        """
        self.config_support = ConfigSupport()
        control_env_obj = self.config_support.get_module('device_environment')
        self.device_environment = control_env_obj(self.config_support)
        self.driver = None

    def get_driver(self):
        """
        Получение драйвер с инициализованными параметрами из конфигурационнного файла Runner'а
        :rtype selenium.webdriver.remote.webdriver.WebDriver
        :return: Appium driver
        """
        appium_url = self.config_support.get_opt('appium_url')
        config_section = self.config_support.get_opt(
            'device_configuration')
        self.driver = self.device_environment.call_appium_driver(config_section)
        if appium_url:
            self.test_init(appium_url)
        return self.driver

    def test_init(self, url):
        """ Инициализация тестов происходит после запуска appium driver
        :param str url:
        """
