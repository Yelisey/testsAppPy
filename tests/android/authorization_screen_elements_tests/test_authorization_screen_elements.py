import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.android.authorization_screen_elements_check.authorization_screen_elements_check import AuthorizationScreenElements
from screens.android.utils.screen_initialization_fixtures import authorization_screen_elements_object


@pytest.fixture()
def close_popup(authorization_screen_elements_object: AuthorizationScreenElements):
    """
    Фикстура для закрытия popup про обновление приложения до последней версии
    :param authorization_screen_elements_object: объект класса AuthorizationScreenElements
    :return:
    """
    authorization_screen_elements_object.screen_utility_fixtures.close_popup_fixture()


@pytest.fixture(scope="function")
def check_if_authorization_open(authorization_screen_elements_object: AuthorizationScreenElements):
    """
    Фикстура для создания предусловий для тестов элементов экрана авторизации
    :param authorization_screen_elements_object: объект класса AuthorizationScreenElements
    :return:
    """
    authorization_screen_elements_object.screen_utility_fixtures.authorization_elements_screen_fixture()


@pytest.mark.usefixtures("authorization_screen_elements_object", "close_popup", "check_if_authorization_open")
class TestAuthorizationScreenElements(BaseTest):

    authorization_screen_elements_object = None  # type: AuthorizationScreenElements


    def test_C145865_check_if_logo_present(self):
        """
        Проверка наличия логотипа на экране авторизации
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        assert self.authorization_screen_elements_object.check_if_logo_present()


    def test_C145867_check_if_email_and_password_are_present(self):
        """
        Проверка наличия полей E-mail\Пароль
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        assert self.authorization_screen_elements_object.check_if_email_and_password_are_present()


    def test_C145868_check_if_sign_in_button_present(self):
        """
        Проверка наличия кнопки "Войти"
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        assert self.authorization_screen_elements_object.check_if_sign_in_button_present()


    def test_C145869_check_if_social_net_buttons_present(self):
        """
        Проверка наличия кнопок авторизации в соцсетях
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        self.authorization_screen_elements_object.check_if_social_net_buttons_present()


    def test_C145871_check_if_forget_password_button_present(self):
        """
        Проверка наличия ссылки на форму восстановления пароля
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        assert self.authorization_screen_elements_object.check_is_forget_password_button_present()


    def test_C145872_check_if_registration_button_present(self):
        """
        Проверка наличия ссылки на форму регистрации
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        assert self.authorization_screen_elements_object.check_is_registration_button_present()


    def test_C146083_check_captcha(self):
        """
        Проверка появления блока captcha
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        assert self.authorization_screen_elements_object.check_captcha()


    # TODO Невозможно определить наличие клавиатуры на экране, как только найдется способ, нужно доделать.
    # def test_C151996_check_keyboard_is_hiding(self):
    #     """
    #     Проверка скрытия клавиатуры при тапе вне поля ввода
    #     :param authorization_screen_object: объект класса AuthorizationScreenElements
    #     :return:
    #     """
    #     self.authorization_screen_elements_object.check_keyboard_is_hiding()


    def test_C145882_check_restore_access_button(self):
        """
        Переход на форму восстановления пароля
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        self.authorization_screen_elements_object.check_restore_access_button()


    def test_C146354_check_registration_button(self):
        """
        Переход и возврат с формы регистрации
        :param authorization_screen_object: объект класса AuthorizationScreenElements
        :return:
        """
        self.authorization_screen_elements_object.check_registration_button()