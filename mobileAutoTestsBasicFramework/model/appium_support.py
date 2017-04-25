import subprocess
import atexit
import os


def startAppium():
    """
    Запуск Appium server'а
    :rtype boolean
    :return: True, если Appium server запущен
    """
    global appiumProcess
    atexit.register(stop_appium)
    appiumProcess = subprocess.Popen(
        ('appium',
         '&'),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid)
    while True:
        line = appiumProcess.stdout.readline()
        if line != '':
            line.strip()
        if "listener started" in str(line):
            return True


def stop_appium():
    """
    Остановка Appium server'а
    :return:
    """
    os.system("ps -A | grep [a]ppium | awk '{print $1}' | xargs kill -9")


def restartAppium():
    """
    Рестарт Appium server'а
    :rtype boolean
    :return: True, если Appium server запущен
    """
    stop_appium()
    startAppium()
