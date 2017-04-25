import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.ios.utils.screen_initialization_fixtures import main_menu_screen_object, ios_utils
from screens.ios.main_menu_screen.ios_main_menu_screen import MainMenuScreen
from screens.ios.authorization_screen.ios_authorization_screen import Utils


@pytest.mark.usefixtures('main_menu_screen_object', 'ios_utils')
class TestOpenFoldersFromMenu(BaseTest):

    main_menu_screen_object = None  # type: MainMenuScreen
    ios_utils = None  # type: Utils


    @pytest.mark.order1
    def test_check_if_autorized(self):
        self.ios_utils.test_check_if_autorized_and_log_in(
            self.get_locator("AuthorizationScreen", "login_field"),
            self.get_locator("AuthorizationScreen", "password_field"),
            self.get_locator("AuthorizationScreen", "sign_in_button"),
            self.ios_utils.email_rambler,
            self.ios_utils.password_rambler,
            self.get_locator("AuthorizationScreen", "welcome_screen_button"),
            self.get_locator("MainMenuScreen", "menu_button"))


    @pytest.mark.order2
    def test_open_inbox(self):
        self.main_menu_screen_object.open_folder_from_menu(
            self.get_locator("MainMenuScreen", "menu_button"),
            self.get_locator("MainMenuScreen", "menu_screen_title"),
            self.get_locator("MainMenuScreen", "inbox_folder"),
            self.get_locator("MainMenuScreen", "inbox_screen_title"))


    @pytest.mark.order3
    def test_open_sent(self):
        self.main_menu_screen_object.open_folder_from_menu(
            self.get_locator("MainMenuScreen", "menu_button"),
            self.get_locator("MainMenuScreen", "menu_screen_title"),
            self.get_locator("MainMenuScreen", "sent_folder"),
            self.get_locator("MainMenuScreen", "sent_screen_title"))


    @pytest.mark.order4
    def test_open_drafts(self):
        self.main_menu_screen_object.open_folder_from_menu(
            self.get_locator("MainMenuScreen", "menu_button"),
            self.get_locator("MainMenuScreen", "menu_screen_title"),
            self.get_locator("MainMenuScreen", "drafts_folder"),
            self.get_locator("MainMenuScreen", "drafts_screen_title"))


    @pytest.mark.order5
    def test_open_bin(self):
        self.main_menu_screen_object.open_folder_from_menu(
            self.get_locator("MainMenuScreen", "menu_button"),
            self.get_locator("MainMenuScreen", "menu_screen_title"),
            self.get_locator("MainMenuScreen", "bin_folder"),
            self.get_locator("MainMenuScreen", "bin_screen_title"))


    @pytest.mark.order6
    def test_open_spam(self):
        self.main_menu_screen_object.open_folder_from_menu(
            self.get_locator("MainMenuScreen", "menu_button"),
            self.get_locator("MainMenuScreen", "menu_screen_title"),
            self.get_locator("MainMenuScreen", "spam_folder"),
            self.get_locator("MainMenuScreen", "spam_screen_title"))


    @pytest.mark.order7
    def test_open_add_mailbox(self):
        self.main_menu_screen_object.open_folder_from_menu(
            self.get_locator("MainMenuScreen", "menu_button"),
            self.get_locator("MainMenuScreen", "menu_screen_title"),
            self.get_locator("MainMenuScreen", "add_mailbox"),
            self.get_locator("MainMenuScreen", "add_mailbox_screen_title"))