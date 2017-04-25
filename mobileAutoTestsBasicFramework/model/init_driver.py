from appium import webdriver


class InitAppiumDriverAndServer(object):

    def __init__(
        self,
        request, host, port,
        platformName,
        platformVersion,
            deviceName, udid, app):
        """
        Конструктор для инициализации параметров
        :param request:
        :param host: хост (IP устройства, на котором запускаются тесты)
        :param port: номер порта
        :param platformName: название платформы девайса
        :param platformVersion: версия платформы девайса
        :param deviceName: имя девайса
        :param udid: UDID девайса(iOS)
        :param app: директория до приложения
        """
        self.request = request
        self.host = host
        self.port = port
        self.platformName = platformName
        self.platformVersion = platformVersion
        self.deviceName = deviceName
        self.udid = udid
        self.app = app

    def driver(self):
        """
        Запуск Appium driver
        :rtype selenium.webdriver.remote.webdriver.WebDriver
        :return: Appium driver
        """
        desired_capabilities = {}
        desired_capabilities.update({"platformName": self.platformName})
        if self.platformName == 'iOS':
            desired_capabilities.update({
                'automationName': 'XCUITest',
                'usePrebuiltWDA': True,
                'realDeviceLogger': '/usr/local/lib/node_modules/deviceconsole/deviceconsole',
                'xcodeConfigFile': '/usr/local/lib/node_modules/appium-xcuitest-driver/WebDriverAgent/Configurations/ProjectSettings.xcconfig',
                'udid': self.udid,
                'iosInstallPause': '8000',
            })
        desired_capabilities.update({
            'platformVersion': self.platformVersion,
            'deviceName': self.deviceName,
            'app': self.app
        })
        driver = webdriver.Remote(
            command_executor='http://{0}:{1}/wd/hub'.format(self.host, self.port),
            desired_capabilities=desired_capabilities)
        self.request.addfinalizer(driver.quit)
        return driver
