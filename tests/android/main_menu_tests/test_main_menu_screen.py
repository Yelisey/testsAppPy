import pytest

from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.android.main_menu_screen.main_menu_screen import MainMenuScreen
from screens.android.utils.screen_initialization_fixtures import main_menu_screen_object


@pytest.fixture()
def close_popup(main_menu_screen_object: MainMenuScreen):
    """
    Фикстура для закрытия popup про обновление приложения до последней версии
    :param main_menu_screen_object: объект класса MainMenuScreen
    :return:
    """
    main_menu_screen_object.screen_utility_fixtures.close_popup_fixture()


@pytest.fixture(scope="function")
def check_if_menu_open(main_menu_screen_object: MainMenuScreen):
    """
    Фикстура для создания предусловий для тестов главного меню
    :param main_menu_screen_object: объект класса MainMenuScreen
    :return:
    """
    main_menu_screen_object.screen_utility_fixtures.main_menu_screen_fixture()


@pytest.mark.usefixtures("main_menu_screen_object", "close_popup", "check_if_menu_open")
class TestMainMenuScreen(BaseTest):

    main_menu_screen_object = None  # type: MainMenuScreen


    def test_C146088_settings_button_present(self):
        """
        Проверка наличия кнопки "Настройки"
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.check_if_settings_button_visible()


    def test_C146087_check_order(self):
        """
        Проверка наличия и корректности расположения стандартных папок в меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        self.main_menu_screen_object.check_menu_buttons_order()


    def test_C146090_if_tasks_button_visible(self):
        """
        Проверка наличия пункта "Задачи"
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.check_if_tasks_folder_button_visible()


    def test_C146095_if_review_button_present(self):
        """
        Проверка наличия пункта "Отправить отзыв"
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.check_if_send_feedback_menu_button_visible()


    def test_C146096_if_other_apps_present(self):
        """
        Проверка наличия пункта "Другие приложения"
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.check_if_other_apps_menu_header_visible()


    def test_C152701_check_inbox_email_counter(self):
        """
        Работа счетчика писем папки "Входящие" в меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.inbox_counter_check()


    def test_C146098_open_settings(self):
        """
        Переход в настройки из меню и возврат
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        self.main_menu_screen_object.open_settings_and_go_back_to_inbox()


    def test_C146100_open_inbox_folder(self):
        """
        Переход к экрану "Входящие" из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.open_inbox_folder()


    def test_C146101_open_outbox_folder(self):
        """
        Переход к экрану "Исходящие" из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.open_outbox_folder()


    def test_C146102_open_sent_folder(self):
        """
        Переход к экрану "Отправленные" из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.open_sent_folder()


    def test_C146103_open_drafts_folder(self):
        """
        Переход к экрану "Черновики" из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.open_drafts_folder()


    def test_C146104_open_recycle_bin_folder(self):
        """
        Переход к экрану "Корзина" из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.open_recycle_bin_folder()


    def test_C146105_open_spam_folder(self):
        """
        Переход к экрану "Спам" из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        assert self.main_menu_screen_object.open_spam_folder()



    # TODO Временно закомментировала, так как нужно придумать способ закрывать тьюториал скрины
    # def test_C146322_open_tasks_folder(self):
    #     """
    #     Переход к экрану "Задачи" из меню
    #     :param main_menu_screen_object: объект класса MainMenuScreen
    #     :return:
    #     """
    #     assert self.main_menu_screen_object.open_tasks_folder()


    def test_C146323_open_add_mailbox_section(self):
        """
        Переход к экрану "Добавить ящик" из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        self.main_menu_screen_object.open_add_mailbox_section()


    def test_C146324_open_send_feedback_screen(self):
        """
        Переход к экрану "Отзыв" из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        self.main_menu_screen_object.open_send_feedback_form()


    def test_C146326_hide_show_other_apps_in_menu(self):
        """
        Переход к приложению из списка "Другие приложения"
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        self.main_menu_screen_object.hide_show_other_apps_in_menu()


    def test_C146356_empty_recycle_bin_folder(self):
        """
        Очистка Корзины из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        self.main_menu_screen_object.remove_emails_from_recycle_bin()


    def test_C146357_empty_spam_folder(self):
        """
        Очистка Спама из меню
        :param main_menu_screen_object: объект класса MainMenuScreen
        :return:
        """
        self.main_menu_screen_object.remove_emails_from_spam_folder()