from element_helpers.wait_element_helper import WaitElementHelper
from element_helpers.find_element_helper import FindElementHelper
from element_helpers.scroll_and_swipe_element_helper import ScrollAndSwipeElementHelper
from element_helpers.service_function_helper import ServiceFunctionHelper
from selenium.common.exceptions import ElementNotVisibleException as error
from appium.webdriver.common.touch_action import TouchAction
from model.parameter_driver_for_helper import ParameterDriverForHelper
from time import sleep

import logging


class TapAndPressElementHelper(ParameterDriverForHelper):

    def __init__(
            self,
            log: logging.Logger,
            wait_element_helper: WaitElementHelper,
            find_element_helper: FindElementHelper,
            scroll_and_swipe_element_helper: ScrollAndSwipeElementHelper,
            service_function_helper: ServiceFunctionHelper):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        :param wait_element_helper: Инициализация хелпера ожидания
        :param find_element_helper: Инициализация хелпера для поиска элементов
        :param scroll_and_swipe_element_helper: Инициализация хелпера для свайпов и скролов
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        assert isinstance(wait_element_helper, WaitElementHelper)
        assert isinstance(find_element_helper, FindElementHelper)
        assert isinstance(scroll_and_swipe_element_helper, ScrollAndSwipeElementHelper)
        assert isinstance(service_function_helper, ServiceFunctionHelper)
        self.wait_element_helper = wait_element_helper
        self.find_element_helper = find_element_helper
        self.scroll_and_swipe_element_helper = scroll_and_swipe_element_helper
        self.service_function_helper = service_function_helper

    def tap(self, locator):
        """
        Тап по элементу

        :param locator: Локатор для элемента
        :return:
        """
        element = self.wait_element_helper.wait_until_element_visible(locator)
        self.log.info("Тапаем по элементу с локатором: '{0}'".format(locator))
        try:
            element.click()
            self.log.info(
                "Тап по элементу с локатором: '{0}' прошел успешно".format(locator))
        except error:
            message = "Не удалось тапнуть на элемент с локатором: '{0}' из-за ошибки: '{1}'".format(
                locator, error)
            self.log.critical(message)
            assert False, message

    def tap_on_element(self, element):
        """
        Нажать на элемент, элемент предварительно должен быть найден

        :param element: Локатор для элемента
        :return:
        """
        try:
            element.click()
            self.log.info(
                "Тап по элементу: '{0}' прошел успешно".format(element))
        except error:
            message = "Не удалось тапнуть на элемент: '{0}' из-за ошибки: '{1}'".format(
                element, error)
            self.log.critical(message)
            assert False, message

    def long_press(self, locator, duration=1000):
        """
        Долгий тап по элементу

        :param locator: Локатор для элемента
        :param duration: Продолжительность нажатия
        :return:
        """
        element = self.find_element_helper.get_element(locator)
        action = TouchAction(self.driver)
        platform = self.service_function_helper.get_device_capabilities('platformName')
        if platform == "iOS":
            duration = duration * 0.0010
        self.log.info(
            "Производим долгий тап по элементу с локатором: '{0}'".format(locator))
        try:
            action.long_press(element, None, None, duration).perform()
            self.log.info(
                "Долгий тап по элементу c локатором: '{0}' прошел успешно".format(locator))
        except error:
            message = "Не удалось произвести долгий тап по элементу с локатором: '{0}' из-за ошибки: {1}".\
                format(locator, error)
            self.log.critical(message)
            assert False, message

    def select_elements_and_long_press_on_first(self, elements, duration=1000):
        """
        Выбрать несколько элементов (долгий тап по первому и обычные по остальным)

        :param elements: Локатор для элементов
        :param duration: Продолжительность нажатия
        :return:
        """
        action = TouchAction(self.driver)
        platform = self.service_function_helper.get_device_capabilities('platformName')
        if platform == "iOS":
            duration = duration * 0.0010
        self.log.info("Выбираем несколько элементов: '{0}'".format(elements))
        try:
            action.long_press(elements[0], None, None, duration).perform()
            for e in range(1, len(elements)):
                elements[e].click()
            self.log.info(
                "Долгий тап по элементам: '{0}' прошел успешно".format(elements))
        except error:
            message = "Не удалось произвести долгий тап по первому элементу: '{0}' из-за ошибки: '{1}'".\
                format(elements, error)
            self.log.critical(message)
            assert False, message

    def scroll_to_element_and_tap(self, locator, limit=5):
        """
        Скролл до появления нужного элемента, затем нажатие на него

        :param locator: Локатор для элемента
        :param limit: Лимит количества скроллов (по умолчанию - 5)
        :return:
        """
        self.log.info("Скролл до элемента с локатором {0}".format(locator))
        limit = limit
        self.scroll_and_swipe_element_helper.scroll_while_element_is_invisible(
            locator, limit)
        self.tap(locator)

    def tap_and_verify_visibility(
            self,
            locator,
            locator_to_check,
            delay=None):
        """
        Нажатие на элемент и проверка наличия элемента на странице

        :param locator: Локатор для элемента
        :param delay: Задержка перед поиском искомого элемента
        :return:
        """
        self.tap(locator)
        if delay:
            sleep(int(delay))
        self.find_element_helper.is_visible_element(locator_to_check)

    def multiple_tap(self, *locators):
        """
        Последовательное нажатие на несколько элементов

        :param locators: Локатор для нескольких элементов
        :return:
        """
        for locator in locators:
            self.tap(locator)

