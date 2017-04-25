from selenium.common.exceptions import NoSuchElementException as error
from model.parameter_driver_for_helper import ParameterDriverForHelper
from appium.webdriver.common.mobileby import MobileBy

import logging


class FindElementHelper(ParameterDriverForHelper):

    def __init__(self, log: logging.Logger):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        self.BY = {
            'id': MobileBy.ID,
            'name': MobileBy.NAME,
            'android': MobileBy.ANDROID_UIAUTOMATOR,
            'class_name': MobileBy.CLASS_NAME,
            'accessibility_id': MobileBy.ACCESSIBILITY_ID,
            'xpath': MobileBy.XPATH
        }

    def get_element(self, locator):
        """
        Получить необходимый элемент (основной метод)
        :param locator: Локатор для элемента
        :return: Объект найденного элемента
        """
        method = locator[0]
        values = locator[1]
        if isinstance(values, str):
            self.log.info(
                "Элемент с типом локатора: '{0}' и данными: '{1}' успешно получен".format(
                    method, values))
            return self.driver.find_element(self.get_By(locator), values)
        elif isinstance(values, list):
            for value in values:
                try:
                    self.log.info(
                        "Элемент с типом локатора: '{0}' и данными: '{1}' успешно получен" .format(
                            method, value))
                    return self.driver.find_element(self.get_By(locator), value)
                except error:
                    pass
            raise error

    def get_By(self, locator):
        """
        Метод получения типа поиска локатора для элемента
        :param locator: Локатор для элементов
        :return:
        """
        return self.BY[locator[0]]

    def get_elements(self, locator):
        """
        Получить элементы (основной метод)

        :param locator: Локатор для элементов
        :return: Объекты найденных элементов
        """
        method = locator[0]
        values = locator[1]
        if isinstance(values, str):
            self.log.info(
                "Элементы с типом локатора: '{0}' и данными: '{1}' успешно получены".format(
                    method, values))
            return self.driver.find_elements(self.get_By(locator), values)
        elif isinstance(values, list):
            for value in values:
                try:
                    self.log.info(
                        "Элементы с типом локатора: '{0}' и данными: '{1}' успешно получены" .format(
                            method, value))
                    return self.driver.find_elements(self.get_By(locator), value)
                except error:
                    pass
            raise error

    def is_enabled_element(self, locator):
        """
        Проверить статус enabled/disabled элемента
        :param locator: Локатор для элемента
        :return True: Элемент включен
        """
        self.log.info(
            "Определение состояния enabled/disabled у элемента с локатором: '{0}'".format(locator))
        element = self.get_element(locator).is_enabled()
        if element:
            self.log.info(
                "Элемент с локатором: '{0}' включен(enabled)".format(locator))
            return True
        elif element == False:
            self.log.critical(
                "Элемент с локатором: '{0}' отключен(disabled)".format(locator))
            return False

    def is_visible_element(self, locator):
        """
        Проверить видимость элемента
        :param locator: Локатор для элемента
        :return True: Элемент виден
        """
        self.log.info(
            "Определение существования элемента на экране: '{0}'".format(locator))
        try:
            self.get_element(locator).is_displayed()
            self.log.info(
                "Элемент с локатором: '{0}' представлен на экране".format(locator))
            return True
        except error:
            self.log.critical(
                "Элемент c локатором: '{0}' не представлен на экране!!!".format(locator))
            return False
