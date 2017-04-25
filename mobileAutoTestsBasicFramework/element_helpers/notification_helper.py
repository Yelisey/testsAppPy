from element_helpers.find_element_helper import FindElementHelper
from element_helpers.tap_and_press_element_helper import TapAndPressElementHelper
from PIL import Image
from model.parameter_driver_for_helper import ParameterDriverForHelper
from time import sleep

import _thread
import pytesseract
import os
import logging


class NotificationHelper(ParameterDriverForHelper):

    def __init__(
            self,
            log: logging.Logger,
            find_element_helper: FindElementHelper,
            tap_and_press_element_helper: TapAndPressElementHelper):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        :param find_element_helper: Инициализация хелпера для поиска элементов
        :param tap_and_press_element_helper: Инициализация хелпера для тапов
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        assert isinstance(find_element_helper, FindElementHelper)
        assert isinstance(tap_and_press_element_helper, TapAndPressElementHelper)
        self.find_element_helper = find_element_helper
        self.tap_and_press_element_helper = tap_and_press_element_helper

    def find_element_and_tap_to_check_toast(self, locator, toast_msg: str):
        """
        Поиск элемента и проверка всплывающего окна
        :param locator: Локатор для искомого элемента
        :param toast_msg: Сообщение тоста
        :return True: Текст отбражается на экране
        """
        self.log.info("Проверка текста тоста на экране : " + str(toast_msg))
        self.find_element_helper.get_element(locator)
        _thread.start_new_thread(self.take_screenshots, (toast_msg, 4), {})
        self.tap_and_press_element_helper.tap(locator)
        sleep(2)
        if not self.verify_text_on_screenshots(1, toast_msg):
            self.log.critical(
                "Текст: '{0}' не представлен на экране!!!".format(toast_msg))
            assert False
        else:
            assert True

    def take_screenshots(self, toast_message: str, channels):
        """
        Снять скриншот с экрана устройства
        :param toast_message: Сообщение тоста
        :param channels: Количество каналов обработки изображения
        :return None:
        """
        for scr_num in range(0, channels):
            img_str64 = self.driver.get_screenshot_as_png()
            directory = os.path.join(
                os.getcwd(), "screenshots_with_toast", "rec_")
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(directory + "/{0}_{1}.png".format(toast_message, int(scr_num)), "wb") as f:
                f.write(img_str64)
                f.close()
            sleep(0.5)
        return None

    def verify_text_on_screenshots(self, channels, toast_msg: str):
        """
        Верификация текста со скриншота
        :param channels: Количество каналов обработки изображения
        :param toast_msg: Сообщение тоста
        :return True: Верифицировали текст с картинки
        :return False: Верификации текста с картинки не происходило
        """
        for scr_num in range(0, channels):
            if toast_msg in self.get_text_from_pic(
                pic_location=os.path.join(
                    os.getcwd(),
                    "screenshots_with_toast",
                    "rec_",
                    "{0}_{1}.png".format(
                        toast_msg,
                        channels)),
                    print_scanned_text=True):
                return True
        return False

    def get_text_from_pic(self, pic_location=None, print_scanned_text=True):
        """
        Вспомогательный метод получения текста со скриншота

        :param pic_location: Местоположение изображения
        :param print_scanned_text: Сканируемый текст
        :return str: Текст
        """
        im = Image.open(pic_location)
        im = im.convert('RGB')
        im.save(pic_location)
        rec_text = pytesseract.image_to_string(
            Image.open(pic_location), lang="rus")
        if print_scanned_text:
            print(rec_text)
        return rec_text