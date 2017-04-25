from element_helpers.find_element_helper import FindElementHelper
from element_helpers.tap_and_press_element_helper import TapAndPressElementHelper
from element_helpers.keyboard_helper import KeyboardHelper
from element_helpers.service_function_helper import ServiceFunctionHelper
from selenium.common.exceptions import ElementNotVisibleException as error
from model.parameter_driver_for_helper import ParameterDriverForHelper
from time import sleep

import logging


class ValueAndDataElementHelper(ParameterDriverForHelper):

    def __init__(
            self,
            log: logging.Logger,
            find_element_helper: FindElementHelper,
            tap_and_press_element_helper: TapAndPressElementHelper,
            keyboard_element_helper: KeyboardHelper,
            service_function_helper:  ServiceFunctionHelper):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        :param find_element_helper: Инициализация хелпера для поиска элементов
        :param tap_and_press_element_helper: Инициализация хелпера для тапов
        :param keyboard_element_helper: Инициализация хелпера для взяимодействия с клавиатурой
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        assert isinstance(find_element_helper, FindElementHelper)
        assert isinstance(tap_and_press_element_helper, TapAndPressElementHelper)
        assert isinstance(keyboard_element_helper, KeyboardHelper)
        assert isinstance(service_function_helper, ServiceFunctionHelper)
        self.find_element_helper = find_element_helper
        self.tap_and_press_element_helper = tap_and_press_element_helper
        self.keyboard_element_helper = keyboard_element_helper
        self.service_function_helper = service_function_helper

    def send_data(self, locator, text: str):
        """
        Отправить данные в элемент

        :param locator: Локатор для поля элемента отправки данных
        :param text: Текст для отправки
        :return:
        """
        element = self.find_element_helper.get_element(locator)
        self.log.info(
            "Отправляем данные в элемент с локатором: '{0}'".format(locator))
        try:
            element.set_value(text)
            self.log.info(
                "Данные в элемент с локатором: '{0}' успешно отправлены".format(locator))
        except error:
            message = "Не удалось отправить данные в элемент c локатором: '{0}' из-за ошибки: '{1}'".\
                format(element, error)
            self.log.critical(message)
            assert False, message

    def send_keycode(self, locator, numbers):
        """
        Отправить KeyCode c клавиатуры в элемент (метод принимает список кодов)

        :param locator: Локатор для поля элемента отправки данных
        :param numbers: Код действия для исполнения
        :return:
        """
        self.tap_and_press_element_helper.tap(locator)
        for number in numbers:
            self.log.info(
                "Отправляем Keycode = '{0}' c клавиатуры в элемент с локатором: '{1}'". format(
                    number, locator))
            try:
                self.keyboard_element_helper.press_keycode(number)
                self.log.info(
                    "Keycode = '{0}' успешно отправлен c клавиатуры в элемент с локатором: '{1}'". format(
                        number, locator))
            except error:
                message = "Не удалось отправить KeyCode = '{0}' c клавиатуры в элемент c локатором: '{1}' " \
                    "из-за ошибки: '{2}'".format(number, locator, error)
                self.log.critical(message)
                assert False, message

    def delete_all_data(self, locator):
        """
        Удалить все данные из элемента

        :param locator: Локатор поля элемента с данными
        :return:
        """
        element = self.find_element_helper.get_element(locator)
        text_len = len(element.text)
        for i in range(0, text_len):
            self.log.info(
                "Удаляем все символы в элементе с локатором: '{0}'".format(locator))
            try:
                self.keyboard_element_helper.press_keycode(67)
                self.log.info(
                    "Все символы в элементе с локатором: '{0}' удалены".format(locator))
            except error:
                message = "Не удалось удалить символы в элементе c локатором: '{0}' из-за ошибки: '{1}'".\
                    format(locator, error)
                self.log.critical(message)
                assert False, message

    def get_checked_property(self, locator):
        """
        Проверить у элемента свойство "checked"

        :param locator: Локатор для элемента
        :return True: Значение совпадает
        :return False: Значение не совпадает
        """
        object_element = self.find_element_helper.get_element(locator)
        locator_status = object_element.get_attribute("checked")
        if locator_status == "true":
            return "true"
        else:
            return "false"

    def compare_elements(self, first_element, second_element):
        """
        Сравненить элементы

        :param first_element: Локатор для первого элемента
        :param second_element: Локатор для второго элемента
        :return True: Совпадение элементов
        :return False: Элементы не совпадают
        """
        if first_element == second_element:
            self.log.info(
                "Элемент: '{0}' совпадает с элементом: '{1}'".format(
                    first_element, second_element))
            return True
        else:
            self.log.critical(
                "Элемент: '{0}' не совпадает с элементом: '{1}'!". format(
                    first_element, second_element))
            return False

    def check_current_activity(
            self,
            package,
            name_screen_activity,
            name_start_activity,
            same_activities=False
    ):
        """
        Проверить текущую activity приложения и запустить нужную

        :param package: Наименование пакета приложения
        :param name_screen_activity: Наименование экрана activity
        :param name_start_activity: Наименование старта activity
        :param same_activities: Флаг ставится, если текущая activity должна совпадать с передаваемой в метод (name_screen_activity).
        Не ставится, если совпадать не должна
        :return:
        """
        sleep(1)
        if same_activities:
            if self.driver.current_activity == name_screen_activity:
                    self.log.info(
                        "Текущая activity совпадает с ожидаемой activity '{0}'. Запуск  activity: '{1}'".format(
                            name_screen_activity, name_start_activity))
                    self.driver.start_activity(package, name_start_activity)
        else:
            if self.driver.current_activity != name_screen_activity:
                    self.log.info(
                        "Текущая activity не совпадает с ожидаемой activity '{0}'. Запуск  activity: '{1}'".format(
                            name_screen_activity, name_start_activity))
                    self.driver.start_activity(package, name_start_activity)

    def find_and_check_count_of_elements(self, locator, expected_value: int):
        """
        Найти элементы и проверить их количество

        :param locator: Локато для элемента
        :param expected_value: Ожидаемое количество элементов
        :return int: Количество элементов соответствует заданному значению
        """
        if len(self.find_element_helper.get_elements(
                locator)) == expected_value:
            self.log.info(
                "Количество элементов c локатором: '{0}' совпадает с тем, что ожидали получить". format(locator))
        else:
            message = "Количество элементов с локатором: '{0}' не совпадает с тем, что ожидали получить". \
                format(locator)
            self.log.critical(message)
            assert False, message

    def get_number_of_elements(self, locator):
        """
        Получить количество элементов

        :param locator: Локатор для элементов
        :return int: Количество элементов
        """
        return (len(self.find_element_helper.get_elements(locator)))

    def send_data_and_hide_keyboard(self, locator, text: str):
        """
        Отправить данные и скрыть клавиатуру

        :param locator: Локатор для поля элемента отправки данных
        :param text: Текст для отправки
        :return:
        """
        platform = self.service_function_helper.get_device_capabilities('platformName')
        self.send_data(locator, text)
        if platform != 'iOS':
            self.keyboard_element_helper.hide_keyboard()

    def tap_and_send_value_at_same_locator(self, locator, text: str):
        """
        Нажатие на элемент и отправка в него данные

        :param locator: Локатор для элемента нажатия и отправки данных
        :param text: Данные для отправки
        :return:
        """
        self.tap_and_press_element_helper.tap(locator)
        self.send_data(locator, text)
