#coding:utf-8

from mobileAutoTestsBasicFramework.model.application import Application
from screens.ios.utils.utils import Utils


class MainMenuScreen(object):


    def __init__(self, app: Application):
        """
        Конструктор для инициализации параметров

        :param app: объект класса Application
        """
        self.app = app
        self.util = Utils(app)


    def check_if_other_apps_present(self, other_apps_button):
        self.app.get_scroll_and_swipe_element_helper.scroll_to_direction()
        self.app.get_find_element_helper.is_visible_element(other_apps_button)


    def open_folder_from_menu(self, menu_button, menu_screen_title, menu_folder, screen_name):
        is_menu_open = self.app.get_find_element_helper.is_visible_element(menu_screen_title)
        if is_menu_open is False:
            self.util.open_side_menu(menu_button, menu_screen_title)
        self.util.open_screen_with_check(menu_folder, screen_name)