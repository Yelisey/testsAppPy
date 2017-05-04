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
        self.test_status = None
        self.test_name = None

    def set_test_info(self, new_status=None, new_name=None):
        self.test_status = new_status
        self.test_name = new_name


test_info = TestInfo()


def get_test_info():
    return test_info


def pytest_addoption(parser):
    parser.addoption(
        "--host",
        action="store",
        default="127.0.0.1",
        required=False,
        help="host for Appium server")
    parser.addoption(
        "--port",
        action="store",
        default="4723",
        required=False,
        help="port for Appium server")
    parser.addoption(
        "--platformName",
        action="store",
        default="Android",
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
        default="yelissey.oshlokov",
        required=False,
        help="name of device")
    parser.addoption(
        "--app_name",
        action="store",
        default=PATH('app/trololo.apk'),
        required=False,
        help="name of map. Example for cmd_mode: PATH('app/trololo.apk')"
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
    parser.addoption('--test_environment', action="store",
                     help="Test Environment")
    parser.addoption('--environment_configuration', action="store",
                     help="Environment Configuration")

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
    return request.config.getoption('--host')


@pytest.fixture(scope='session')
def port(request):
    return request.config.getoption('--port')


@pytest.fixture(scope='session')
def platformName(request):
    return request.config.getoption('--platformName')


@pytest.fixture(scope='session')
def platformVersion(request):
    return request.config.getoption('--platformVersion')


@pytest.fixture(scope='session')
def deviceName(request):
    return request.config.getoption('--deviceName')


@pytest.fixture(scope='session')
def udid(request):
    return request.config.getoption('--device_udid')


@pytest.fixture(scope='session')
def bundle_id(request):
    return request.config.getoption('--bundle_id')


@pytest.fixture(scope='session')
def app_package(request):
    return request.config.getoption('--app_package')


@pytest.fixture(scope='session')
def app_activity(request):
    return request.config.getoption('--app_activity')


@pytest.fixture(scope='session')
def app_name(request):
    return request.config.getoption('--app_name')


@pytest.fixture(scope='session')
def cmd_mode(request):
    return request.config.getoption('--cmd_mode')


# фикстура для определения имени метода
@pytest.fixture(scope="module")
def test_method(request):
    return request.node.name


# фикстура для определения имени файла с тестом
@pytest.fixture(scope="module")
def test_file(request):
    return request.fspath.basename.split('.py')[0]


# фикстура для определения директории, где хранятся тесты
@pytest.fixture(scope="module")
def test_path(request):
    return request.fspath.dirname


# фикстура путь до корневой дериктории
@pytest.fixture(scope="session")
def root_dir():
    return os.path.dirname(__file__)


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    """
    Создание отчетов
    :param item:
    :param call:
    :param __multicall__:
    :return:
    """
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def test_status(request):
    test_name = request.node.nodeid.split('::')[-1]

    def fin():
        if request.node.rep_setup.failed:
            test_info.set_test_info('failed_setup', test_name)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                test_info.set_test_info('failed_run', test_name)
    request.addfinalizer(fin)
    test_info.set_test_info('passed', test_name)

