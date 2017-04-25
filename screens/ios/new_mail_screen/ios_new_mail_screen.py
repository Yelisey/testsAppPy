#coding:utf-8

from mobileAutoTestsBasicFramework.model.application import Application
from mobileAutoTestsBasicFramework.element_helpers.artifacts_helper import get_time
from screens.ios.utils.utils import Utils


class NewMailScreen(object):

    def __init__(self, app: Application):
        """
        Конструктор для инициализации параметров

        :param app: объект класса Application
        """
        self.app = app
        self.util = Utils(app)


    def set_to_address(self, field, to_addres):
        self.app.get_value_and_data_helper.send_data(field, to_addres)
        address_locator = ("xpath", "//XCUIElementTypeStaticText[@value='{0}']".format(to_addres))
        if self.app.get_find_element_helper.is_visible_element(address_locator):
            self.app.get_tap_and_press_element_helper.tap(address_locator)


    def set_subject(self, field):
        global subject
        subject = self.generate_subject()
        self.app.get_value_and_data_helper.tap_and_send_value_at_same_locator(field, subject)


    def generate_subject(self):
        """
        Сгенерировать строку с темой письма
        :rtype str
        :return: строка с темой письма
        """
        generated_subject = self.util.subject_message + "_{0}".format(get_time("%Y-%m-%d %H-%M-%S-%f"))
        return generated_subject


    def send_email(self, send_button, inbox_screen_title):
        self.util.open_screen_with_check(send_button, inbox_screen_title)


    def check_email_is_recieved(self):
        new_email = ("accessibility_id", subject)
        self.app.get_wait_element_helper.wait_of_visible(new_email)