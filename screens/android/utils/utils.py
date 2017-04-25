from mobileAutoTestsBasicFramework.model.application import Application
from screens.android.utils.email_sender import EmailSender


class Utils(object):


    # логин/пароль для авторизации в доменах Рамблера
    email_data_rambler = "roboapp"
    password_rambler = "9250990390"

    # Email для авторизации в mail.ru
    email_data_mailru = "rambler.mail.tests@mail.ru"

    # Email для авторизации соц.сетей кроме mail.ru (Password подходит всем соц.сетям)
    email_data_soc = "rambler.mail.tests@gmail.com"
    password_soc = "9250990390a"


    # Телефон/Пароль для авторизации в vk/ok
    tel_number = "89851151083"
    password_for_tel = "qweasd12"

    domains_list = ["@rambler.ru", "@lenta.ru", "@autorambler.ru", "@myrambler.ru", "@ro.ru"]
    password = "1234567"
    email = "dev.qa"

    # Список кнопок меню по порядку
    menu_folders_buttons_names = ["Входящие", "Исходящие", "Отправленные", "Черновики", "Корзина", "Спам"]

    address = "roboapp@rambler.ru"
    subject_message ="test"

    name_text = "Test123"
    signature_text = "Test signature"


    def __init__(self, app: Application):
        """
        Конструктор инициализации параметров, необходимых для вспомогательных методов для экранов
        :param app: объект класса Application
        """
        self.app = app
        self.email_sender = EmailSender


    def get_locator(self, table_name, locator_key):
        """
        Обвязка для получения локатора
        :param table_name: название таблицы в базе данных
        :param locator_key: ключ (название элемента)
        :rtype str
        :return: локатор
        """
        return self.app.get_load_db.get_locator(table_name, locator_key)


    def open_screen_with_check(self, locator_button, screen_to_be_opened, scroll_until_element_is_unvisible=False):
        """
        Открытие экрана с проверкой
        :param locator_button: элемент, на который нужно нажать
        :param screen_to_be_opened: экран, который должен открыться/элемент, который должен отображаться после нажатия на locator_button
        :param scroll_until_element_is_unvisible: флаг, которому присваивается значение True, если необходим доскролл до элемента
        :rtype boolean
        :return: True - если элемент виден, False - если нет
        """
        if scroll_until_element_is_unvisible:
            self.app.get_scroll_and_swipe_element_helper.scroll_while_element_is_invisible(locator_button)
        self.app.get_tap_and_press_element_helper.tap(locator_button)
        return self.app.get_find_element_helper.is_visible_element(screen_to_be_opened)


    def open_screen_and_check_with_limit(self, locator_button, locator_toolbar=None, limit=1):
        """
        Общий метод для открытия раздела
        :param locator_button: элемент, на который нужно нажать
        :param locator_toolbar: талбар эарана, который должен открыться после нажатия на locator_button (не обязательный параметр)
        :param limit: лимит для скролла
        :rtype boolean
        :return: True - если элемент виден, False - если нет
        """
        self.app.get_scroll_and_swipe_element_helper.scroll_while_element_is_invisible(locator_button, limit)
        self.app.get_tap_and_press_element_helper.tap(locator_button)
        if locator_toolbar != None:
            self.app.get_wait_element_helper.wait_of_visible(locator_toolbar)
            return self.app.get_find_element_helper.is_visible_element(locator_toolbar)


    def close_welcome_screen(self):
        """
        Закрытие activity "Welcome screen"
        :return:
        """
        self.app.get_wait_element_helper.wait_of_visible(self.get_locator('AuthorizationScreenElements', 'welcome_pager'))
        if self.app.get_find_element_helper.is_visible_element(self.get_locator('AuthorizationScreenElements', 'welcome_pager')):
            self.app.get_tap_and_press_element_helper.tap(self.get_locator('AuthorizationScreenElements', 'welcome_screen_close_button'))


    def close_popup(self):
        """
        Закрытие popup про обновление приложения до последней версии
        :return:
        """
        if self.app.get_find_element_helper.is_visible_element(self.get_locator('AuthorizationScreenElements', 'popup_cancel')):
            self.app.get_tap_and_press_element_helper.tap(self.get_locator('AuthorizationScreenElements', 'popup_cancel'))


    def check_authorization_state_and_log_in(self):
        """
        Проверка статуса авторизации пользователя и авторизация, если пользователь не был авторизован
        """
        if self.app.get_find_element_helper.is_visible_element(
                self.get_locator("AuthorizationScreenElements", "email_field")):
            self.app.get_authorization_helper.auth(
                self.get_locator('AuthorizationScreenElements', 'email_field'),
                self.get_locator('AuthorizationScreenElements', 'password_field'),
                self.get_locator('AuthorizationScreenElements', 'sign_in_button'),
                self.email_data_rambler, self.password_rambler)


    def check_authorization_state_and_log_out(self):
        """
        Проверка авторизован ли пользователь, если да, то выход из аккаунта
        """
        if self.app.get_find_element_helper.is_visible_element(
                self.get_locator('AuthorizationScreenElements', 'main_toolbar')):
            self.app.get_find_element_helper.get_element(self.get_locator('AuthorizationScreenElements',
                                                                               'menu_button'))
            self.app.get_tap_and_press_element_helper.multiple_tap((self.get_locator('AuthorizationScreenElements', 'menu_button')),
                                                               (self.get_locator('SettingsScreen', 'settings_button')))
            self.app.get_tap_and_press_element_helper.scroll_to_element_and_tap(self.get_locator('AuthorizationScreenElements',
                                                                          'logout_button'))
            self.app.get_keyboard_helper.hide_keyboard()


    def check_if_menu_open(self):
        """
        Проверка, открыто ли меню, если нет - открытие меню
        :return:
        """
        self.app.get_value_and_data_helper.check_current_activity("ru.rambler.mail",
                                                                  ".presentation.list.MessageListActivity",
                                                                  ".presentation.login.StartActivity")
        if self.app.get_find_element_helper.is_visible_element(self.get_locator("MainMenuScreen", "menu_layout")):
            if self.app.get_find_element_helper.is_visible_element(
                    self.get_locator("MainMenuScreen", "inbox_folder_button")) == False:
                self.app.get_scroll_and_swipe_element_helper.scroll_to_direction(
                    self.get_locator("MainMenuScreen", "menu_layout"), "up")
        else:
            self.open_side_menu()


    def open_side_menu(self):
        """
        Открытие бокового меню
        :return:
        """
        self.app.get_tap_and_press_element_helper.tap(self.get_locator("MainMenuScreen", "side_menu_button"))
        self.app.get_wait_element_helper.wait_of_visible(self.get_locator("MainMenuScreen", "menu_toolbar"))


    def check_if_mailbox_is_empty_and_fill_it(self, number_of_emails):
        """
        Проверка, пуста ли папка "Входящие" и наполнениее ее письмами, если да
        :param number_of_emails: количество писем, которые нужно отправить
        :return:
        """
        if self.app.get_find_element_helper.is_visible_element(self.get_locator("MessageListScreen", "empty_mailbox")):
            self.email_sender.send_emails(number_of_emails, self.address)
            self.app.get_wait_element_helper.wait_until_element_visible(self.get_locator("MessageListScreen", "email_checkbox"))


    def check_main_message_list_activity_and_open_inbox(self):
        """
        Проверка активити и переход к экрану "Входящие"
        :return:
        """
        self.app.get_value_and_data_helper.check_current_activity("ru.rambler.mail",
                                                                  ".presentation.list.MessageListActivity",
                                                                  ".presentation.login.StartActivity")
        if not self.app.get_find_element_helper.is_visible_element(
                self.get_locator("MainMenuScreen", "inbox_toolbar")):
            self.check_if_menu_open()
            self.app.get_tap_and_press_element_helper.tap(
                self.get_locator("MainMenuScreen", "inbox_folder_button"))


    def open_settings(self):
        """
        Открытие настроек
        :return:
        """
        if self.app.get_find_element_helper.is_visible_element(
                self.get_locator("SettingsScreen", "settings_toolbar")) == False:
            if self.app.get_find_element_helper.is_visible_element(self.get_locator("SettingsScreen",
                                                                                         "menu_layout")):
                if self.app.get_find_element_helper.is_visible_element(
                        self.get_locator("SettingsScreen","inbox_folder_button")) == False:
                    self.app.get_scroll_and_swipe_element_helper.scroll_to_direction(
                        self.get_locator("SettingsScreen","menu_layout"), "up")
            else:
                self.open_screen_with_check(self.get_locator("SettingsScreen", "side_menu_button"),
                                                 self.get_locator("SettingsScreen", "menu_toolbar"))
            self.open_screen_with_check(self.get_locator("SettingsScreen", "settings_button"),
                                             self.get_locator("SettingsScreen", "settings_toolbar"))