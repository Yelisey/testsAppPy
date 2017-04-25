import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.ios.utils.screen_initialization_fixtures import settings_screen_object, ios_utils
from screens.ios.settings_screen.ios_settings_screen import SettingsScreen
from screens.ios.settings_screen.ios_settings_screen import Utils


@pytest.mark.usefixtures('settings_screen_object', 'ios_utils')
class TestSettingsScreenElements(BaseTest):

    settings_screen_object = None  #type: SettingsScreen
    ios_utils = None                    #type: Utils


    @pytest.mark.order1
    def test_check_if_autorized(self):
        self.ios_utils.test_check_if_autorized_and_log_in(self.get_locator("AuthorizationScreen", "login_field"),
                                                          self.get_locator("AuthorizationScreen", "password_field"),
                                                          self.get_locator("AuthorizationScreen", "sign_in_button"),
                                                          self.ios_utils.email_rambler,
                                                          self.ios_utils.password_rambler,
                                                          self.get_locator("AuthorizationScreen", "welcome_screen_button"),
                                                          self.get_locator("SettingsScreen", "menu_button"))


    @pytest.mark.order2
    def test_open_menu(self):
        self.ios_utils.open_side_menu(self.get_locator("SettingsScreen", "menu_button"),
                                      self.get_locator("SettingsScreen", "menu_screen_title"))


    @pytest.mark.order3
    def test_open_settings(self):
        self.ios_utils.open_settings(self.get_locator("SettingsScreen", "settings_button"),
                                     self.get_locator("SettingsScreen", "settings_screen_title"))


    @pytest.mark.order4
    def test_open_send_feedback_form(self):
        self.ios_utils.open_screen_with_check(self.get_locator("SettingsScreen", "send_feedback"),
                                              self.get_locator("SettingsScreen", "feedback_screen_title"),
                                              scroll=True)


    @pytest.mark.order5
    def test_check_feedback_screen_elements_are_visible(self):
        self.settings_screen_object.check_elements_are_visible(self.get_locator("SettingsScreen", "report_bug"),
                                                               self.get_locator("SettingsScreen", "new_feature"),
                                                               self.get_locator("SettingsScreen", "other"),
                                                               self.get_locator("SettingsScreen", "send_button"),
                                                               tap=True)


    @pytest.mark.order6
    def test_go_back_from_feedback_form(self):
        self.ios_utils.open_screen_with_check(self.get_locator("SettingsScreen", "back_from_feedback_button"),
                                              self.get_locator("SettingsScreen", "settings_screen_title"))
