class BaseDeviceEnvironment(object):

    def __init__(self, appium_support):
        """
        Поддержка Appium'а
        :param appium_support: параметр-связка для обработки параметров запуска тестов
        """
        self.appium_support = appium_support

    def get_capabilities(self, config_section):
        """
        Получение параметров из конфигурационного файла для оперделенного девайса
        :param config_section: параметры из конфигурационного файла для оперделенного девайса
        :rtype dict
        :return:
        """
        return {}

    def start_driver(self, browser_type, capabilities):
        """
        Запуск Appium driver'а
        :param browser_type:
        :param capabilities: параметры из конфигурационного файла для оперделенного девайса
        :rtype selenium.webdriver.remote.webdriver.WebDriver
        :return: Appium driver
        """
        raise NotImplementedError()

    def get_pytest_arguments(self, config_section):
        """
        Получение параметров для pytest'а
        :param config_section: параметры из конфигурационного файла для оперделенного девайса
        :rtype dict
        :return:
        """
        pass

    #TODO: Привязать метод при тестировании запуска suites
    # def get_test_name(self):
    #
    #     frames = inspect.getouterframes(inspect.currentframe())
    #     for frame in frames:
    #         if re.match('test_.*', os.path.basename(frame[1])):
    #             return os.path.basename(frame[1])[:-3]
    #
    #     return self.config_support.get_opt('project_name')
