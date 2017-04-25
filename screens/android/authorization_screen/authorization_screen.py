#coding:utf-8
from time import sleep

from mobileAutoTestsBasicFramework.model.application import Application
from screens.android.utils.utils import Utils
from screens.android.utils.screen_utility_fixtures import ScreenUtilityFixtures


class AuthorizationScreen(object):


    def __init__(self, app: Application):
        """
        Конструктор для инициализации параметров

        :param app: объект класса Application
        """
        self.app = app
        self.util = Utils(app)
        self.screen_utility_fixtures = ScreenUtilityFixtures(app)


    def authorize_with_domain(
            self,
            email_field,
            password_field,
            submit_button,
            email,
            password,
            expected_email):
        """
        Авторизация с разными доменами
        :param email_field: поле для ввода email
        :param password_field: поле для ввода login
        :param submit_button: кнопка "Войти"
        :param email: email для авторизации
        :param password: пароль для авторизации
        :param expected_email: email после автоподстановки доменного имени
        :return:
        """
        self.app.get_value_and_data_helper.tap_and_send_value_at_same_locator(
            email_field, email)
        domain_autocomplete = self.app.get_element_text_helper.get_element_text(email_field)
        if domain_autocomplete == expected_email:
            self.app.get_value_and_data_helper.send_data_and_hide_keyboard(password_field, password)
        self.app.get_tap_and_press_element_helper.tap(submit_button)
        self.util.close_welcome_screen()
        self.check_that_inbox_is_open()


    def authorization_with_ramblerru_domain(self):
        """
        Авторизация с аккаунтом рамблера с доменом @rambler.ru
        """
        email = self.util.email_data_rambler + "@"
        expected_email = self.util.email_data_rambler + "@rambler.ru"
        self.authorize_with_domain(
            self.util.get_locator('AuthorizationScreenElements', 'email_field'),
            self.util.get_locator('AuthorizationScreenElements', 'password_field'),
            self.util.get_locator('AuthorizationScreenElements', 'sign_in_button'),
            email, self.util.password_rambler, expected_email)


    def authorization_with_ro_domain(self):
        """
        Авторизация с аккаунтом рамблера с доменом @ro.ru
        """
        email = self.util.email_data_rambler + "@ro"
        expected_email = self.util.email_data_rambler + "@ro.ru"
        self.authorize_with_domain(
            self.util.get_locator('AuthorizationScreenElements', 'email_field'),
            self.util.get_locator('AuthorizationScreenElements', 'password_field'),
            self.util.get_locator('AuthorizationScreenElements', 'sign_in_button'),
            email, self.util.password_soc, expected_email)


    # TODO Не удаляются данные из поля пароля, так как поле распознается как пустое
    # def authorization_with_wrong_password(self):
    #     """
    #     Авторизация с некорректным паролем, затем ввод корректных данных
    #     """
    #     self.app.get_authorization_helper.auth_with_incorrect_password(
    #         self.util.get_locator('AuthorizationScreenElements', 'email_field'),
    #         self.util.get_locator('AuthorizationScreenElements', 'password_field'),
    #         self.util.get_locator('AuthorizationScreenElements', 'sign_in_button'), self.util.email_data_rambler)
    #     if not self.app.get_find_element_helper.is_visible_element(
    #             self.util.get_locator('AuthorizationScreenElements', 'main_toolbar')):
    #         text = self.app.get_element_text_helper.get_element_text(self.util.get_locator('AuthorizationScreenElements', 'password_field'))
    #         print(text)
    #         self.app.get_value_and_data_helper.delete_all_data(
    #             self.util.get_locator('AuthorizationScreenElements', 'password_field'))
    #         self.app.get_value_and_data_helper.send_data_and_hide_keyboard(
    #             self.util.get_locator('AuthorizationScreenElements', 'password_field'), self.util.password_rambler)
    #         self.app.get_tap_and_press_element_helper.tap(
    #             self.util.get_locator('AuthorizationScreenElements', 'sign_in_button'))
    #         self.check_that_inbox_is_open()


    def check_fields_are_empty(self):
        """
        Авторизация и проверка полей логина ввода на наличие символов
        :rtype boolean
        :return True - если поля логина и пароля пустые, False - если нет
        """
        self.app.get_authorization_helper.auth(
            self.util.get_locator('AuthorizationScreenElements', 'email_field'),
            self.util.get_locator('AuthorizationScreenElements', 'password_field'),
            self.util.get_locator('AuthorizationScreenElements', 'sign_in_button'),
            self.util.email_data_rambler, self.util.password_rambler)
        self.util.close_welcome_screen()
        self.app.get_wait_element_helper.wait_of_visible(self.util.get_locator('MainMenuScreen', 'inbox_toolbar'))
        self.logout()
        self.app.get_wait_element_helper.wait_of_visible(self.util.get_locator('AuthorizationScreenElements', 'rambler_logo'))
        email_field_content = self.app.get_element_text_helper.get_element_text(
            self.util.get_locator('AuthorizationScreenElements', 'email_field'))
        # TODO Текст в поле "пароль" распознается как "", сравнение длины теста полей логина и пароля не имеет смысла
        password_field_content = self.app.get_element_text_helper.get_element_text(
            self.util.get_locator('AuthorizationScreenElements', 'password_field'))
        if len(email_field_content) == 0 and len(password_field_content) == 0:
            return True
        else:
            assert False


    def authorize_with_social_network(self, email_field, password_field, submit_button, social_network_button,
                                      email, password, next_button=None):
        """
        Общий метод для авторизации через социальные сети, закрытие welcome screen и проверки, что открыта папка Входящие
        :param email_field: поле для ввода email
        :param password_field: поля для ввода пароля
        :param submit_button: кнопка "Войти"
        :param social_network_button: кнопка авторизации через социальную сеть
        :param email: email для авторизации
        :param password: пароль
        :param next_button: кнопка "Далее"
        :return:
        """
        self.app.get_authorization_helper.auth_with_social_network(email_field, password_field, submit_button,
                                                                   social_network_button, email, password, next_button)
        self.util.close_welcome_screen()
        self.check_that_inbox_is_open()


    def ok_authorization(self):
        """
        Авторизация в Одноклассниках
        """
        self.authorize_with_social_network(
            self.util.get_locator('AuthorizationScreenElements', 'ok_login_field'),
            self.util.get_locator('AuthorizationScreenElements', 'ok_password_field'),
            self.util.get_locator('AuthorizationScreenElements', 'ok_submit_button'),
            self.util.get_locator('AuthorizationScreenElements', 'ok_social_button'),
            self.util.tel_number, self.util.password_soc)


    def mailru_authorization(self):
        """
        Авторизация в Mail.ru
        """
        self.authorize_with_social_network(
            self.util.get_locator('AuthorizationScreenElements', 'mr_login_field'),
            self.util.get_locator('AuthorizationScreenElements', 'mr_password_field'),
            self.util.get_locator('AuthorizationScreenElements', 'mr_submit_button'),
            self.util.get_locator('AuthorizationScreenElements', 'mail_ru_social_button'),
            self.util.email_data_mailru, self.util.password_soc)


    # TODO Экран с подтверждением телефона
    # def google_authorization(self):
    #     """
    #     Авторизация в Google
    #     """
    #     self.authorize_with_social_network(
    #         self.util.get_locator('AuthorizationScreenElements', 'google_login_field'),
    #         self.util.get_locator('AuthorizationScreenElements', 'google_password_field'),
    #         self.util.get_locator('AuthorizationScreenElements', 'google_submit_button'),
    #         self.util.get_locator('AuthorizationScreenElements', 'google_plus_social_button'),
    #         self.util.email_data_soc, self.util.password_soc,
    #         self.util.get_locator('AuthorizationScreenElements', 'google_next_button'))


    def vk_authorization(self):
        """
        Авторизация в Вконтакте
        """
        self.authorize_with_social_network(
            self.util.get_locator('AuthorizationScreenElements', 'vk_login_field'),
            self.util.get_locator('AuthorizationScreenElements', 'vk_password_field'),
            self.util.get_locator('AuthorizationScreenElements', 'vk_submit_button'),
            self.util.get_locator('AuthorizationScreenElements', 'vk_social_button'),
            self.util.tel_number, self.util.password_soc)


    def facebook_authorization(self):
        """
        Авторизация в Facebook
        """
        self.authorize_with_social_network(
            self.util.get_locator('AuthorizationScreenElements', 'fb_login_field'),
            self.util.get_locator('AuthorizationScreenElements', 'fb_password_field'),
            self.util.get_locator('AuthorizationScreenElements', 'fb_submit_button'),
            self.util.get_locator('AuthorizationScreenElements', 'fb_social_button'),
            self.util.email_data_soc, self.util.password_soc)
        # TODO Отвалилась rambler ID, не могу проверить, для чего нужен этот sleep и на что его заменить
        sleep(5)


    def logout(self):
        """
        Разлогинивание залогиненого пользователя
        """
        self.app.get_tap_and_press_element_helper.multiple_tap((self.util.get_locator('AuthorizationScreenElements', 'menu_button')),
                                                               (self.util.get_locator('SettingsScreen', 'settings_button')))
        self.app.get_tap_and_press_element_helper.scroll_to_element_and_tap(self.util.get_locator('AuthorizationScreenElements', 'logout_button')),\
        self.app.get_keyboard_helper.hide_keyboard()


    def check_that_inbox_is_open(self):
        """
        Сравнение по частичному совпадению строку "Входящие" после логина
        """
        self.app.get_wait_element_helper.wait_of_visible(self.util.get_locator('MainMenuScreen', 'inbox_toolbar'))
        assert self.app.get_find_element_helper.is_visible_element(self.util.get_locator('MainMenuScreen', 'inbox_toolbar'))