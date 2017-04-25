import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.ios.utils.screen_initialization_fixtures import message_screen_object, new_mail_screen_object, ios_utils
from screens.ios.new_mail_screen.ios_new_mail_screen import NewMailScreen
from screens.ios.authorization_screen.ios_authorization_screen import Utils


@pytest.mark.usefixtures('new_mail_screen_object', 'ios_utils')
class TestSendEmail(BaseTest):

    new_mail_screen_object = None  #type: NewMailScreen
    ios_utils = None               #type: Utils


    @pytest.mark.order1
    def test_check_if_autorized(self):
        self.ios_utils.test_check_if_autorized_and_log_in(
            self.get_locator("AuthorizationScreen", "login_field"),
            self.get_locator("AuthorizationScreen", "password_field"),
            self.get_locator("AuthorizationScreen", "sign_in_button"),
            self.ios_utils.email_rambler,
            self.ios_utils.password_rambler,
            self.get_locator("AuthorizationScreen", "welcome_screen_button"),
            self.get_locator("MessageListScreen", "menu_button"))


    @pytest.mark.order2
    def test_open_new_mail_form(self):
        self.ios_utils.open_screen_with_check(
            self.get_locator("NewMailScreen", "new_mail_button"),
            self.get_locator("NewMailScreen", "send_button"))


    @pytest.mark.order3
    def test_fill_to_field(self):
        self.new_mail_screen_object.set_to_address(
            self.get_locator("NewMailScreen", "to_field"),
            self.ios_utils.address)


    @pytest.mark.order4
    def test_fill_subject_field(self):
        self.new_mail_screen_object.set_subject(self.get_locator("NewMailScreen", "subject_field"))


    @pytest.mark.order5
    def test_send_email(self):
        self.new_mail_screen_object.send_email(
            self.get_locator("NewMailScreen", "send_button"),
            self.get_locator("MessageListScreen", "inbox_screen_title"))


    @pytest.mark.order6
    def test_check_email_is_recieved(self):
        self.new_mail_screen_object.check_email_is_recieved()