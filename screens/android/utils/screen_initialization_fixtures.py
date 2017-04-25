import pytest

from screens.android.authorization_screen_elements_check.authorization_screen_elements_check import AuthorizationScreenElements
from screens.android.authorization_screen.authorization_screen import AuthorizationScreen
from screens.android.main_menu_screen.main_menu_screen import MainMenuScreen
from screens.android.message_list_screen.message_list_screen import MessageListScreen
from screens.android.new_mail_screen.new_mail_screen import NewMailScreen
from screens.android.settings_screen.settings_screen import SettingsScreen


@pytest.yield_fixture()
def authorization_screen_elements_object(request, application):
    """
    Фикстура инициализации объекта экрана authorization_screen_elements_object

    :param request: Экземпляр класса FixtureRequest
    :param application: Экземпляр класса Application
    """
    if request.cls is not None:
        request.cls.authorization_screen_elements_object = AuthorizationScreenElements(application)
        yield request.cls.authorization_screen_elements_object
    else:
        yield None

    if request.cls is not None:
        request.cls.authorization_screen_elements_object = None


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