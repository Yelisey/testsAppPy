#coding:utf-8

from mobileAutoTestsBasicFramework.model.application import Application
from screens.ios.utils.utils import Utils


class AuthorizationScreen(object):


    def __init__(self, app: Application):
        """
        Конструктор для инициализации параметров

        :param app: объект класса Application
        """
        self.app = app
        self.util = Utils(app)


    def open_authorization_screen(self, sign_in_button):
        login_field_visible = self.app.get_find_element_helper.is_visible_element(sign_in_button)
        if login_field_visible == False:
            self.app.get_service_function_helper.reinstall_app('ru.rambler.mail')


    def fill_login_field(self, login_field, email):
        self.app.get_value_and_data_helper.tap_and_send_value_at_same_locator(login_field, email)


    def fill_password_field(self, password_field, password):
        self.app.get_value_and_data_helper.tap_and_send_value_at_same_locator(password_field, password)


    def sign_in(self, sign_in_button, inbox_screen_title, welcome_screen_locator=None):
        self.app.get_tap_and_press_element_helper.tap(sign_in_button)
        if welcome_screen_locator:
            self.util.close_welcome_screen(welcome_screen_locator)
        self.app.get_wait_element_helper.wait_of_visible(inbox_screen_title)
        self.app.get_find_element_helper.is_visible_element(inbox_screen_title)


    def check_fields_empty(self, login_field, password_field):
        login_field_text = self.app.get_element_text_helper.get_element_text(login_field)
        password_field_text = self.app.get_element_text_helper.get_element_text(password_field)
        if login_field_text.lower() == 'логин' and password_field_text.lower() == 'пароль':
            return True
        else:
            assert False


    def open_social_net_authorization_form(self, social_net_button, inbox_toolbar=None):
        self.util.open_screen_with_check(social_net_button, inbox_toolbar)