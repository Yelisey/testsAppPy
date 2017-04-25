import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.ios.utils.screen_initialization_fixtures import message_screen_object, new_mail_screen_object, ios_utils
from screens.ios.message_list_screen.ios_message_list_screen import MessageListScreen
from screens.ios.authorization_screen.ios_authorization_screen import Utils


@pytest.mark.usefixtures('message_screen_object', 'ios_utils')
class TestClearRecycleBin(BaseTest):

    message_screen_object = None   #type: MessageListScreen
    ios_utils = None               #type: Utils


    pass

    # TODO Не могу прогнать данный кейс, так как на 2-3 шаге тесты зависают
    # def test_check_if_authorized(self):
    #     self.ios_utils.test_check_if_autorized_and_log_in(
    #         self.get_locator("AuthorizationScreen", "login_field"),
    #         self.get_locator("AuthorizationScreen", "password_field"),
    #         self.get_locator("AuthorizationScreen", "sign_in_button"),
    #         self.ios_utils.email_rambler,
    #         self.ios_utils.password_rambler,
    #         self.get_locator("AuthorizationScreen", "welcome_screen_button"),
    #         self.get_locator("MessageListScreen", "menu_button"))
    #
    #
    # def test_clear_recycle_bin_before_test(self):
    #     self.message_screen_object.clear_folder(
    #         self.get_locator("MessageListScreen", "menu_button"),
    #         self.get_locator("MessageListScreen", "menu_screen_title"),
    #         self.get_locator("MessageListScreen", "clear_bin_from_menu"),
    #         self.get_locator("MessageListScreen", "clear_folder_dialog"),
    #         self.get_locator("MessageListScreen", "yes_button"))
    #
    #
    # def test_open_inbox(self):
    #     self.message_screen_object.open_inbox(
    #         self.get_locator("MessageListScreen", "inbox_folder"),
    #         self.get_locator("MessageListScreen", "inbox_screen_title"),)
    #
    #
    # def test_select_emails_and_move_emails_to_recycle_bin(self):
    #     self.message_screen_object.select_emails_and_move_to_folder(
    #         self.get_locator("MessageListScreen", "move_to_bin_button"))
    #
    #
    # def test_check_emails_present_in_bin(self):
    #     self.message_screen_object.check_folder_is_empty_or_not(
    #         self.get_locator("MessageListScreen", "menu_button"),
    #         self.get_locator("MessageListScreen", "menu_screen_title"),
    #         self.get_locator("MessageListScreen", "bin_folder"),
    #         self.get_locator("MessageListScreen", "bin_screen_title"),
    #         self.get_locator("MessageListScreen", "empty_folder_placeholder"))
    #
    #
    # def test_clear_recycle_bin(self):
    #     self.message_screen_object.clear_folder(
    #         self.get_locator("MessageListScreen", "menu_button"),
    #         self.get_locator("MessageListScreen", "menu_screen_title"),
    #         self.get_locator("MessageListScreen", "clear_bin_from_menu"),
    #         self.get_locator("MessageListScreen", "clear_folder_dialog"),
    #         self.get_locator("MessageListScreen", "yes_button"))
    #
    #
    # def test_check_recycle_bin_is_empty(self):
    #     self.message_screen_object.check_folder_is_empty_or_not(
    #         self.get_locator("MessageListScreen", "menu_button"),
    #         self.get_locator("MessageListScreen", "menu_screen_title"),
    #         self.get_locator("MessageListScreen", "bin_folder"),
    #         self.get_locator("MessageListScreen", "bin_screen_title"),
    #         self.get_locator("MessageListScreen", "empty_folder_placeholder"),
    #         empty=True)