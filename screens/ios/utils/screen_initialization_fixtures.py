import pytest

from screens.ios.authorization_screen.ios_authorization_screen import AuthorizationScreen
from screens.ios.settings_screen.ios_settings_screen import SettingsScreen
from screens.ios.main_menu_screen.ios_main_menu_screen import MainMenuScreen
from screens.ios.message_list_screen.ios_message_list_screen import MessageListScreen
from screens.ios.new_mail_screen.ios_new_mail_screen import NewMailScreen
from screens.ios.utils.utils import Utils


@pytest.yield_fixture()
def authorization_screen_object(request, application):
    """
    Фикстура инициализации объекта экрана authorization_screen_object

    :param request: Экземпляр класса FixtureRequest
    :param application: Экземпляр класса Application
    """
    if request.cls is not None:
        request.cls.authorization_screen_object = AuthorizationScreen(application)
        yield request.cls.authorization_screen_object
    else:
        yield None

    if request.cls is not None:
        request.cls.authorization_screen_object = None


@pytest.yield_fixture()
def ios_utils(request, application):
    """
    Фикстура инициализации объекта экрана authorization_screen_object

    :param request: Экземпляр класса FixtureRequest
    :param application: Экземпляр класса Application
    """
    if request.cls is not None:
        request.cls.ios_utils = Utils(application)
        yield request.cls.ios_utils
    else:
        yield None

    if request.cls is not None:
        request.cls.ios_utils = None


@pytest.yield_fixture()
def main_menu_screen_object(request, application):
    """
    Фикстура инициализации объекта экрана main_menu_screen_object

    :param request: Экземпляр класса FixtureRequest
    :param application: Экземпляр класса Application
    """
    if request.cls is not None:
        request.cls.main_menu_screen_object = MainMenuScreen(application)
        yield request.cls.main_menu_screen_object
    else:
        yield None

    if request.cls is not None:
        request.cls.main_menu_screen_object = None


@pytest.yield_fixture()
def new_mail_screen_object(request, application):
    """
    Фикстура инициализации объекта экрана main_menu_screen_object

    :param request: Экземпляр класса FixtureRequest
    :param application: Экземпляр класса Application
    """
    if request.cls is not None:
        request.cls.new_mail_screen_object = NewMailScreen(application)
        yield request.cls.new_mail_screen_object
    else:
        yield None

    if request.cls is not None:
        request.cls.new_mail_screen_object = None


@pytest.yield_fixture()
def message_screen_object(request, application):
    """
    Фикстура инициализации объекта экрана message_screen_object

    :param request: Экземпляр класса FixtureRequest
    :param application: Экземпляр класса Application
    """
    if request.cls is not None:
        request.cls.message_screen_object = MessageListScreen(application)
        yield request.cls.message_screen_object
    else:
        yield None

    if request.cls is not None:
        request.cls.message_screen_object = None


@pytest.yield_fixture()
def settings_screen_object(request, application):
    """
    Фикстура инициализации объекта экрана settings_screen_object

    :param request: Экземпляр класса FixtureRequest
    :param application: Экземпляр класса Application
    """
    if request.cls is not None:
        request.cls.settings_screen_object = SettingsScreen(application)
        yield request.cls.settings_screen_object
    else:
        yield None

    if request.cls is not None:
        request.cls.settings_screen_object = None


# @pytest.yield_fixture()
# def tasks_screen_object(request, application):
#     """
#     Фикстура инициализации объекта экрана authorization_screen_elements_object
#
#     :param request: Экземпляр класса FixtureRequest
#     :param application: Экземпляр класса Application
#     """
#     if request.cls is not None:
#         request.cls.tasks_screen = TasksScreen(application)
#         yield request.cls.tasks_screen
#     else:
#         yield None
#
#     if request.cls is not None:
#         request.cls.tasks_screen = None