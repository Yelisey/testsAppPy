import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.ios.utils.screen_initialization_fixtures import authorization_screen_object, ios_utils
from screens.ios.authorization_screen.ios_authorization_screen import AuthorizationScreen
from screens.ios.authorization_screen.ios_authorization_screen import Utils


@pytest.mark.usefixtures('authorization_screen_object', 'ios_utils')
class TestAuthWithRamblerRu(BaseTest):


    authorization_screen_object = None  #type: AuthorizationScreen
    ios_utils = None                    #type: Utils


    @pytest.mark.order1
    def test_open_authorization_screen(self):
        self.authorization_screen_object.open_authorization_screen(self.get_locator("AuthorizationScreen", "sign_in_button"))


    @pytest.mark.order2
    def test_fill_in_login(self):
        self.authorization_screen_object.fill_login_field(self.get_locator("AuthorizationScreen", "login_field"),
                                                          self.ios_utils.email_rambler)


    @pytest.mark.order3
    def test_fill_in_password(self):
        self.authorization_screen_object.fill_password_field(self.get_locator("AuthorizationScreen", "password_field"),
                                                          self.ios_utils.password_rambler)


    @pytest.mark.order4
    def test_rambler_ru_sign(self):
        self.authorization_screen_object.sign_in(self.get_locator("AuthorizationScreen", "sign_in_button"),
                                                 self.get_locator("AuthorizationScreen", "inbox_screen_title"),
                                                 self.get_locator("AuthorizationScreen", "welcome_screen_button"))


    @pytest.mark.order5
    def test_logout(self):
        self.ios_utils.logout(self.get_locator("AuthorizationScreen", "menu_button"),
                              self.get_locator("AuthorizationScreen", "menu_screen_title"),
                              self.get_locator("AuthorizationScreen", "settings_button"),
                              self.get_locator("AuthorizationScreen", "settings_screen_title"),
                              self.get_locator("AuthorizationScreen", "log_out_button"),
                              self.get_locator("AuthorizationScreen", "login_field"))


    @pytest.mark.order6
    def test_check_if_fields_empty_after_logout(self):
        self.authorization_screen_object.check_fields_empty(self.get_locator("AuthorizationScreen", "login_field"),
                                                            self.get_locator("AuthorizationScreen", "password_field"))