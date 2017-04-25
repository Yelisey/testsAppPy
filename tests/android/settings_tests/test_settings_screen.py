import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.android.settings_screen.settings_screen import SettingsScreen
from screens.android.utils.screen_initialization_fixtures import settings_screen_object


@pytest.fixture()
def close_popup(settings_screen_object: SettingsScreen):
    """
    Фикстура для закрытия popup про обновление приложения до последней версии
    :param settings_screen_object: объект класса SettingsScreen
    :return:
    """
    settings_screen_object.screen_utility_fixtures.close_popup_fixture()


@pytest.fixture(scope="function")
def open_settings(settings_screen_object: SettingsScreen):
    """
    Фикстура для создания предусловий для тестов экрана настроек
    :param settings_screen_object: объект класса SettingsScreen
    :return:
    """
    settings_screen_object.screen_utility_fixtures.settings_screen_fixture()


@pytest.mark.usefixtures("settings_screen_object", "close_popup", "open_settings")
class TestSettingsScreen(BaseTest):

    settings_screen_object = None  # type: SettingsScreen


    def test_C152079_check_name_settings(self):
        """
        Проверка поля Имя
        :param settings_screen_object: объект класса SettingsScreen
        :return:
        """
        self.settings_screen_object.name_settings()


    def test_C152080_check_signature_settings(self):
        """
        Проверка поля Подпись
        :param settings_screen_object: объект класса SettingsScreen
        :return:
        """
        self.settings_screen_object.signature_settings()


    def test_C152081_turn_notifications_on_and_off(self):
        """
        Включение/выключение уведомлений
        :param settings_screen_object: объект класса SettingsScreen
        :return:
        """
        self.settings_screen_object.check_notification_switcher()


    def test_C152082_check_if_sound_and_vibration_settings_present(self):
        """
        При включенных уведомлениях появляются дополнительные настройки
        :param settings_screen_object: объект класса SettingsScreen
        :return:
        """
        self.settings_screen_object.turn_on_notifications_and_check_elements()


    def test_C152083_check_notification_sounds_settings(self):
        """
        Настройка звука уведомления
        :param settings_screen_object: объект класса SettingsScreen
        :return:
        """
        self.settings_screen_object.check_sound_settings()


    def test_C152084_turn_vibration_on_and_off(self):
        """
        Включение\выключение вибрации
        :param settings_screen_object: объект класса SettingsScreen
        :return:
        """
        self.settings_screen_object.check_vibration_switcher()


    def test_C152664_check_picture_settings(self):
        """
        Работа пункта "Изображения в письме"
        :param settings_screen_object: объект класса SettingsScreen
        :return:
        """
        self.settings_screen_object.check_picture_settings()


    def test_C152668_check_if_cash_present(self):
        """
        На экране "Настройки" присутствует Пункт "Кэш"
        :param settings_screen_object: объект класса SettingsScreen
        :return:
        """
        assert self.settings_screen_object.check_if_cash_present()