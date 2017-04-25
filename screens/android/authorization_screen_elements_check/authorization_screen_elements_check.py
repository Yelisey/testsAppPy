#coding:utf-8
from mobileAutoTestsBasicFramework.model.application import Application
from screens.android.utils.utils import Utils
from screens.android.utils.screen_utility_fixtures import ScreenUtilityFixtures


class AuthorizationScreenElements(object):


    def __init__(self, app: Application):
        """
        Конструктор инициализации параметров, необходимых для методов описания экрана авторизации
        :param app: объект класса Application
        :param util: объект класса Utils
        """
        self.app = app
        self.util = Utils(app)
        self.screen_utility_fixtures = ScreenUtilityFixtures(app)


    def check_if_authorization_open(self):
        """
        Проверка, открыт ли экран авторизации
        :rtype boolean
        :return: True - если открыт, False - если нет
        """
        assert self.app.get_find_element_helper.is_visible_element(self.util.get_locator("AuthorizationScreenElements",
                                                                                          "authorization_screen"))


    def check_if_logo_present(self):
        """
        Проверка наличия логотипа Рамблер/почта
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        return self.app.get_find_element_helper.is_visible_element(self.util.get_locator("AuthorizationScreenElements",
                                                                                          "rambler_logo"))


    def check_if_email_and_password_are_present(self):
        """
        Проверка наличия полей email, списка доменов и пароля
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        for locator in [self.util.get_locator("AuthorizationScreenElements", "email_field"),
                        self.util.get_locator("AuthorizationScreenElements", "password_field"),
                        self.util.get_locator("AuthorizationScreenElements", "email_domain_selectbox")]:
            return self.app.get_find_element_helper.is_visible_element(locator)


    def check_if_sign_in_button_present(self):
        """
        Проверка наличия кнопки "Войти"
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        return self.app.get_find_element_helper.is_visible_element(self.util.get_locator("AuthorizationScreenElements",
                                                                                          "sign_in_button"))


    def check_if_social_net_buttons_present(self):
        """
        Проверка наличия кнопок авторизации в социальных сетях
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("AuthorizationScreenElements", "show_more_social_buttons"))
        for locator in [self.util.get_locator("AuthorizationScreenElements", "vk_social_button"),
                        self.util.get_locator("AuthorizationScreenElements", "fb_social_button"),
                        self.util.get_locator("AuthorizationScreenElements", "mail_ru_social_button"),
                        self.util.get_locator("AuthorizationScreenElements", "ok_social_button"),
                        self.util.get_locator("AuthorizationScreenElements", "tw_social_button"),
                        self.util.get_locator("AuthorizationScreenElements", "google_plus_social_button")]:
            assert self.app.get_find_element_helper.is_visible_element(locator)


    def check_is_forget_password_button_present(self):
        """
        Проверка наличия кнопки "Забыли пароль?"
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        return self.app.get_find_element_helper.is_visible_element(self.util.get_locator("AuthorizationScreenElements",
                                                                                          "forget_password_button"))

    def check_is_registration_button_present(self):
        """
        Проверка наличия кнопки "Зарегистрироваться"
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        return self.app.get_find_element_helper.is_visible_element(self.util.get_locator("AuthorizationScreenElements",
                                                                                          "registration_button"))


    # TODO Временно убрали этот кейс, как как нельзя определить, есть ли клавиатура на экране.
    # def check_keyboard_is_hiding(self):
    #     """
    #     Проверка отображения/скрытия клавиатуры
    #     :return:
    #     """
    #     self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("AuthorizationScreenElements", "email_field"))
    #     self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("AuthorizationScreenElements", "rambler_logo"))


    def check_captcha(self):
        """
        Проверка появления captcha (заполняются поля email и пароль,
        кнопка "Войти" нажимается до тех пор, пока не появится captcha)
        :rtype boolean
        :return: True - если captcha появилась после 5 тапов на кнопку "Войти",
        False - если нет
        """
        self.app.get_value_and_data_helper.send_data(self.util.get_locator("AuthorizationScreenElements",
                                                                            "email_field"), self.util.email)
        self.app.get_value_and_data_helper.send_data_and_hide_keyboard(self.util.get_locator("AuthorizationScreenElements",
                                                                            "password_field"), self.util.password)
        for i in range(0, 5):
            self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("AuthorizationScreenElements",
                                                                           "sign_in_button"))
            captcha_is_visible = self.app.get_find_element_helper.is_visible_element(
                self.util.get_locator("AuthorizationScreenElements", "captcha"))
            if captcha_is_visible == True:
                return True


    def check_restore_access_button(self):
        """
        Проверка перехода на форму восстановления пароля и возврата
        :return:
        """
        assert self.util.open_screen_with_check(self.util.get_locator("AuthorizationScreenElements",
                                                                 "forget_password_button"),
                                                self.util.get_locator("AuthorizationScreenElements", "browser"), True)
        self.app.get_keyboard_helper.android_back()


    def check_registration_button(self):
        """
        Проверка перехода на форму регистрации и возврата
        :return:
        """
        assert self.util.open_screen_with_check(
            self.util.get_locator("AuthorizationScreenElements", "registration_button"),
            self.util.get_locator("AuthorizationScreenElements", "registration_toolbar"), True)
        self.app.get_keyboard_helper.android_back()