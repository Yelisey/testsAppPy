#coding:utf-8

from mobileAutoTestsBasicFramework.model.application import Application
from screens.ios.utils.utils import Utils


class SettingsScreen(object):

    def __init__(self, app: Application):
        """
        Конструктор для инициализации параметров

        :param app: объект класса Application
        """
        self.app = app
        self.util = Utils(app)


    def check_elements_are_visible(self, *elements, scroll=False, tap=False):
        if scroll:
            self.app.get_scroll_and_swipe_element_helper.scroll_to_direction()
        if tap:
            self.app.get_tap_and_press_element_helper.tap(elements[0])
        for element in elements:
            assert self.app.get_find_element_helper.is_visible_element(element)


    def open_feedback_form(self, feedback_button, feedback_screen_title):
        self.app.get_scroll_and_swipe_element_helper.scroll_to_direction()
        self.util.open_screen_with_check(feedback_button, feedback_screen_title)