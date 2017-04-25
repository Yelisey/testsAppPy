from selenium.common.exceptions import WebDriverException as error
from model.parameter_driver_for_helper import ParameterDriverForHelper
from time import sleep

import logging


class KeyboardHelper(ParameterDriverForHelper):

    def __init__(self, log: logging.Logger):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log

    # TODO Поддержка hide_keyboard не реализована в XCUITest https://github.com/appium/appium/issues/6816
    def hide_keyboard(self):
        """
        Скрыть клавиатуру
        :return:
        """
        self.log.info("Скрываем клавиатуру девайса")
        try:
            sleep(1)
            self.driver.hide_keyboard()
            self.log.info("Клавиатура девайса скрыта")
        except error:
            self.log.critical(
                "Скрыть клавиатуру не удалось! Из-за ошибки: '{0}'".format(error))
            pass

    def press_keycode(self, number):
        """
        Коды клавиатуры, например код 66 = Enter , более подробно про номера кодов здесь -
        https://developer.android.com/reference/android/view/KeyEvent.html
        :param number: Код для исполнения
        :return:
        """
        self.driver.press_keycode(number)

    def android_back(self):
        """
        Метод нажатия системной кнопки "Назад" в Android
        :return:
        """
        self.driver.back()
