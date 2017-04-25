#coding:utf-8
from mobileAutoTestsBasicFramework.model.application import Application
from screens.android.new_mail_screen.new_mail_screen import NewMailScreen
from screens.android.main_menu_screen.main_menu_screen import MainMenuScreen
from screens.android.authorization_screen.authorization_screen import AuthorizationScreen
from screens.android.utils.utils import Utils
from screens.android.utils.screen_utility_fixtures import ScreenUtilityFixtures


class MessageListScreen(object):


    def __init__(self, app: Application):
        """
        Конструктор инициализации параметров, необходимых для методов описания экрана со списком писем
        :param app: экземпляр класса Application
        :param new_mail_screen: объект класса NewMailScreen
        :param main_menu_screen: объект класса MainMenuScreen
        :param auth_screen: обект класса AuthorizationScreen
        :param util: объект класса Utils
        """
        self.app = app
        self.new_mail_screen = NewMailScreen(app)
        self.main_menu_screen = MainMenuScreen(app)
        self.auth_screen = AuthorizationScreen(app)
        self.util = Utils(app)
        self.screen_utility_fixtures = ScreenUtilityFixtures(app)


    def check_empty_list_icon(self):
        """
        Проверка наличия плэйсхолдера в пустой папке
        :rtype str
        :return: локатор изображения (empty_image) и текста (empty_text) плэйсхолддера для пустой папки
        """
        empty_image = self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MessageListScreen", "empty_list_image"))
        empty_text = self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MessageListScreen", "empty_list_text"))
        return empty_image and empty_text


    def open_search_and_check(self):
        """
        Открытие формы поиска
        :rtype boolean
        :return: True - есть форма поиска видна, False - если нет
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MessageListScreen", "search_button"))
        return self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MessageListScreen", "search_form"))


    def back_from_search(self):
        """
        Закрытие формы поиска
        :rtype boolean
        :return: True - есть форма поиска не видна, False - если видна
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MessageListScreen", "back_from_search_button"))
        return not self.app.get_find_element_helper.is_visible_element(
            self.util.get_locator("MessageListScreen", "search_form"))


    def to_search_and_back(self):
        """
        Перейти на форму поиска и обратно
        :rtype function
        :return: back_from_search()
        """
        self.open_search_and_check()
        return self.back_from_search()


    def pull_to_refresh(self):
        """
        Действие pull-to-refresh
        :return:
        """
        self.app.get_scroll_and_swipe_element_helper.pull_to_refresh()


    def check_mail_important(self, subject):
        """
        Поиск отметки "Важное" на определенном письме
        :param subject: строка с темой конкретного письма
        :rtype boolean
        :return: True - если пометка "Важное" видна, False - если не видна
        """
        important_mail_icon = ("xpath", "//android.widget.TextView[@text='{0}']/../..//android.widget.ImageView".
                               format(subject))
        return self.app.get_find_element_helper.is_visible_element(important_mail_icon)


    def mark_mail_as_important(self):
        """
        Пометить письмо как важное
        :rtype function
        :return: self.check_mail_important(subject)
        """
        subject = self.new_mail_screen.send_new_mail()
        self.app.get_tap_and_press_element_helper.tap(self.generate_mail_locator_by_subject(subject))
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MessageListScreen", "star_button"))
        self.new_mail_screen.close_mail()
        return self.check_mail_important(subject)


    def del_message_by_short_swipe(self):
        """
        Удаление письма коротким свайпом
        :rtype boolean
        :return: True - если письмо видно, False - если нет
        """
        subject = self.get_all_subjects_text()[0]
        self.app.get_scroll_and_swipe_element_helper.swipe_element(
            self.util.get_locator("MessageListScreen", "swipe_box"),"left", 1000, 100)
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MessageListScreen", "del_swipe_button"))
        return self.app.get_find_element_helper.is_visible_element(self.generate_mail_locator_by_subject(subject))


    def del_message_by_long_swipe(self):
        """
        Удаление письма длинным свайпом
        :rtype boolean
        :return: True - если письмо видно, False - если нет
        """
        subject = self.get_all_subjects_text()[0]
        self.app.get_scroll_and_swipe_element_helper.swipe_element(
            self.util.get_locator("MessageListScreen", "swipe_box"),"left", 3000, 500)
        return self.app.get_find_element_helper.is_visible_element(self.generate_mail_locator_by_subject(subject))


    def change_mail_status_by_short_swipe(self):
        """
        Смена статуса письма коротким свайпом
        :rtype
        :return:
        """
        subject = self.new_mail_screen.send_new_mail()
        new_email = ("xpath", "//android.widget.TextView[@text='{0}']".format(subject))
        self.app.get_wait_element_helper.wait_of_visible(new_email)
        self.app.get_scroll_and_swipe_element_helper.swipe_element(
            self.util.get_locator("MessageListScreen", "swipe_box"), "right", 1000, 100)
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MessageListScreen", "not_read_email_button"))
        self.app.get_scroll_and_swipe_element_helper.swipe_element(
            self.util.get_locator("MessageListScreen", "swipe_box"), "right", 1000, 100)
        return self.app.get_find_element_helper.is_visible_element(self.util.get_locator("MessageListScreen", "read_email_button"))



    def change_mail_status_by_long_swipe(self):
        """
        Смена статуса письма длинным свайпом
        :rtype
        :return
        """
        self.new_mail_screen.send_new_mail()
        self.app.get_scroll_and_swipe_element_helper.swipe_element(
            self.util.get_locator("MessageListScreen", "swipe_box"), "right", 3000, 510)
        self.app.get_scroll_and_swipe_element_helper.swipe_element(
            self.util.get_locator("MessageListScreen", "swipe_box"), "right", 1000, 100)
        return self.app.get_find_element_helper.is_visible_element(self.util.get_locator("MessageListScreen", "read_email_button"))

    def check_one_message(self):
        """
        Выделение одного письма долгим тапом
        :rtype boolean
        :return: True - если письмо выбрано, False - если нет
        """
        self.app.get_tap_and_press_element_helper.long_press(self.util.get_locator("MessageListScreen", "check_box"))
        self.app.get_find_element_helper.is_visible_element(self.util.get_locator("MessageListScreen",
                                                                                  "checked_mail_icon"))
        return self.app.get_find_element_helper.is_visible_element(('android', 'text("Выбрано 1")'))


    def check_many_messages(self):
        """
        Выделение нескольких писем
        :rtype boolean
        :return: True - если письма выбраны, False - если нет
        """
        if self.app.get_find_element_helper.is_visible_element(
                self.util.get_locator("MessageListScreen", "uncheck_messages_button")):
            self.uncheck_messages()
        messages_list = self.app.get_find_element_helper.get_elements(
            self.util.get_locator("MessageListScreen", "check_box"))
        self.app.get_tap_and_press_element_helper.select_elements_and_long_press_on_first(messages_list)
        self.app.get_find_element_helper.is_visible_element(self.util.get_locator("MessageListScreen",
                                                                                  "checked_mail_icon"))
        return self.app.get_find_element_helper.is_visible_element(('android', 'text("Выбрано {0}")'.
                                                                    format(len(messages_list))))


    def uncheck_messages(self):
        """
        Снять выделение со всех писем
        :return:
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MessageListScreen", "uncheck_messages_button"))


    def move_messages(self, target_button):
        """
        Перемещение писем в заданую папку
        :param target_button:
        :rtype function
        :return: self.is_messages_present_in_folder(subjects) с инвертированным результатом
        """
        self.util.check_if_mailbox_is_empty_and_fill_it(5)
        subjects = self.get_all_subjects_text()
        self.check_many_messages()
        if target_button==self.util.get_locator("MessageListScreen", "del_button") \
                or target_button==self.util.get_locator("MessageListScreen", "spam_button"):
            self.app.get_tap_and_press_element_helper.tap(target_button)
            return subjects
        else:
            self.app.get_tap_and_press_element_helper.tap(
                self.util.get_locator("NewMailScreen", "new_mail_button"))
            self.app.get_wait_element_helper.wait_of_visible(target_button)
            self.app.get_tap_and_press_element_helper.tap(target_button)
            return not self.is_messages_present_in_folder(subjects)


    def move_list_of_messages_to_folder(self):
        """
        Перемещение писем в заданную папку (вспомогательный метод)
        :return:
        """
        self.move_messages(self.util.get_locator("MessageListScreen", "folder_for_move"))


    def move_messages_to_trash(self):
        """
        Перемещение писем в корзину
        :rtype function
        :return: is_messages_present_in_folder(subjects)
        """
        self.clean_folder()
        subjects = self.move_messages(self.util.get_locator("MessageListScreen", "del_button"))
        self.util.check_if_menu_open()
        self.main_menu_screen.open_recycle_bin_folder()
        result = self.is_messages_present_in_folder(subjects)
        self.return_to_inbox()
        return result


    def move_messages_to_spam(self):
        """
        Перемещение писем в спам
        :rtype function
        :return: is_messages_present_in_folder(subjects)
        """
        self.clean_folder()
        subjects = self.move_messages(self.util.get_locator("MessageListScreen", "spam_button"))
        self.util.check_if_menu_open()
        self.main_menu_screen.open_spam_folder()
        result = self.is_messages_present_in_folder(subjects)
        self.return_to_inbox()
        return result


    def get_all_subjects_elements(self):
        """
        Получить все элементы "тема письма" на странице
        :rtype str
        :return: локатор всех "тем письма" all_subjects_elements_locator
        """
        self.app.get_wait_element_helper.wait_of_visible(
            self.util.get_locator("MessageListScreen", "all_subjects_elements_locator"))
        all_subjects_elemets = self.app.get_find_element_helper.get_elements(
            self.util.get_locator("MessageListScreen", "all_subjects_elements_locator"))
        return all_subjects_elemets


    def get_all_subjects_text(self):
        """
        Получить тексты всех тем писем на экране
        :rtype list
        :return: массив со всеми текстами в темах писем на экране
        """
        all_subjects_elemets = self.get_all_subjects_elements()
        all_subjects_text =[]
        for elem in all_subjects_elemets:
            all_subjects_text.append(elem.text)
        return all_subjects_text


    def generate_mail_locator_by_subject(self, subject):
        """
        Генерация локатора целевого письма по теме
        :param subject: строка с темой конкретного письма
        :rtype str
        :return: локатор конкретного письма
        """
        target_mail_locator = ("xpath", "//android.widget.TextView[@text='{0}']".format(subject))
        return target_mail_locator


    def is_messages_present_in_folder(self, target_subjects):
        """
        Проверка присутствия списка определенных писем на странице
        :param target_subjects: тексты тем всех писем на экране
        :rtype boolean
        :return: True - если все темы совпадают, False - если нет
        """
        current_subjects = self.get_all_subjects_text()
        flag = True
        for i in range(len(current_subjects)):
            if not current_subjects[i]==target_subjects[i]:
                flag = False
        return flag


    def check_current_counter_value(self):
        """
        Проверка текущего статуса счетчика писем
        :rtype int
        :return: число писем в папке
        """
        inbox_toolbar = self.app.get_find_element_helper.get_element(
            self.util.get_locator("MessageListScreen", "inbox_toolbar")).text
        current_value = int(inbox_toolbar[8:len(inbox_toolbar)])
        return current_value


    def check_counter_rise(self):
        """
        Проверка изменения счетчика входящих
        :rtype boolean
        :return: True - если количество писем до отправки нового письма +1 равно текущему, False - если нет
        """
        start_value = self.check_current_counter_value()
        self.new_mail_screen.send_new_mail()
        final_value = self.check_current_counter_value()
        return (start_value+1) == final_value


    def clean_folder(self):
        """
        Проверка заполненности и очистка папок спам и корзина(служебный метод для тестов)
        :return:
        """
        self.util.open_side_menu()
        if self.app.get_find_element_helper.is_visible_element(
                self.util.get_locator("MessageListScreen", "clear_button")):
            clear_buttons = self.app.get_find_element_helper.get_elements(
                self.util.get_locator("MessageListScreen", "clear_button"))
            for button in clear_buttons:
                self.util.check_if_menu_open()
                button.click()
                if self.app.get_find_element_helper.is_visible_element(
                        self.util.get_locator("MessageListScreen", "confirm_clear")):
                    self.app.get_tap_and_press_element_helper.tap(
                        self.util.get_locator("MessageListScreen", "confirm_clear"))
        else:
            self.return_to_inbox()


    def return_to_inbox(self):
        """
        Возврат в папку "Входящие"
        :return:
        """
        self.util.check_if_menu_open()
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("MainMenuScreen", "inbox_folder_button"))