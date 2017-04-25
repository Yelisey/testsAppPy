from element_helpers.value_and_data_element_helper import ValueAndDataElementHelper
from element_helpers.tap_and_press_element_helper import TapAndPressElementHelper
from element_helpers.keyboard_helper import KeyboardHelper
from selenium.common.exceptions import ElementNotVisibleException as error
from time import sleep
from random import randint

import logging


class AuthorizationHelper(object):

    def __init__(
            self,
            log: logging.Logger,
            value_and_data_element_helper: ValueAndDataElementHelper,
            tap_and_press_element_helper: TapAndPressElementHelper,
            keyboard_helper: KeyboardHelper):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        :param value_and_data_element_helper: Инициализация хелпера передачи данных
        :param tap_and_press_element_helper: Инициализация хелпера для тапов
        :param keyboard_helper: Инициализация хелпера взаимодействия с клавиатурой
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        assert isinstance(value_and_data_element_helper, ValueAndDataElementHelper)
        assert isinstance(tap_and_press_element_helper, TapAndPressElementHelper)
        assert isinstance(keyboard_helper, KeyboardHelper)
        self.tap_and_press_element_helper = tap_and_press_element_helper
        self.send_data_element_helper = value_and_data_element_helper
        self.keyboard_helper = keyboard_helper

    def auth(
            self,
            locator_email_field,
            locator_password_field,
            locator_submit_button,
            email_data,
            password_data,
            locator_next_button=None):
        """
        Основной метод авторизации

        :param locator_email_field: Локатор элемента для ввода email/Логина
        :param locator_password_field: Локатор элемента для ввода пароля
        :param locator_submit_button:  Локатор элемента для кнопки авторизации
        :param email_data: Данные для логина
        :param password_data: Данные для пароля
        :param locator_next_button:  Локатор элемента для кнопки "Далее"
        :return
        """
        try:
            self.log.info("Запуск процесса авторизации")
            self.log.info(
                "Тапаем на поле email с локатором: '{0}'".format(locator_email_field))
            self.send_data_element_helper.tap_and_send_value_at_same_locator(
                locator_email_field, email_data)
            if locator_next_button is not None:
                self.log.info("Тапаем на кнопку 'Далее' с локатором: '{0}' для перехода к экрану ввода пароля".
                              format(locator_next_button))
                self.tap_and_press_element_helper.tap(locator_next_button)
            self.log.info(
                "Тапаем на поле password с локатором: '{0}'".format(locator_password_field))
            self.tap_and_press_element_helper.tap(locator_password_field)
            self.send_data_element_helper.send_data_and_hide_keyboard(
                locator_password_field, password_data)
            self.log.info("Тапаем на кнопку подтверждения авторизации c локатором: '{0}'".
                          format(locator_submit_button))
            self.tap_and_press_element_helper.tap(locator_submit_button)
            self.log.info("Авторизация прошла успешно")
        except error:
            message = "Не удалось авторизоваться из-за ошибки: '{0}'".format(
                error)
            self.log.critical(message)
            assert False, message

    def auth_with_social_network(
            self,
            locator_email_field,
            locator_password_field,
            locator_submit_button,
            locator_social_network,
            email_data,
            password_data,
            locator_next_button=None):
        """
        Авторизация через социальную сеть

        :param locator_email_field: Локатор элемента для ввода email/Логина
        :param locator_password_field: Локатор элемента для ввода пароля
        :param locator_submit_button: Локатор элемента для кнопки авторизации
        :param locator_social_network: Локатор элемента для кнопки социальной сети
        :param email_data: Данные для логина
        :param password_data: Данные для пароля
        :param locator_next_button: Локатор элемента для кнопки "Далее"
        :return
        """
        try:
            self.log.info("Тапаем на кнопку c локатором: '{0}' для перехода к экрану авторизации в социальной сети".
                          format(locator_social_network))
            self.tap_and_press_element_helper.tap(locator_social_network)
            sleep(3)
            self.auth(
                locator_email_field,
                locator_password_field,
                locator_submit_button,
                email_data,
                password_data,
                locator_next_button)
        except error:
            message = "Не удалось авторизоваться через социальную сеть из-за ошибки: '{0}'".format(
                error)
            self.log.critical(message)
            assert False, message

    def auth_with_incorrect_email(
            self,
            locator_email_field,
            locator_password_field,
            locator_submit_button,
            password_data):
        """
        Авторизация с некорректным email

        :param locator_email_field: Локатор элемента для ввода логина
        :param locator_password_field: Локатор элемента для ввода пароля
        :param locator_submit_button: Локатор элемента для кнопки подтверждения
        :param password_data: Данные для пароля
        :return
        """
        email_data = "user_{0}".format(randint(0, 1000))
        self.auth(
            locator_email_field,
            locator_password_field,
            locator_submit_button,
            email_data,
            password_data)

    def auth_with_incorrect_password(
            self,
            locator_email_field,
            locator_password_field,
            locator_submit_button,
            email_data):
        """
        Авторизация с некорректным паролем

        :param locator_email_field: Локатор элемента для ввода логина
        :param locator_password_field: Локатор элемента для ввода пароля
        :param locator_submit_button: Локатор элемента для кнопки подтверждения
        :param email_data: Данные для ввода логина
        :return
        """
        password_data = "password_{0}".format(randint(0, 1000))
        self.auth(
            locator_email_field,
            locator_password_field,
            locator_submit_button,
            email_data,
            password_data)

    def auth_with_incorrect_data(
            self,
            locator_email_field,
            locator_password_field,
            locator_submit_button):
        """
        Авторизация с некорректными данными

        :param locator_email_field: Локатор элемента для ввода логина
        :param locator_password_field: Локатор элемента для ввода пароля
        :param locator_submit_button: Локатор элемента для кнопки подтверждения
        :return
        """
        email_data = "user_{0}".format(randint(0, 1000))
        password_data = "password_{0}".format(randint(0, 1000))
        self.auth(
            locator_email_field,
            locator_password_field,
            locator_submit_button,
            email_data,
            password_data)

    def auth_with_empty_email(
            self,
            locator_email,
            locator_password,
            locator_submit_button,
            password_data):
        """
        Авторизация с пустым email

        :param locator_email: Локатор элемента для ввода логина
        :param locator_password: Локатор элемента для ввода пароля
        :param locator_submit_button: Локатор элемента для кнопки подтверждения
        :param password_data: Данные для пароля
        :return
        """
        self.auth(
            locator_email,
            locator_password,
            locator_submit_button,
            '',
            password_data)

    def auth_with_empty_password(
            self,
            locator_email,
            locator_password,
            locator_submit_button,
            email_data):
        """
        Авторизация с пустым паролем

        :param locator_email: Локатор элемента для ввода логина
        :param locator_password: Локатор элемента для ввода пароля
        :param locator_submit_button: Локатор элемента для кнопки подтверждения
        :param email_data: Данные для логина
        :return
        """
        self.auth(
            locator_email,
            locator_password,
            locator_submit_button,
            email_data,
            '')

    def auth_with_empty_data(
            self,
            locator_email,
            locator_password,
            locator_submit_button):
        """
        Авторизация с пустыми паролем/email

        :param locator_email: Локатор элемента для ввода логина
        :param locator_password: Локатор элемента для ввода пароля
        :param locator_submit_button: Локатор элемента для кнопки подтверждения
        :return
        """
        self.auth(
            locator_email,
            locator_password,
            locator_submit_button,
            '',
            '')
