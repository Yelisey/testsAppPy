#coding:utf-8
from mobileAutoTestsBasicFramework.model.application import Application
from screens.android.authorization_screen.authorization_screen import AuthorizationScreen
from screens.android.utils.utils import Utils
from screens.android.utils.screen_utility_fixtures import ScreenUtilityFixtures

import random


class SettingsScreen(object):


    def __init__(self, app: Application):
        """
        Конструктор инициализации параметров, необходимых для методов описания экрана настроек
        :param app: объект класса Application
        :param auth_screen: объект класса AuthorizationScreen
        :param util: объект класса Utils
        """
        self.app = app
        self.auth_screen = AuthorizationScreen(app)
        self.util = Utils(app)
        self.screen_utility_fixtures = ScreenUtilityFixtures(app)


    def check_fields(self, field_in_settings, element_to_open, text_edit, confirmation_button, text_to_fill_in):
        """
        Проверка полей Имя и Подпись (общий метод для заполнения этих полей и проверки сохранения данных)
        :param field_in_settings: поле, которое нужно проверять на экране настройки
        :param element_to_open: элемент, в котором находится поле EditText
        :param text_to_fill_in: текст для заполнения поля
        :return:
        """
        self.util.open_screen_with_check(field_in_settings, element_to_open)
        text_len = self.app.get_element_text_helper.get_element_text(text_edit)
        if len(text_len) != 0:
            self.app.get_tap_and_press_element_helper.tap(text_edit)
            self.app.get_value_and_data_helper.delete_all_data(text_edit)
        self.app.get_value_and_data_helper.send_data(text_edit,
                                                     text_to_fill_in)
        self.util.open_screen_with_check(confirmation_button, self.util.get_locator("SettingsScreen", "settings_toolbar"))
        self.app.get_element_text_helper.compare_element_text(field_in_settings, text_to_fill_in)


    def check_switcher_position(self, switcher_locator):
        """
        Проверка положения свичера
        :param switcher_locator: локатор свитчера
        :rtype boolean
        :return: если True - состояние свитчера вкл/выкл не совпадает с изначальным, если False - совпадает (переключение не сработало)
        """
        initial_switcher_position = self.app.get_value_and_data_helper.get_checked_property(switcher_locator)
        self.app.get_tap_and_press_element_helper.tap(switcher_locator)
        current_switcher_position = self.app.get_value_and_data_helper.get_checked_property(switcher_locator)
        return not self.app.get_value_and_data_helper.compare_elements(initial_switcher_position,
                                                                       current_switcher_position)


    def turn_on_notifications_and_check_elements(self):
        """
        Включение уведомлений и проверка элементов в экране "Уведомления"
        :return:
        """
        self.turn_on_notifications()
        assert self.app.get_find_element_helper.is_enabled_element(self.util.get_locator("SettingsScreen",
                                                                                         "sound_settings"))
        assert self.app.get_find_element_helper.is_enabled_element(self.util.get_locator("SettingsScreen",
                                                                                    "vibration_switcher"))
        assert self.app.get_find_element_helper.is_enabled_element(self.util.get_locator("SettingsScreen",
                                                                                         "dont_disturb_button"))
        assert self.app.get_find_element_helper.is_enabled_element(self.util.get_locator("SettingsScreen",
                                                                                         "privacy_button"))
        self.app.get_keyboard_helper.android_back()


    def turn_on_notifications(self):
        """
        Включение уведомлений
        :return:
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("SettingsScreen", "notifications_screen_button"))
        current_switcher_position = self.app.get_value_and_data_helper.get_checked_property(
            self.util.get_locator("SettingsScreen", "notifications_switcher"))
        if current_switcher_position == "false":
            self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("SettingsScreen", "notifications_switcher"))



    def select_random_sound(self):
        """
        Выбор и сохранение рандомной мелодии уведомлений
        :rtype boolean
        :return: True - название мелодии совпадает, False - не совпадает
        """
        list = self.app.get_find_element_helper.get_elements(self.util.get_locator("SettingsScreen", "sounds_list"))
        selected_sound = (random.choice(list))
        selected_sound_text = selected_sound.text
        self.app.get_tap_and_press_element_helper.tap(('xpath', "//*[@text='{0}']".format(selected_sound_text)))
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("SettingsScreen", "ok_button"))
        selected_sound_in_menu_text = self.app.get_element_text_helper.get_element_text(
            self.util.get_locator("SettingsScreen", "selected_sound_in_settings"))
        return self.app.get_value_and_data_helper.compare_elements(selected_sound_text, selected_sound_in_menu_text)


    def name_settings(self):
        """
        Проверка поля Имя
        :return:
        """
        self.check_fields(self.util.get_locator("SettingsScreen", "your_name_field"),
                          self.util.get_locator("SettingsScreen", "popup"),
                          self.util.get_locator("SettingsScreen", "text_edit_for_name_popup"),
                          self.util.get_locator("SettingsScreen", "ok_button"),
                          self.util.name_text)


    def signature_settings(self):
        """
        Проверка поля Подпись
        :return:
        """
        self.check_fields(self.util.get_locator("SettingsScreen", "signature_field"),
                          self.util.get_locator("SettingsScreen", "signature_window"),
                          self.util.get_locator("SettingsScreen", "text_edit_for_signature"),
                          self.util.get_locator("SettingsScreen", "save_signature_button"),
                          self.util.signature_text)
        self.app.get_keyboard_helper.hide_keyboard()


    def check_notification_switcher(self):
        """
        Проверка свитчера уведомлений
        :rtype
        :return:
        """
        self.app.get_tap_and_press_element_helper.tap(
            self.util.get_locator("SettingsScreen", "notifications_screen_button"))
        assert self.check_switcher_position(self.util.get_locator("SettingsScreen", "notifications_switcher"))
        self.app.get_keyboard_helper.android_back()


    def check_sound_settings(self):
        """
        Проверка настроек звука
        :rtype
        :return:
        """
        self.turn_on_notifications()
        assert self.util.open_screen_with_check(self.util.get_locator("SettingsScreen", "sound_settings"),
                                                self.util.get_locator("SettingsScreen", "sounds_list_panel"))
        assert self.select_random_sound()
        self.app.get_keyboard_helper.android_back()


    def check_vibration_switcher(self):
        """
        Проверка свитчера вибросигнала
        :rtype
        :return:
        """
        self.turn_on_notifications()
        assert self.check_switcher_position(self.util.get_locator("SettingsScreen", "vibration_switcher"))
        self.app.get_keyboard_helper.android_back()


    def check_picture_settings(self):
        """
        Проверка настроек картинок
        :rtype
        :return:
        """
        initial_value = self.app.get_element_text_helper.get_element_text(
            self.util.get_locator("SettingsScreen", "pictures_settings"))
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("SettingsScreen", "pictures_settings"))
        if initial_value == self.app.get_element_text_helper.get_element_text(
                self.util.get_locator("SettingsScreen", "always_show_pictures_button")):
            self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("SettingsScreen", "ask_to_show_pictures"))
        else:
            self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("SettingsScreen",
                                                                          "always_show_pictures_button"))
        current_value = self.app.get_element_text_helper.get_element_text(
            self.util.get_locator("SettingsScreen", "pictures_settings"))
        assert not self.app.get_value_and_data_helper.compare_elements(initial_value, current_value)


    def check_if_cash_present(self):
        """
        Проверка строки Кэш
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        self.app.get_scroll_and_swipe_element_helper.scroll_while_element_is_invisible(
            self.util.get_locator("SettingsScreen", "cash_settings"))
        return self.app.get_find_element_helper.is_visible_element(self.util.get_locator("SettingsScreen",
                                                                                         "cash_settings"))