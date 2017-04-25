from model.parameter_driver_for_helper import ParameterDriverForHelper
from time import sleep

import os
import logging


class ServiceFunctionHelper(ParameterDriverForHelper):

    def __init__(self, log: logging.Logger):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log

    def clear_app_data(self, package: str):
        """
        Очистить данные приложения

        :param package: Название пакета приложения
        :return:
        """
        command = "adb shell pm clear {0}".format(package)
        os.popen(command).read()

    def force_stop_app(self, package: str):
        """
        Принудительная остановка приложения приложения

        :param package: Название пакета приложения
        :return:
        """
        command = "adb shell am force-stop {0}".format(package)
        os.popen(command).read()

    def reboot_device(self):
        """
        Перезагрузка девайса

        :return:
        """
        deviceName = os.popen("adb devices").read()
        command = "adb reboot"
        os.popen(command)
        i = 0
        while True:
            result = os.popen("adb devices").read()
            if deviceName == result:
                sleep(5)
                break
            else:
                i += 1
                sleep(1)

    def pull_down_status_bar(self):
        """
        Открыть статус бар на устройстве

        :return:
        """
        os.popen("adb shell service call statusbar 1").read()

    def get_android_version(self):
        """
        Получить версию андроида

        :return: Версия андроида
        """
        detailAndroidVersion = os.popen(
            "adb shell getprop ro.build.version.release ").read()
        androidVersion = detailAndroidVersion[0:3]
        return androidVersion

    def grant_permission(self, package_name: str, permission_name: str):
        """
        Пример задания пермишена - android.permission.CHANGE_CONFIGURATION

        :param package_name: Название пакета приложения
        :param permission_name: Название пермишшена
        :return True:
        """
        command = "adb shell pm grant {0} {1}".format(
            package_name, permission_name)
        os.popen(command).read()
        while True:
            result = os.popen(command).read()
            if result == '':
                return True
        else:
            raise RuntimeError(
                "При выдаче прав {0} произошла ошибка!!".format(permission_name))

    def setOrientation(self, mode='PORTRAIT'):
        """
        Задать ориентацию экрану (по умолчанию - портретная ориентация)

        :param mode: Установка параметра отображения экрана PORTRAIT, LANDSCAPE
        :return:
        """
        if mode == 'PORTRAIT':
            self.log.info("Устанавливаем портретную ориентацию экрана")
            self.driver.orientation = 'PORTRAIT'
            self.log.info("Портретная ориентация экрана установлена")
        else:
            self.log.info("Устанавливаем ландшафтную ориентацию экрана")
            self.driver.orientation = 'LANDSCAPE'
            self.log.info("Ландшафтная ориентация экрана установлена")

    def enableFlightMode(self):
        """
        Задать режим работы с сетью - "В самолете"

        :return: Режим работы с сетью "самолет" задан
        """
        self.driver.mobile.set_network_connection(
            self.driver.mobile.AIRPLANE_MODE)
        self.driver.implicitly_wait(5)
        if self.driver.network_connection == 1:
            self.log.info("Включаем режим в самолете")
        else:
            self.log.info("Режим в самолете не включился!!!")

    def enableWifiMode(self):
        """
        Задать режим работы с сетью - "Wi-Fi"

        :return: Режим работы "Wi-Fi" с сетью задан
        """
        self.driver.mobile.set_network_connection(
            self.driver.mobile.WIFI_NETWORK)
        self.driver.implicitly_wait(5)
        if self.driver.network_connection == 2:
            self.log.info("Включаем режим wi-fi")
        else:
            self.log.info("Режим wi-fi не включился!!!")

    def enableDataMode(self):
        """
        Задать режим работы с сетью - "Data"

        :return: Режим работы с сетью "Data" задан
        """
        self.driver.mobile.set_network_connection(
            self.driver.mobile.DATA_NETWORK)
        self.driver.implicitly_wait(5)
        if self.driver.network_connection == 4:
            self.log.info("Включаем режим data")
        else:
            self.log.info("Режим data не включился!!!")

    def enableData_WifiMode(self):
        """
        Задать режим работы с сетью - "Data + Wifi"

        :return: Режим работы с сетью "Data + Wifi" задан
        """
        self.driver.mobile.set_network_connection(
            self.driver.mobile.ALL_NETWORK)
        self.driver.implicitly_wait(5)
        if self.driver.network_connection == 6:
            self.log.info("Включаем режим wi-fi + data")
        else:
            self.log.info("Режим wi-fi + data не включился!!!")

    def check_wifi(self):
        """
        Проверить текущее подключение к wi-fi

        :return True: Wi-fi Соединение включено
        """
        wi_fi_connection = self.enableWifiMode()
        if wi_fi_connection:
            self.log.info("Wi-Fi включен")
        else:
            self.log.info("Wi-fi невозможно включить. Проблемы с сетью!!!")

    def get_device_capabilities(self, capability: str):
        """
        Вернуть свойство девайса
        :param capability: свойство девайса, которое нужно получить (platformName, deviceName и т. д.)
        :rtype str
        :return: capability
        """
        return self.driver.desired_capabilities[capability]
