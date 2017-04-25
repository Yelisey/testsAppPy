import pytest
import os


@pytest.yield_fixture()
def setup_test_class(request, application, driver):
   """
   Фикстура инициализирующая переменные app и web_driver в классе BaseTest,
   для последующего их использования в тестах
   :param request:  Экземпляр класса FixtureRequest
   :param application: фикстура инициализирующая менеджер хелперов
   :param driver: фикстура инициализирующая driver
   """
   if request.cls is not None:
       request.cls.app = application
       request.cls.appium_driver = driver
   yield None
   if request.cls is not None:
       request.cls.app = None
       request.cls.appium_driver = None


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestInfo():

    def __init__(self):
        """
        Конструктор для инициализации параметров
        :param test_status: текущий статус теста
        :param test_name: название теста
        """
        self.test_status = None
        self.test_name = None

    def set_test_info(self, new_status=None, new_name=None):
        """
        Определение информации о тесте
        :param new_status: обновленный статус теста
        :param new_name: новое название теста
        :return:
        """
        self.test_status = new_status
        self.test_name = new_name


test_info = TestInfo()


def get_test_info():
    """
    Получение информации о тесте (текущий статус, название)
    :return: информация о тесте (текущий статус, название)
    """
    return test_info


def pytest_addoption(parser):
    """
    Обработка параметров для командной строки
    :param parser: парсер аргументов для командной строки
    :return:
    """
    parser.addoption(
        "--host",
        action="store",
        default=None,
        required=False,
        help="host for Appium server")
    parser.addoption(
        "--port",
        action="store",
        default=None,
        required=False,
        help="port for Appium server")
    parser.addoption(
        "--platformName",
        action="store",
        default=None,
        required=False,
        help="platformName of device")
    parser.addoption(
        "--platformVersion",
        action="store",
        default=None,
        required=False,
        help="platformVersion of device")
    parser.addoption(
        "--deviceName",
        action="store",
        default=None,
        required=False,
        help="name of device")
    parser.addoption(
        "--app_name",
        action="store",
        default=None,
        required=False,
        help="name of map. Example for cmd_mode: Path('app/app_name.apk')"
             "Example for runner: app_name.apk")
    parser.addoption("--autoAcceptAlerts", action="store", default=True,
                     help="Auto accepts alerts on iOS devices")

    # Configuration
    parser.addoption(
        "--cmd_mode",
        action="store",
        required=False,
        help="cmd mode for run tests")
    parser.addoption('--test_platform', action="store",
                     help="Test Platform")
    parser.addoption('--device_environment', action="store",
                     help="Device Environment")
    parser.addoption('--device_configuration', action="store",
                     help="Device Configuration")

    # Android
    parser.addoption(
        "--app_package",
        action="store",
        default=None,
        required=False,
        help="package of application (for Android)")
    parser.addoption(
        "--app_activity",
        action="store",
        default=None,
        required=False,
        help="appActivity of application (for Android)")

    # iOS
    parser.addoption(
        "--device_udid",
        action="store",
        required=False,
        help="udid of device (for iOS)")
    parser.addoption(
        "--bundle_id",
        action="store",
        default=None,
        required=False,
        help="bundleId of application (for iOS)")


@pytest.fixture(scope='session')
def host(request):
    """
    Фикстура для получения хоста (IP устройства, на котором запускаются тесты) для командной строки
    :param request:
    :return: хост (IP устройства, на котором запускаются тесты)
    """
    return request.config.getoption('--host')


@pytest.fixture(scope='session')
def port(request):
    """
    Фикстура для получения номер порта для командной строки
    :param request:
    :return: номер порта
    """
    return request.config.getoption('--port')


@pytest.fixture(scope='session')
def platformName(request):
    """
    Фикстура для получения названия платформы девайса для командной строки
    :param request:
    :return: платформа девайса
    """
    return request.config.getoption('--platformName')


@pytest.fixture(scope='session')
def platformVersion(request):
    """
    Фикстура для получения версии платформы девайса для командной строки
    :param request:
    :return: версия платформы девайса
    """
    return request.config.getoption('--platformVersion')


@pytest.fixture(scope='session')
def deviceName(request):
    """
    Фикстура для получения имени девайса для командной строки
    :param request:
    :return: имя девайса
    """
    return request.config.getoption('--deviceName')


@pytest.fixture(scope='session')
def udid(request):
    """
    Фикстура для получения UDID девайса (iOS) для командной строки
    :param request:
    :return: UDID девайса (iOS)
    """
    return request.config.getoption('--device_udid')


@pytest.fixture(scope='session')
def bundle_id(request):
    """
    Фикстура для получения bundle_id приложения (iOS) для командной строки
    :param request:
    :return: bundle_id приложения (iOS)
    """
    return request.config.getoption('--bundle_id')


@pytest.fixture(scope='session')
def app_package(request):
    """
    Фикстура для получения названия пакета приложения (Android) для командной строки
    :param request:
    :return: название пакета приложения (Android)
    """
    return request.config.getoption('--app_package')


@pytest.fixture(scope='session')
def app_activity(request):
    """
    Фикстура для получения названия activity приложения (Android) для командной строки
    :param request:
    :return: название activity приложения (Android)
    """
    return request.config.getoption('--app_activity')


@pytest.fixture(scope='session')
def app_name(request):
    """
    Фикстура для получения пути до приложения для командной строки
    :param request:
    :return: путь до приложения
    """
    return request.config.getoption('--app_name')


@pytest.fixture(scope='session')
def cmd_mode(request):
    """
    Фикстура для запуска тестов из командной строки
    :param request:
    :return: если True, - тесты запускаются из командной строки
    """
    return request.config.getoption('--cmd_mode')


@pytest.fixture(scope="module")
def test_method(request):
    """
    Фикстура для определения имени метода
    :param request:
    :return: имя метода
    """
    return request.node.name


@pytest.fixture(scope="module")
def test_file(request):
    """
    Фикстура для определения имени файла с тестом
    :param request:
    :return: имя файла с тестом
    """
    return request.fspath.basename.split('.py')[0]


@pytest.fixture(scope="module")
def test_path(request):
    """
    Фикстура для определения директории, где хранятся тесты
    :param request:
    :return: директория с тестами
    """
    return request.fspath.dirname


@pytest.fixture(scope="session")
def root_dir():
    """
    Фикстура для получения корневой дириктории
    :return: корневая директория
    """
    return os.path.dirname(__file__)


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    """
    Создание отчетов
    :param item:
    :param call:
    :param __multicall__:
    :return: отчет
    """
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def test_status(request):
    """
    Проверка текущего статуса теста (passed/failed)
    :param request:
    :return:
    """
    test_name = request.node.nodeid.split('::')[-1]

    def fin():
        if request.node.rep_setup.failed:
            test_info.set_test_info('failed_setup', test_name)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                test_info.set_test_info('failed_run', test_name)
    request.addfinalizer(fin)
    test_info.set_test_info('passed', test_name)
