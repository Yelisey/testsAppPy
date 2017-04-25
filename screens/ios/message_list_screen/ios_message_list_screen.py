#coding:utf-8

from mobileAutoTestsBasicFramework.model.application import Application
from screens.ios.utils.utils import Utils


class MessageListScreen(object):

    def __init__(self, app: Application):
        """
        Конструктор для инициализации параметров

        :param app: объект класса Application
        """
        self.app = app
        self.util = Utils(app)


    def clear_folder(self, menu_button, menu_screen_title, clear_folder_from_menu, clear_folder_dialog, yes_button):
        self.util.open_side_menu(menu_button, menu_screen_title)
        if self.app.get_value_and_data_helper.get_enabled_property(clear_folder_from_menu):
            self.app.get_tap_and_press_element_helper.tap(clear_folder_from_menu)
            self.app.get_wait_element_helper.wait_of_visible(clear_folder_dialog)
            self.app.get_tap_and_press_element_helper.tap(yes_button)


    def open_inbox(self, inbox_folder, inbox_screen_title):
        self.util.open_screen_with_check(inbox_folder, inbox_screen_title)


    def select_emails_and_move_to_folder(self, move_to_folder_button):
        elements_list = []
        for i in range(2, 7):
            email_locator = (
                'xpath', '//XCUIElementTypeTable/XCUIElementTypeCell[{0}]/XCUIElementTypeStaticText[2]'.format(i))
            email_object = self.app.get_find_element_helper.get_element(email_locator)
            elements_list.append(email_object)
        self.app.get_tap_and_press_element_helper.select_elements_and_long_press_on_first(elements_list)
        self.app.get_tap_and_press_element_helper.tap(move_to_folder_button)


    def check_folder_is_empty_or_not(self,
                    menu_button,
                    menu_screen_title,
                    move_to_folder_button,
                    folder_screen_title,
                    empty_folder_placeholder,
                                     empty=False):
        self.util.open_side_menu(menu_button, menu_screen_title)
        self.util.open_screen_with_check(move_to_folder_button, folder_screen_title)
        if empty:
            assert self.app.get_find_element_helper.is_visible_element(empty_folder_placeholder)
        else:
            assert not self.app.get_find_element_helper.is_visible_element(empty_folder_placeholder)