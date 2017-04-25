#coding:utf-8
from mobileAutoTestsBasicFramework.model.application import Application
from mobileAutoTestsBasicFramework.element_helpers.artifacts_helper import get_time
from screens.android.utils.utils import Utils


class NewMailScreen(object):


    def __init__(self, app: Application):
        self.app = app
        self.util = Utils(app)


    def open_new_mail_form(self):
        """
        Открыть форму создания нового письма
        :return:
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("NewMailScreen", "new_mail_button"))
        self.app.get_find_element_helper.is_visible_element(self.util.get_locator("NewMailScreen", "new_mail_toolbar"))


    def close_mail(self):
        """
        Закрытие формы нового письма
        :return:
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("NewMailScreen", "close_mail_button"))


    def set_new_mail_adress(self, to_address):
        """
        Ввести данные в поле "Кому"
        :param to_address: строка с адресом получателя письма
        :return:
        """
        self.app.get_value_and_data_helper.send_data(
            self.util.get_locator("NewMailScreen", "to_new_mail_field"), to_address)
        self.app.get_keyboard_helper.press_keycode(61)


    def set_new_mail_subject(self, subject):
        """
        Ввести данные в поле "Тема"
        :param subject: сгенерированная строка с темой письма
        :return:
        """
        self.app.get_value_and_data_helper.send_data(
            self.util.get_locator("NewMailScreen", "subject_new_mail_field"), subject)


    def push_send_button(self):
        """
        Отправить новое письмо
        :return:
        """
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("NewMailScreen", "new_mail_send_button"))


    def generate_subject(self):
        """
        Сгенерировать строку с темой письма
        :rtype str
        :return: строка с темой письма
        """
        subject_object = self.util.subject_message + "_{0}".format(get_time("%Y-%m-%d %H-%M-%S-%f"))
        return subject_object


    def send_new_mail(self):
        """
        Отправить новое письмо
        :rtype str
        :return: строка с темой отправленного письма
        """
        self.open_new_mail_form()
        self.set_new_mail_adress(self.util.address)
        subject = self.generate_subject()
        self.set_new_mail_subject(subject)
        self.push_send_button()
        new_email = ("xpath", "//android.widget.TextView[@text='{0}']".format(subject))
        self.app.get_wait_element_helper.wait_of_visible(new_email)
        return subject


    def open_new_mail_form_and_back(self):
        """
        Открыть форму нового письма и закрыть ее
        :return:
        """
        self.open_new_mail_form()
        self.app.get_tap_and_press_element_helper.tap(self.util.get_locator("NewMailScreen", "close_mail_button"))