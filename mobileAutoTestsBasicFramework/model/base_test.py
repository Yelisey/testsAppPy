from model.application import Application
from model.appium_support import restartAppium
from model.platform_control.appium_control_test import ConfigSupport
from model.init_driver import InitAppiumDriverAndServer
from model.parameter_driver_for_helper import ParameterDriverForHelper

import pytest
import os
import sqlite3


@pytest.mark.usefixtures("setup_test_class")
class BaseTest(object):

    app = None  # type: Application
    __platformName = None
    __platformVersion = None
    __deviceName = None
    __app_name = None
    __udid = None
    __host = None
    __port = None
    appium_driver = None

    @classmethod
    def set_app_name(cls, app_name):
        """
        Определение директории приложения
        :param app_name: директория приложения
        :return:
        """
        cls.__app_name = app_name

    @classmethod
    def get_app_for_cmd(cls):
        """
        Получение директории приложения из командной строки
        :rtype str
        :return: директория приложения
        """
        return cls.__app_name

    # TODO поменять имя метода
    def get_app_for_runner(self, app_name):
        """
        Получение директории приложения для runner'а
        :param app_name:
        :return: директория приложения
        """
        app_directory = os.path.abspath(
            os.path.join(
                os.path.abspath(
                    os.curdir),
                "app"))
        app_name = os.path.join(app_directory, app_name)
        return app_name

    @classmethod
    @pytest.fixture(scope="module", autouse=True)
    def init(self, driver):
        """
        Фикстура инициализации фреймворка
        :param driver: Фикстура инициализации драйвера
        """
        ParameterDriverForHelper.set_driver(driver)

    # фикстура для автоматического запуска appium
    @pytest.fixture(scope="session", autouse=True)
    def appium_start(self):
        """
        Фикстура для запуска Appium server
        :return: запуск Appium server
        """
        restartAppium()

    @pytest.fixture(scope="module")
    def driver(
            self,
            request,
            platformName,
            platformVersion,
            deviceName,
            host, port, udid,
            cmd_mode, app_name):
        """
        Фикстура для инициализации Appium драйвера
        :param request:
        :param platformName: название платформы девайса
        :param platformVersion: версия платформы девайса
        :param deviceName: имя девайса
        :param host: хост (IP устройства, на котором запускаются тесты)
        :param port: порт
        :param udid: UDID девайса (iOS)
        :param cmd_mode: запуск тестов из командной строки
        :param app_name: название приложения
        :rtype selenium.webdriver.remote.webdriver.WebDriver
        :return: Appium driver
        """
        global appium_driver
        if cmd_mode == "True":
            self.config_from_console(
                host, port,
                platformName,
                platformVersion,
                deviceName, udid, app_name)
            appium_driver = InitAppiumDriverAndServer(
                request,
                self.get_host(),
                self.get_port(),
                self.get_platformName(),
                self.get_platformVersion(),
                self.get_deviceName(),
                self.get_udid(),
                self.get_app_for_cmd()).driver()
        else:
            self.tc = ConfigSupport().get_test_control()
            appium_driver = self.tc.get_driver()
        return appium_driver

    # Инициализация конфигурации тестовой
    @pytest.fixture(scope="module")
    def application(self, request):
        """
        Фикстура для инициализации тестовой конфигурации
        :param request:
        :param driver: Appium driver
        :param test_path: директория с тестами
        :rtype class
        :return: объект класса Application
        """
        return Application(request)

    @pytest.fixture(scope='function', autouse=True)
    def take_screenshot(self, request, application: Application):
        """
        Фикстура для снятия скриншота
        :param request:
        :param driver:
        :return:
        """
        application.get_artifacts_helper.take_screen(request)

    @classmethod
    def set_platformName(cls, platformName: str):
        """
        Определение платформы
        :param platformName: название платформы
        :rtype str
        :return: название платформы
        """
        cls.__platformName = platformName

    @classmethod
    def set_platformVersion(cls, platformVersion: str):
        """
        Определение версии платформы
        :param platformVersion: версия платформы
        :rtype str
        :return: версия платформы
        """
        cls.__platformVersion = platformVersion

    @classmethod
    def set_deviceName(cls, deviceName: str):
        """
        Определение имени девайса
        :param deviceName: имя девайса
        :rtype str
        :return: имя девайса
        """
        cls.__deviceName = deviceName

    @classmethod
    def set_udid(cls, udid: str):
        """
        Определение UDID девайса (iOS)
        :param udid: UDID девайса
        :rtype str
        :return: UDID девайса
        """
        cls.__udid = udid

    @classmethod
    def set_host(cls, host: str):
        """
        Определение хоста (IP устройства, на котором запускаются тесты)
        :param host: хост
        :rtype str
        :return: хост
        """
        cls.__host = host

    @classmethod
    def set_port(cls, port: str):
        """
        Определение порта
        :param port: номер порта
        :rtype str
        :return: нормер порта
        """
        cls.__port = port

    @classmethod
    def get_platformName(cls):
        """
        Получние названия платформы
        :rtype str
        :return: название платформы
        """
        return cls.__platformName

    @classmethod
    def get_platformVersion(cls):
        """
        Получение версии платформы
        :rtype str
        :return: версия платформы
        """
        return cls.__platformVersion

    @classmethod
    def get_deviceName(cls):
        """
        Получение имени девайса
        :rtype str
        :return: имя девайса
        """
        return cls.__deviceName

    @classmethod
    def get_udid(cls):
        """
        Получение UDID девайса (iOS)
        :rtype str
        :return: UDID девайса
        """
        return cls.__udid

    @classmethod
    def get_host(cls):
        """
        Полчение хоста (IP устройства, на котором запускаются тесты)
        :rtype str
        :return: хост
        """
        return cls.__host

    @classmethod
    def get_port(cls):
        """
        Получение номера порта
        :rtype str
        :return: номер порта
        """
        return cls.__port

    def config_from_console(
            self,
            host: str,
            port: str,
            platformName: str,
            platformVersion: str,
            deviceName: str, udid, app_name: str):
        """
        :param host: хост (IP устройства, на котором запускаются тесты)
        :param port: номер порта
        :param platformName: название платформы
        :param platformVersion: версия платформы
        :param deviceName: имя девайса
        :param udid: UDID девайса (iOS)
        :param app_name: название приложения
        :return: получение параметров platformName, platformVersion, deviceName, app_name, host, port, udid
        """
        if platformName is not None:
            self.set_platformName(platformName)
        if platformVersion is not None:
            self.set_platformVersion(platformVersion)
        if deviceName is not None:
            self.set_deviceName(deviceName)
        if app_name is not None:
            self.set_app_name(app_name)
        if host is not None:
            self.set_host(host)
        if port is not None:
            self.set_port(port)
        if udid is not None:
            self.set_udid(udid)


    def get_locator(self, table_name, key: str):
        """
        Получение локатора из базы данных
        :param table_name: название таблицы
        :param key: ключ (название элемента)
        :rtype str
        :return: локатор элемента
        """
        data = self.app.get_load_db.dbconn.select_data(table_name, key)
        if data is not None:
            self.app.get_artifacts_helper.log().info(
                "Данные для элемента выбраны из таблицы: '{0}' базы данных".format(table_name))
            return data
        else:
            method = self.app.get_load_db.i_database.set_method(table_name, key)
            value = self.app.get_load_db.i_database.set_value(table_name, key)
            try:
                self.app.get_artifacts_helper.log().info(
                    "Добавляем недостающие данные в таблицу базы данных")
                self.app.get_load_db.dbconn.insert_data(table_name, key, method, value)
                self.app.get_artifacts_helper.log().info(
                    "Данные для элемента помещены в таблицу: '{0}' базы данных".format(table_name))
                return self.app.get_load_db.dbconn.select_data(table_name, key)
            except sqlite3.OperationalError as error:
                self.app.get_artifacts_helper.log().critical(
                    "Получить данные из таблицы не получилось из-за ошибки: '{0}'".format(error))
                assert False
