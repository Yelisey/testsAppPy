from mobileAutoTestsBasicFramework.model.application import Application
from screens.android.utils.email_sender import EmailSender


class Utils(object):


    # логин/пароль для авторизации в доменах Рамблера
    email_rambler = "roboapp"
    password_rambler = "9250990390"

    # Email для авторизации соц.сетей кроме mail.ru (Password подходит всем соц.сетям)
    email_for_social_net = "rambler.mail.tests@gmail.com"
    password_for_social_net = "9250990390a"

    # Телефон/Пароль для авторизации в vk/ok
    tel_number = "89851151083"
    password_for_tel = "qweasd12"

    password = "1234567"
    email = "dev.qa"

    address = "roboapp@rambler.ru"
    subject_message = "test"


    def __init__(self, app: Application):
        """
        Конструктор инициализации параметров, необходимых для вспомогательных методов для экранов
        :param app: объект класса Application
        """
        self.app = app
        self.email_sender = EmailSender


    def test_check_if_autorized_and_log_in(self, login_field,
                                           password_field,
                                           sign_in_button,
                                           email,
                                           password,
                                           welcome_screen_locator,
                                           menu_button):
        """
        Проверка, авторизован ли пользователь и выход из аккаунта, если да
        :param login_field: поле лоя ввода логина
        :param password_field: поле для ввода пароля
        :param sign_in_button: кнопка "Войти"
        :param email: данные для логина
        :param password: данные для пароля
        :param welcome_screen_locator: локатор для элемента экрана приветствия
        :param inbox_screen_title: заголовок экрана "Входящие"
        :param menu_button: кнопка для открытия главного меню
        :return:
        """
        is_inbox_screen_title_visible = self.app.get_find_element_helper.is_visible_element(menu_button)
        if is_inbox_screen_title_visible is False:
            self.app.get_authorization_helper.auth(login_field,
                                                   password_field,
                                                   sign_in_button,
                                                   email,
                                                   password)
            self.close_welcome_screen(welcome_screen_locator)
            self.app.get_wait_element_helper.wait_of_visible(menu_button)
            assert self.app.get_find_element_helper.is_visible_element(menu_button)


    def open_screen_with_check(self, locator_button, screen_to_be_opened, scroll=False):
        """
        Открытие экрана с проверкой
        :param locator_button: элемент, на который нужно нажать
        :param screen_to_be_opened: экран, который должен открыться/элемент, который должен отображаться после нажатия на locator_button
        :param scroll: флаг для скролла вниз
        :return:
        """
        if scroll:
            self.app.get_scroll_and_swipe_element_helper.scroll_to_direction()
        self.app.get_tap_and_press_element_helper.tap(locator_button)
        self.app.get_wait_element_helper.wait_of_visible(screen_to_be_opened)
        assert self.app.get_find_element_helper.is_visible_element(screen_to_be_opened)


    def open_side_menu(self, menu_button, menu_screen_title):
        """
        Открытие бокового меню
        :return:
        """
        is_menu_open = self.app.get_find_element_helper.is_visible_element(menu_screen_title)
        if is_menu_open is False:
            self.open_screen_with_check(menu_button, menu_screen_title)


    def check_if_mailbox_is_empty_and_fill_it(self, empty_mailbox_placeholder, number_of_emails, email_cell):
        """
        Проверка, пуста ли папка "Входящие" и наполнениее ее письмами, если да
        :param empty_mailbox_placeholder: плэйсхолдер пустого экрана "Входящие"
        :param number_of_emails: количество писем, которые нужно отправить
        :param email_cell: локатор ячейки письма, чтобы убедиться, что хотя бы одно письмо пришло
        :return:
        """
        if self.app.get_find_element_helper.is_visible_element(empty_mailbox_placeholder):
            self.email_sender.send_emails(number_of_emails, self.address)
            self.app.get_wait_element_helper.wait_until_element_visible(email_cell)


    def open_settings(self, settings_button, settings_screen_title):
        """
        Открытие настроек
        :return:
        """
        self.open_screen_with_check(settings_button, settings_screen_title)


    def logout(self, menu_button, menu_screen_title, settings_button, settings_screen_title,log_out_button, login_field):
        """
        Выход из аккаунта почты
        :param menu_button: кнопка для открытия главного меню
        :param menu_screen_title: заголовок экрана меню
        :param settings_button: кнопка для открытия настроек
        :param settings_screen_title: заголовок экрана настроек
        :param log_out_button: кнопка "Выйти"
        :param login_field: поле для логина на экране авторизации
        :return:
        """
        self.open_side_menu(menu_button, menu_screen_title)
        self.open_settings(settings_button, settings_screen_title)
        self.app.get_scroll_and_swipe_element_helper.scroll_to_direction()
        self.open_screen_with_check(log_out_button, login_field)


    def close_welcome_screen(self, welcome_screen_locator):
        """
        Закрытие экрана с приветствием
        :param welcome_screen_locator: локатор для экрана приветствия
        :return:
        """
        self.app.get_wait_element_helper.wait_of_visible(welcome_screen_locator)
        is_welcome_screen_visible = self.app.get_find_element_helper.is_visible_element(welcome_screen_locator)
        if is_welcome_screen_visible == True:
            for i in range(0, 2):
                self.app.get_tap_and_press_element_helper.tap(welcome_screen_locator)
