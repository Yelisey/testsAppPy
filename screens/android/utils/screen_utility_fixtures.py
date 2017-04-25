from mobileAutoTestsBasicFramework.model.application import Application
from screens.android.utils.utils import Utils


class ScreenUtilityFixtures(object):


    def __init__(self, app: Application):
        """
        Конструктор инициализации параметров
        :param app: объект класса Application
        """
        self.app = app
        self.util = Utils(app)


    def authorization_elements_screen_fixture(self):
        """
        Вызов метода для фикстуры, обеспечивающей предусловия для тестов элементов экрана авторизации
        :return:
        """
        self.util.check_authorization_state_and_log_out()


    def authorization_screen_fixture(self):
        """
        Вызов методов для фикстуры, обеспечивающей предусловия для тестов экрана авторизации
        :return:
        """
        self.util.check_authorization_state_and_log_out()
        self.util.close_welcome_screen()


    def main_menu_screen_fixture(self):
        """
        Вызов методов для фикстуры, обеспечивающей предусловия для тестов главного меню
        :return:
        """
        self.util.check_authorization_state_and_log_in()
        self.util.close_welcome_screen()
        self.util.check_if_menu_open()


    def message_list_screen_fixture(self):
        """
        Вызов методов для фикстуры, обеспечивающей предусловия для тестов экрана со списком писем
        :return:
        """
        self.util.check_authorization_state_and_log_in()
        self.util.close_welcome_screen()
        self.util.check_main_message_list_activity_and_open_inbox()


    def settings_screen_fixture(self):
        """
        Вызов методов для фикстуры, обеспечивающей предусловия для тестов экрана настроек
        :return:
        """
        self.util.check_authorization_state_and_log_in()
        self.util.close_welcome_screen()
        self.util.open_settings()


    def close_popup_fixture(self):
        """
        Вызов метода для фикстуры закрытия системного popup про обновление приложения до последней версии
        :return:
        """
        self.util.close_popup()