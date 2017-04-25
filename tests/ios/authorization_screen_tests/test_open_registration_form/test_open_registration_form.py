import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.ios.utils.screen_initialization_fixtures import authorization_screen_object, ios_utils
from screens.ios.authorization_screen.ios_authorization_screen import AuthorizationScreen
from screens.ios.authorization_screen.ios_authorization_screen import Utils


@pytest.mark.usefixtures('authorization_screen_object', 'ios_utils')
class TestRegistrationForm(BaseTest):


    authorization_screen_object = None  #type: AuthorizationScreen
    ios_utils = None                    #type: Utils


    @pytest.mark.order1
    def test_open_authorization_screen(self):
        self.authorization_screen_object.open_authorization_screen(self.get_locator("AuthorizationScreen", "sign_in_button"))


    @pytest.mark.order2
    def test_open_registration_form(self):
        self.ios_utils.open_screen_with_check(self.get_locator("AuthorizationScreen", "registration_button"),
                                              self.get_locator("AuthorizationScreen", "registration_form_title"))


    @pytest.mark.order3
    def test_back_from_registration_form(self):
        self.ios_utils.open_screen_with_check(self.get_locator("AuthorizationScreen", "close_registration_button"),
                                              self.get_locator("AuthorizationScreen", "login_field"))