from conftest import root_dir, test_file, test_method, test_path
from element_helpers.tap_and_press_element_helper import TapAndPressElementHelper
from element_helpers.find_element_helper import FindElementHelper
from element_helpers.keyboard_helper import KeyboardHelper
from element_helpers.notification_helper import NotificationHelper
from element_helpers.scroll_and_swipe_element_helper import ScrollAndSwipeElementHelper
from element_helpers.element_text_helper import ElementTextHelper
from element_helpers.authorization_helper import AuthorizationHelper
from element_helpers.value_and_data_element_helper import ValueAndDataElementHelper
from element_helpers.service_function_helper import ServiceFunctionHelper
from element_helpers.wait_element_helper import WaitElementHelper
from model.database_model.database_for_test import DataForTest
from model.database_model.database_connection import DataBaseConnection
from element_helpers.artifacts_helper import ArtifactsHelper


def memorize(func):
    """
    Декоратор отдающий объект, если он уже был проинициализирован
    :param func: функция
    :return:
    """

    def wrapper(self):
        """
        wrapper для получения имени атрибута (func.__name__)
        :param self:
        :return: объект wrapper
        """
        store_attr_name = '_{0}'.format(func.__name__)
        if not hasattr(self, store_attr_name):
            setattr(self, store_attr_name, func(self))
        return getattr(self, store_attr_name)
    return wrapper


class Application(object):

    def __init__(
            self, request):
        """
        Конструктор для инициализации параметров
        :param driver: вебдрайвер
        :param test_path: директория с тестами
        :param request:
        :param test_method:
        :param test_file:
        :param root_dir: путь до корневой директори проекта
        :param log: логирование
        """
        self.test_path = test_path(request)
        self.test_method = test_method(request)
        self.test_file = test_file(request)
        self.root_dir = root_dir()

    @property
    @memorize
    def get_find_element_helper(self):
        """
        Хелпер поиска элементов
        :rtype class
        :return: объект класса FindElementHelper
        """
        return FindElementHelper(self.get_artifacts_helper.log())

    @property
    @memorize
    def get_wait_element_helper(self):
        """
        Хелпер ожидания
        :rtype class
        :return: объект класса WaitElementHelper
        """
        return WaitElementHelper(
            self.get_artifacts_helper.log(),
            self.get_find_element_helper)

    @property
    @memorize
    def get_tap_and_press_element_helper(self):
        """
        Хелпер нажатия на элементы
        :rtype class
        :return: объект класса TapAndPressElementHelper
        """
        return TapAndPressElementHelper(
            self.get_artifacts_helper.log(),
            self.get_wait_element_helper,
            self.get_find_element_helper,
            self.get_scroll_and_swipe_element_helper,
            self.get_service_function_helper)

    @property
    @memorize
    def get_scroll_and_swipe_element_helper(self):
        """
        Хелпер скролла элементов
        :rtype class
        :return: объект класса ScrollAndSwipeElementHelper
        """
        return ScrollAndSwipeElementHelper(
            self.get_artifacts_helper.log(),
            self.get_find_element_helper,
            self.get_wait_element_helper,
            self.get_service_function_helper)

    @property
    @memorize
    def get_value_and_data_helper(self):
        """
        Хелпер для работы со значениями и данными
        :rtype class
        :return: объект класса ValueAndDataElementHelper
        """
        return ValueAndDataElementHelper(
            self.get_artifacts_helper.log(),
            self.get_find_element_helper,
            self.get_tap_and_press_element_helper,
            self.get_keyboard_helper,
            self.get_service_function_helper)

    @property
    @memorize
    def get_keyboard_helper(self):
        """
        Хелпер для работы с клавиатурой
        :rtype class
        :return: объект класса KeyboardHelper
        """
        return KeyboardHelper(self.get_artifacts_helper.log())

    @property
    @memorize
    def get_notification_helper(self):
        """
        Хелпер для обработки уведомлений
        :rtype class
        :return: объект класса NotificationHelper
        """
        return NotificationHelper(
            self.get_artifacts_helper.log(),
            self.get_find_element_helper,
            self.get_tap_and_press_element_helper)

    @property
    @memorize
    def get_service_function_helper(self):
        """
        Хелепер для работы с системными функциями девайса
        :rtype class
        :return: объект класса ServiceFunctionHelper
        """
        return ServiceFunctionHelper(self.get_artifacts_helper.log())

    @property
    @memorize
    def get_element_text_helper(self):
        """
        Хелпер для работы с текстом элементов
        :rtype class
        :return: объект класса ElementTextHelper
        """
        return ElementTextHelper(
            self.get_artifacts_helper.log(),
            self.get_find_element_helper)

    @property
    @memorize
    def get_database_connection(self):
        """
        Хелпер для работы с базой данных
        :rtype class
        :return: объект класса DataBaseConnection
        """
        return DataBaseConnection(self.get_artifacts_helper.log(), self.test_path)

    @property
    @memorize
    def get_load_db(self):
        """
        Получение локаторов для тестов из базы данных
        :rtype class
        :return: объект класса DataForTest
        """
        return DataForTest(self.get_artifacts_helper.log(), self.test_path)

    @property
    @memorize
    def get_artifacts_helper(self):
        """
        Хелпер для работы с артефактами тестов (логи, скриншоты)
        :rtype class
        :return: объект класса ArtifactsHelper
        """
        return ArtifactsHelper(
            self.root_dir,
            self.test_file,
            self.test_method)

    @property
    @memorize
    def get_authorization_helper(self):
        """
        Хелпер для авторизации в приложении
        :rtype class
        :return: объект класса AuthorizationHelper
        """
        return AuthorizationHelper(
            self.get_artifacts_helper.log(),
            self.get_value_and_data_helper,
            self.get_tap_and_press_element_helper,
            self.get_keyboard_helper)
