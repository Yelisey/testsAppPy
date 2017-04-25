from appium import webdriver


class ParameterDriverForHelper:

    driver = None

    @classmethod
    def set_driver(cls, driver: webdriver.Remote):
        """
        Задать объект драйвера

        :param driver: Экземпляр класса webdriver
        """
        cls.driver = driver