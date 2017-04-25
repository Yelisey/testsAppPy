import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.android.authorization_screen.authorization_screen import AuthorizationScreen
from screens.android.utils.screen_initialization_fixtures import authorization_screen_object


@pytest.fixture()
def close_popup(authorization_screen_object: AuthorizationScreen):
    """
    Фикстура для закрытия popup про обновление приложения до последней версии
    :param authorization_screen_object: объект класса AuthorizationScreen
    :return:
    """
    authorization_screen_object.screen_utility_fixtures.close_popup_fixture()


@pytest.fixture(scope="function")
def check_auth_state(authorization_screen_object: AuthorizationScreen):
    """
    Фикстура для создания предусловий для тестов экрана авторизации
    :param authorization_screen_object: объект класса AuthorizationScreen
    :return:
    """
    authorization_screen_object.screen_utility_fixtures.authorization_screen_fixture()


@pytest.mark.usefixtures("authorization_screen_object", "close_popup", "check_auth_state")
class TestAuthorizationScreen(BaseTest):

    authorization_screen_object = None  # type: AuthorizationScreen


    def test_C152072_main_fields_are_empty(self):
        """
        Проверить, что учетные данные не сохраняются после logout

        :param authorization_screen_object: обьект класса AuthorizationScreen
        :return:
        """
        assert self.authorization_screen_object.check_fields_are_empty()


    def test_C145874_authorization_with_ramblerru_domain(self):
        """
        Авторизация в приложении с доменом @rambler.ru

        :param authorization_screen_object: обьект класса AuthorizationScreen
        :return:
        """
        self.authorization_screen_object.authorization_with_ramblerru_domain()


    def test_C145875_authorization_with_ro_domain(self):
        """
        Авторизация в приложении с доменом @ro.ru

        :param authorization_screen_object: обьект класса AuthorizationScreen
        :return:
        """
        self.authorization_screen_object.authorization_with_ro_domain()

    # TODO Не удаляются данные из поля пароля, так как поле распознается как пустое
    # def test_C146084_main_autorization_bad_password(self):
    #     """
    #     Авторизация в приложении после исправлении ошибочных данных
    #
    #     :param authorization_screen_object: обьект класса AuthorizationScreen
    #     :return:
    #     """
    #     self.authorization_screen_object.authorization_with_wrong_password()


    def test_C145879_mailru_authorization(self):
        """
        Авторизация в приложении через Mail.ru

        :param authorization_screen_object: обьект класса AuthorizationScreen
        :return:
        """
        self.authorization_screen_object.mailru_authorization()


    def test_C145878_ok_authorization(self):
        """
        Авторизация в приложении через Одноклассники

        :param authorization_screen_object: обьект класса AuthorizationScreen
        :return:
        """
        self.authorization_screen_object.ok_authorization()


    def test_C145876_vk_login(self):
        """
        Авторизация в приложении через Вконтакте

        :param authorization_screen_object: обьект класса AuthorizationScreen
        :return:
        """
        self.authorization_screen_object.vk_authorization()


    # TODO Временно убрали, так как требует подтверждение номера телефона
    # def test_C145880_google_authorization(self):
    #     """
    #     Авторизация в приложении через Google+
    #
    #     :param authorization_screen_object: обьект класса AuthorizationScreen
    #     :return:
    #     """
    #     self.authorization_screen_object.google_authorization()


    def test_C145877_facebook_authorization(self):
        """
        Авторизация в приложении через  Facebook

        :param authorization_screen_object: обьект класса AuthorizationScreen
        :return:
        """
        self.authorization_screen_object.facebook_authorization()