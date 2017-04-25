from element_helpers.find_element_helper import FindElementHelper
from selenium.common.exceptions import NoSuchElementException as error
from model.parameter_driver_for_helper import ParameterDriverForHelper
import logging
import re


class ElementTextHelper(ParameterDriverForHelper):

    def __init__(
            self,
            log: logging.Logger,
            find_element_helper: FindElementHelper):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        :param find_element_helper: Инициализация хелпера для поиска элементов
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        assert isinstance(find_element_helper, FindElementHelper)
        self.find_element_helper = find_element_helper

    def get_element_text(self, locator):
        """
        Получить текст из элемента
        :param locator: Локатор для элемента с текстом
        :return str: Текст из строки элемента
        """
        element_object = self.find_element_helper.get_element(locator)
        try:
            self.log.info(
                "Получение текста элемента с локатором: '{0}'".format(locator))
            text_element_on_screen = element_object.text
            self.log.info(
                "Текст элемента с локатором: '{0}' успешно получен".format(locator))
        except error:
            message = "Не удалось получить текст элемента с локатором: '{0}' из-за ошибки '{1}'".format(
                locator, error)
            self.log.critical(message)
            assert False, message
        return text_element_on_screen

    def get_elements_text(self, locators):
        """
        Получить текст из нескольких элементов (вспомогательный метод)
        :param locators: локатор для нескольких элементов, содержащих текст
        :rtype list
        :return: массив строк (текст из каждого элемента)
        """
        elements = self.find_element_helper.get_elements(locators)
        return [*map(lambda element: element.text, elements)]

    def compare_element_text(self, locator, text_to_compare):
        """
        Сравнить текст элементов
        :param locator: принимает локатор элемента, в котором содержится текст, который нужно получить
        :param text_to_compare: Текст для сравнения (строка или массив с нужными строчками в правильном порядке)
        :return True: Текст совпадает
        """
        global element_text, i
        elements_text = self.get_elements_text(locator)
        if isinstance(text_to_compare, str):
            text_to_compare = [text_to_compare]
        for i in range(0, len(text_to_compare)):
            element_text = elements_text[i]
            if element_text == text_to_compare[i]:
                self.log.info(
                    "Текст элемента '{0}' совпадает c ожидаемым текстом '{1}'".format(
                        element_text, text_to_compare[i]))
            else:
                message = "Текст элемента '{0}' не совпадает c ожидаемым текстом '{1}'".format(
                    element_text, text_to_compare[i])
                assert False, message

    def get_number_from_string(self, locator):
        """
        Получить число из строки

        :param locator: Локатор для элемента
        :return int: Число из строки элемента
        """
        text = self.get_element_text(locator)
        try:
            self.log.info("Получение числа из строки '{0}'".format(text))
            result = int(re.search(r'\d+', text).group())
            self.log.info("Число успешно получено")
        except error:
            message = "Не удалось получить число из текста элемента c локатором '{0}' на странице , " \
                      "так как произошла ошибка '{1}'".format(locator, error)
            self.log.critical(message)
            assert False, message
        return result

    def partially_matching_text(self, locator, text_to_compare):
        """
        Cравнить текст в локаторе по частичному совпадению с заданным текстом
        :param locator: Локатор для элемента
        :param text_to_compare: Текст для сравнения
        :return True: Текст подтвержден по частичному совпадению
        """
        text = self.get_element_text(locator)
        if text_to_compare in text:
            message = "Текст локатора '{0}' соответствует заданному тексту: '{1}'".format(
                locator, text_to_compare)
            self.log.info(message)
            return True
        else:
            message = "Текст локатора '{0}' не совпадает с заданным текстом: '{1}'".format(
                locator, text_to_compare)
            self.log.critical(message)
            assert False, message