from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from element_helpers.find_element_helper import FindElementHelper
from model.parameter_driver_for_helper import ParameterDriverForHelper

import logging


class WaitElementHelper(ParameterDriverForHelper):

    def __init__(self, log: logging,
                 find_element_helper: FindElementHelper):
        """
        Конструктор для инициализации параметров
        :param log: Экземпляр класса logging
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        assert isinstance(find_element_helper, FindElementHelper)
        self.find_element_helper = find_element_helper

    def implicitly_wait(self, timeout: int):
        """
        Неявное ожидание
        :param timeout: Значение задаваемого ожидания
        """
        self.driver.implicitly_wait(timeout)

    def __wait_conditions(self, wait_condition: str, locator, text=None):
        """
        Основной метод для определения необходимого типа ожидания элемента
        :param wait_condition: тип ожидания элемента
        :param locator: локатор элемента
        :param text: ожидаемый текст
        :return: condition - состояние waiter
        :rtype: object
        """
        presence_of_element_located = lambda: ec.presence_of_element_located(
            locator)
        visibility_of_element_located = lambda: ec.visibility_of_element_located(
            locator)
        element_to_be_clickable = lambda: ec.element_to_be_clickable(locator)
        element_to_be_selected = lambda: ec.element_to_be_selected(
            self.find_element_helper.get_element(locator))
        text_to_be_present_in_element = lambda: ec.text_to_be_present_in_element(
            locator, text)
        title_is = lambda: ec.title_is(text)
        title_contains = lambda: ec.title_contains(text)
        unknown_waiter = lambda: 'Неправильный тип ожидания'
        condition = wait_condition
        functions = {
            'presence_of_element_located': presence_of_element_located,
            'visibility_of_element_located': visibility_of_element_located,
            'element_to_be_clickable': element_to_be_clickable,
            'element_to_be_selected': element_to_be_selected,
            'text_to_be_present_in_element': text_to_be_present_in_element,
            'title_is': title_is,
            'title_contains': title_contains}
        return functions.get(condition, unknown_waiter)()

    def __wait_element_for(self, wait_condition: str, locator):
        """
        Вспомогательный метод для ожидания элемента
        :param wait_condition: тип ожидания
        :param locator: локатор элемента
        :return:
        """
        try:
            self.log.info("Ожидание появления элемента '{0}'.".format(locator))
            WebDriverWait(
                self.driver,
                10).until(
                self.__wait_conditions(
                    wait_condition,
                    locator))
            self.log.info("Ожидание появления элемента '{0}' прошло успешно."
                          .format(locator))
        except Exception as error:
            self.log.exception(
                "Не удалось найти элемент '{locator}', так как произошла ошибка:\n{error}." .format(
                    locator=locator, error=error), exc_info=True)

    def __wait_text_for(self, wait_condition: str, text: str, locator=None):
        """
        Вспомогательный метод для ожидания текста элемента
        :param wait_condition: тип ожидания
        :param text: текст, который ожидаем
        :param locator: локатор элемента
        :return:
        """
        try:
            self.log.info("Ожидание появления текста '{0}'.".format(text))
            WebDriverWait(
                self.driver,
                10).until(
                self.__wait_conditions(
                    wait_condition,
                    locator,
                    text))
            self.log.info(
                "Ожидание появления текста '{0}' прошло успешно.".format(text))
        except Exception as error:
            self.log.exception(
                "Не удалось найти текст '{text}', "
                "так как произошла ошибка:\n{error}.".format(
                    text=text, error=error), exc_info=True)

    def wait_of_presence(self, locator):
        """
        Ожидание presence_of_element_located (Ожидание для проверки того, что элемент присутствует в DOM страницы)
        :param locator: локатор элемента
        :return:
        """
        self.__wait_element_for('presence_of_element_located', locator)

    def wait_of_visible(self, locator):
        """
        Ожидание visibility_of_element_located
        (Ожидание для проверки того, что элемент присутствует в DOM страницы и виден)
        :param locator: локатор элемента
        :return:
        """
        self.__wait_element_for('visibility_of_element_located', locator)

    def wait_of_clickable(self, locator):
        """
        Ожидание element_to_be_clickable (Ожидание для проверки видимости элемента и доступности таким образом,
        что вы можете кликнуть по нему.)
        :param locator: локатор элемента
        :return:
        """
        self.__wait_element_for('element_to_be_clickable', locator)

    def wait_of_text_present(self, locator, text: str):
        """
        Ожидание text_to_be_present_in_element (Ожидание для проверки того, что данный текст присутствует в элементе)
        :param locator: локатор элемента
        :param text: текст, который ожидаем
        :return:
        """
        self.__wait_text_for('text_to_be_present_in_element', text, locator)

    def wait_until_element_visible(self, locator, timeout=10):
        """
        Ждать пока элемент станет видимым на экране
        :param locator: Локатор ожидаемого элемента
        :param timeout: Время ожидания
        :return: Текущий элемент
        """
        for i in range(0, timeout):
            self.log.info(
                "Ожидаем пока элемент с локатором: '{0}' станет видимым".format(locator))
            try:
                self.wait_of_visible(locator)
                self.log.info(
                    "Элемент с локатором: '{0}' виден".format(locator))
                return self.find_element_helper.get_element(locator)
            except Exception as error:
                message = "Элемент с локатором: '{0}' не виден из-за ошибки: '{1}'".format(
                    locator, error)
                self.log.exception(message, exc_info=True)
                assert False, message
