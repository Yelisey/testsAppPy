import pytest
from screens.android.new_mail_screen.new_mail_screen import NewMailScreen
from mobileAutoTestsBasicFramework.model.base_test import BaseTest
from screens.android.message_list_screen.message_list_screen import MessageListScreen
from screens.android.utils.screen_initialization_fixtures import message_screen_object
from screens.android.utils.screen_initialization_fixtures import new_mail_screen_object


@pytest.fixture()
def close_popup(message_screen_object:MessageListScreen):
    """
    Фикстура для закрытия popup про обновление приложения до последней версии
    :param message_screen_object: объект класса MessageListScreen
    :return:
    """
    message_screen_object.screen_utility_fixtures.close_popup_fixture()


@pytest.fixture(scope="function")
def check_main_message_list_activity(message_screen_object: MessageListScreen):
    """
    Фикстура для создания предусловий для тестов экрана со списком писем
    :param message_screen: объект класса MessageListScreen
    :return:
    """
    message_screen_object.screen_utility_fixtures.message_list_screen_fixture()


@pytest.mark.usefixtures("message_screen_object", "new_mail_screen_object", "close_popup", "check_main_message_list_activity")
class TestMessageListScreen(BaseTest):

    message_screen_object = None  # type: MessageListScreen
    new_mail_screen_object = None  # type: NewMailScreen


    # TODO Для тестов необходимо сделать отдельную фикстуру с авторизацией через пустой аккаунт
    # def test_C146353_check_empty_list_icon(self):
    #     """
    #     C146353	Присутствие заглушки "Писем нет"
    #     :param message_screen: объект класса MessageListScreen
    #     :return:
    #     """
    #     assert self.message_screen_object.check_empty_list_icon()


    def test_C146639_move_list_of_messages_to_trash(self):
        """
        C146639	Выделить несколько писем и удалить
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        self.message_screen_object.move_messages_to_trash()


    def test_C146640_move_list_of_messages_to_spam(self):
        """
        C146640	Выделить несколько писем и перемещение в спам
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        self.message_screen_object.move_messages_to_spam()


    def test_C146645_move_list_of_messages_to_folder(self):
        """
        C146645	Выделить несколько писем и перемещение в папку
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        self.message_screen_object.move_list_of_messages_to_folder()


    def test_C146644_goto_search_and_back(self):
        """
        C146644	Переход к экрану поиска и обратно
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        assert self.message_screen_object.to_search_and_back()


    def test_C146627_short_swipe_delete(self):
        """
        C146627	Удаление коротким свайпом влево
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        assert self.message_screen_object.del_message_by_short_swipe()


    def test_C146628_long_swipe_delete(self):
        """
        C146628	Удаление длинным свайпом влево
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        assert self.message_screen_object.del_message_by_long_swipe()


    def test_C146633_check_one_message(self):
        """
        C146633	Выделение одного письма долгим тапом
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        assert self.message_screen_object.check_one_message()


    def test_C146634_check_many_message(self):
        """
        C146634	Выделить несколько писем
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        assert self.message_screen_object.check_many_messages()


    def test_C146635_pull_to_refresh(self):
        """
        C146635	Pul-to-refresh
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        self.message_screen_object.pull_to_refresh()


    def test_C146641_uncheck_many_message(self):
        """
        C146641	Снять выделение со всех писем
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        self.message_screen_object.check_many_messages()
        self.message_screen_object.uncheck_messages()


    def test_C146631_go_to_new_mail_form(self):
        """
        C146631	Переход к форме создания письма
        :param new_mail_screen: объект класса NewMailScreen
        :return:
        """
        self.new_mail_screen_object.open_new_mail_form_and_back()


    def test_C146629_change_mail_status_by_short_swipe(self):
        """
        C146629 Смена статуса письма (прочитано\не прочитано) коротким свайпом вправо
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        assert self.message_screen_object.change_mail_status_by_short_swipe()


    def test_C146630_change_mail_status_by_long_swipe(self):
        """
        C146630	Смена статуса письма (прочитано\не прочитано) длинным свайпом вправо
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        self.message_screen_object.change_mail_status_by_long_swipe()


    def test_C146636_mark_mail_as_imortant(self):
        """
        C146636	Отметки письма (пометить как важное)
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        assert self.message_screen_object.mark_mail_as_important()


    def test_C152700_check_inbox_counter(self):
        """
        C152700	Работа счетчика писем на экране "Входящие"
        :param message_screen: объект класса MessageListScreen
        :return:
        """
        assert self.message_screen_object.check_counter_rise()