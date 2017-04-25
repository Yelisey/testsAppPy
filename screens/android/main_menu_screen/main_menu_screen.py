#coding:utf-8
from mobileAutoTestsBasicFramework.model.application import Application
from screens.android.authorization_screen.authorization_screen import AuthorizationScreen
from screens.android.new_mail_screen.new_mail_screen import NewMailScreen
from screens.android.utils.utils import Utils
from screens.android.utils.screen_utility_fixtures import ScreenUtilityFixtures


class MainMenuScreen(object):


    def __init__(self, app: Application):
        """
        Конструктор инициализации параметров, необходимых для методов описания главного меню
        :param app: объект класса Application
        :param auth_screen: обеъкт класса AuthorizationScreen
        :param new_mail_screen: объект класса NewMailScreen
        :param util: объект класса Utils
        """
        self.app = app
        self.auth_screen = AuthorizationScreen(app)
        self.new_mail_screen = NewMailScreen(app)
        self.util = Utils(app)
        self.screen_utility_fixtures = ScreenUtilityFixtures(app)


    def remove_emails_from_folder(self, locator_folder, locator_toolbar, locator_move_emails_to_folder_button,
                                  locator_empty_folder_button, remove_confirmation_popup=None, locator_yes_button=None,
                                  recycle=False):
        """
        Общий метод для удаления писем из папок
        :param locator_folder: локатор для папки, которую нужно очистить
        :param locator_toolbar: локатор тулбара папки, которую нужно очитить
        :param locator_move_emails_to_folder_button: локатор кнопки перемещения писем в папку, которую нужно очистить
        :param locator_empty_folder_button: локатор кнопки Очистить
        :param remove_confirmation_popup: локатор диалогового окна с подтверждением очистки папки
        :param locator_yes_button: локатор кнопки "Да" в диалоговом окне
        :param recycle: флаг, которому присваивается True, если нужно производить действия с диалоговым окном
        :return:
        """
        self.open_inbox_folder()
        self.util.check_if_mailbox_is_empty_and_fill_it(5)
        elements = self.app.get_find_element_helper.get_elements(self.util.get_locator("MainMenuScreen", "email_list"))
        self.app.get_tap_and_press_element_helper.select_elements_and_long_press_on_first(elements)
        self.app.get_tap_and_press_element_helper.tap(locator_move_emails_to_folder_button)
        self.util.open_side_menu()
        self.util.open_screen_and_check_with_limit(locator_folder, locator_toolbar)
        assert self.check_if_emails_present_in_folder()
        self.util.open_side_menu()
        self.app.get_tap_and_press_element_helper.tap(locator_empty_folder_button)
        if recycle:
            assert self.app.get_find_element_helper.is_visible_element(remove_confirmation_popup)
            self.app.get_tap_and_press_element_helper.tap(locator_yes_button)
        self.util.open_screen_and_check_with_limit(locator_folder, locator_toolbar)
        assert self.check_if_folder_is_empty()
        self.util.open_side_menu()
        self.app.get_find_element_helper.is_visible_element(locator_empty_folder_button)


    # TODO Доделать для эмулятора (определение названия приложения в браузере)
    def hide_show_other_apps_in_menu(self):
        """
        Переход к странице приложения Рамблер/новости
        :return:
        """
        self.app.get_scroll_and_swipe_element_helper.scroll_while_element_is_invisible(
            self.util.get_locator("MainMenuScreen", "other_apps_menu_header"))
        self.util.open_screen_and_check_with_limit(self.util.get_locator("MainMenuScreen", "more_apps_menu_button"))
        self.util.open_screen_and_check_with_limit(self.util.get_locator("MainMenuScreen", "rambler_news_menu_button"))
        self.app.get_wait_element_helper.wait_of_visible(
            self.util.get_locator("MainMenuScreen", "rambler_news_in_store"))
        assert self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MainMenuScreen", "rambler_news_in_store"))
        self.app.get_keyboard_helper.android_back()
        self.util.open_screen_and_check_with_limit(self.util.get_locator("MainMenuScreen",
                                                                         "hide_other_apps_menu_button"))


    def check_if_settings_button_visible(self):
        """
        Проверка наличия кнопки настроек
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        return self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MainMenuScreen", "settings_button"))


    def check_menu_buttons_order(self):
        """
        Проверка порядка кнопок в меню
        :return:
        """
        self.app.get_element_text_helper.compare_element_text(
            self.util.get_locator("MainMenuScreen", "all_menu_folders_buttons"),self.util.menu_folders_buttons_names)


    def check_if_tasks_folder_button_visible(self):
        """
        Проверка наличия папки "Задачи"
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        self.app.get_scroll_and_swipe_element_helper.scroll_while_element_is_invisible(
            self.util.get_locator("MainMenuScreen", "tasks_folder_button"), 1)
        return self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MainMenuScreen", "tasks_folder_button"))


    def check_if_send_feedback_menu_button_visible(self):
        """
        Проверка наличия кнопки "Отправить отзыв"
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        self.app.get_scroll_and_swipe_element_helper.scroll_while_element_is_invisible(
            self.util.get_locator("MainMenuScreen", "send_feedback_menu_button"))
        return self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MainMenuScreen", "send_feedback_menu_button"))


    def check_if_other_apps_menu_header_visible(self):
        """
        Проверка наличия заголовка "Другие приложения"
        :rtype boolean
        :return: True - если есть, False - если нет
        """
        self.app.get_scroll_and_swipe_element_helper.scroll_while_element_is_invisible(
            self.util.get_locator("MainMenuScreen", "other_apps_menu_header"))
        return self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MainMenuScreen", "other_apps_menu_header"))


    def open_settings_and_go_back_to_inbox(self):
        """
        Открытие настроек и возврат к папке "Входящие"
        :return:
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MainMenuScreen", "settings_button"))
        assert self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MainMenuScreen", "settings_toolbar"))
        self.util.open_screen_and_check_with_limit(self.util.get_locator("MainMenuScreen", "back_from_settings"),
                             self.util.get_locator("MainMenuScreen", "inbox_toolbar"))


    def open_inbox_folder(self):
        """
        Открытие папки "Входящие"
        :rtype boolean
        :return: True - если открылась нужная папка, False - если нет
        """
        return self.util.open_screen_and_check_with_limit(self.util.get_locator("MainMenuScreen", "inbox_folder_button"),
                                    self.util.get_locator("MainMenuScreen", "inbox_toolbar"))


    def open_outbox_folder(self):
        """
        Открытие папки "Исходящие"
        :rtype boolean
        :return: True - если открылась нужная папка, False - если нет
        """
        return self.util.open_screen_and_check_with_limit(
            self.util.get_locator("MainMenuScreen", "outbox_folder_button"),
            self.util.get_locator("MainMenuScreen", "outbox_toolbar"))


    def open_sent_folder(self):
        """
        Открытие папки "Отправленные"
        :rtype boolean
        :return: True - если открылась нужная папка, False - если нет
        """
        return self.util.open_screen_and_check_with_limit(
            self.util.get_locator("MainMenuScreen", "sent_folder_button"),
            self.util.get_locator("MainMenuScreen", "sent_toolbar"))


    def open_drafts_folder(self):
        """
        Открытие папки "Черновики"
        :rtype boolean
        :return: True - если открылась нужная папка, False - если нет
        """
        return self.util.open_screen_and_check_with_limit(
            self.util.get_locator("MainMenuScreen", "drafts_folder_button"),
            self.util.get_locator("MainMenuScreen", "drafts_toolbar"))


    def open_recycle_bin_folder(self):
        """
        Открытие папки "Корзина"
        :rtype boolean
        :return: True - если открылась нужная папка, False - если нет
        """
        return self.util.open_screen_and_check_with_limit(
            self.util.get_locator("MainMenuScreen", "recycle_bin_folder_button"),
            self.util.get_locator("MainMenuScreen", "recycle_bin_toolbar"))


    def open_spam_folder(self):
        """
        Открытие папки "Спам"
        :rtype boolean
        :return: True - если открылась нужная папка, False - если нет
        """
        return self.util.open_screen_and_check_with_limit(
            self.util.get_locator("MainMenuScreen", "spam_folder_button"),
            self.util.get_locator("MainMenuScreen", "spam_toolbar"))


    def open_tasks_folder(self):
        """
        Открытие папки "Задачи"
        :rtype boolean
        :return: True - если открылась нужная папка, False - если нет
        """
        return self.util.open_screen_and_check_with_limit(
            self.util.get_locator("MainMenuScreen", "tasks_folder_button"),
            self.util.get_locator("MainMenuScreen", "tasks_toolbar"))


    def open_add_mailbox_section(self):
        """
        Открытие раздела "Добавить ящик"
        :return:
        """
        assert self.util.open_screen_and_check_with_limit(
            self.util.get_locator("MainMenuScreen", "add_mailbox_menu_button"),
            self.util.get_locator("MainMenuScreen", "add_mailbox_toolbar"))
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MainMenuScreen", "back_from_add_mailbox_button"))


    def open_send_feedback_form(self):
        """
        Открытие формы отправки отзыва
        :return:
        """
        assert self.util.open_screen_and_check_with_limit(
            self.util.get_locator("MainMenuScreen", "send_feedback_menu_button"),
            self.util.get_locator("MainMenuScreen", "review_toolbar"))
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MainMenuScreen", "close_email_form_button"))


    def check_if_emails_present_in_folder(self):
        """
        Проверка наличия писем в папке
        :rtype boolean
        :return: True - если письма присутствуют в папке, False - если нет
        """
        return self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MainMenuScreen", "email_list"))


    def check_if_folder_is_empty(self):
        """
        Проверка наличия placeholder пустой папки
        :rtype boolean
        :return: True - если плэйсхолдер виден, False - если нет
        """
        return self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MainMenuScreen", "empty_folder_placeholder"))


    def remove_emails_from_recycle_bin(self):
        """
        Удаление писем из папки "Корзина"
        :return:
        """
        self.remove_emails_from_folder(self.util.get_locator("MainMenuScreen", "recycle_bin_folder_button"),
                                       self.util.get_locator("MainMenuScreen", "recycle_bin_toolbar"),
                                       self.util.get_locator("MainMenuScreen", "move_to_bin_button"),
                                       self.util.get_locator("MainMenuScreen", "empty_recycle_bin_button"),
                                       self.util.get_locator("MainMenuScreen", "remove_confirmation"),
                                       self.util.get_locator("MainMenuScreen", "yes_button"), True)


    def remove_emails_from_spam_folder(self):
        """
        Удаление писем из папки "Спам"
        :return:
        """
        self.remove_emails_from_folder(self.util.get_locator("MainMenuScreen", "spam_folder_button"),
                                       self.util.get_locator("MainMenuScreen", "spam_toolbar"),
                                       self.util.get_locator("MainMenuScreen", "move_to_spam_button"),
                                       self.util.get_locator("MainMenuScreen", "empty_spam_folder_button"))


    def inbox_counter_check(self):
        """
        Проверка счетчика писем у папки "Входящие"
        :rtype boolean
        :return: True - количество писем совпадает с ожидаемым, False - не совпадает
        """
        initial_email_number = self.app.get_element_text_helper.get_element_text(
            self.util.get_locator("MainMenuScreen", "inbox_counter"))
        self.open_inbox_folder()
        subject = self.new_mail_screen.send_new_mail()
        email_locator = ('xpath', "//*[@text='{0}']".format(subject))
        self.app.get_wait_element_helper.wait_of_visible(email_locator)
        self.util.open_side_menu()
        current_email_number = self.app.get_element_text_helper.get_element_text(
            self.util.get_locator("MainMenuScreen", "inbox_counter"))
        self.app.get_value_and_data_helper.compare_elements(int(current_email_number), int(initial_email_number) + 1)
        self.open_inbox_folder()
        self.app.get_tap_and_press_element_helper.tap(email_locator)
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MainMenuScreen", "close_email_form_button"))
        self.util.open_side_menu()
        final_email_number = self.app.get_element_text_helper.get_element_text(
            self.util.get_locator("MainMenuScreen", "inbox_counter"))
        return self.app.get_value_and_data_helper.compare_elements(int(initial_email_number), int(final_email_number))