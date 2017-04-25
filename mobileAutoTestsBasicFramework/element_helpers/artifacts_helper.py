from datetime import datetime
from model.parameter_driver_for_helper import ParameterDriverForHelper

import os
import logging
import uuid


def get_time(time_format):
    """
    Получить текущее время
    :param time_format: Формат вывода времени
    :return str: Текущая дата в указанном формате
    """
    return datetime.now().strftime(time_format)


class ArtifactsHelper(ParameterDriverForHelper):

    def __init__(self, root_dir, test_file, test_name):
        """
        Конструктор для инициализации параметров
        :param root_dir: рутовая директория
        :param test_file: название файла с тестами
        :param test_name: название теста
        """
        super().__init__()
        self.logger = None
        self.root_dir = root_dir
        self.test_file = test_file
        self.test_name = test_name
        self.session_id = str(uuid.uuid4())
        self.path_artifacts_test = self._path_artifacts_test(
            self.root_dir, self.test_name, self.session_id)
        self.log_file = self.path_log_file()

    def _path_artifacts_test(self, root_dir, test_name, session_id):
        """
        Метод для получения пути до артефактов
        :param root_dir: рутовая директория
        :param test_name: название теста
        :param session_id: название сессии
        :return: название директории с артефактами
        :rtype: str
        """
        return os.path.join(
            root_dir,
            "artifacts",
            test_name,
            get_time("%d-%m-%Y %H-%M-%S") +
            " - " +
            session_id)

    def log(self):
        """
        Метод для логирования
        :return logger: Экземпляр класса logger
        """
        if None == self.logger:
            self.logger = logging.getLogger(self.test_name)
            if not self.logger.handlers:
                self.logger.setLevel(logging.DEBUG)
                fh = logging.FileHandler(self.log_file, 'w', 'utf-8')
                fh.setLevel(logging.DEBUG)
                formatter = logging.Formatter('%(asctime)s - %(name)s -  %(module)s - %(levelname)s - %(message)s')
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
        return self.logger

    def path_log_file(self):
        """
        Получение пути файла с логами
        :rtype: str
        :return: путь файла с логами
        """
        log_console_path = os.path.join(self.path_artifacts_test, "log")
        if not os.path.exists(log_console_path):
            os.makedirs(log_console_path)
        date = get_time("%Y-%m-%d %H-%M-%S-%f")
        return os.path.join(log_console_path, date + ".log")


    def path_source_file(self):
        """
        Получение пути файла с xml кодом экрана
        :rtype: str
        :return: путь файла с xml таблицей
        """
        path_source_file = os.path.join(self.path_artifacts_test, "source_xml_code")
        if not os.path.exists(path_source_file):
            os.makedirs(path_source_file)
        date = get_time("%Y-%m-%d %H-%M-%S-%f")
        return os.path.join(path_source_file, date + ".xml")


    def take_screen(self, request):
        """
        Фикстура для получения скриншота
        :param request: Экземпляр класса FixtureRequest
        """
        def fin():
            global screenshot_path
            path = os.path.join(self.path_artifacts_test, 'screen_report')
            if not os.path.exists(path):
                os.makedirs(path)
            ts = get_time('%Y-%m-%d %H-%M-%S')
            from conftest import test_method
            screenshot_name = '{ts} {test_file} {test_method}.png'.format(
                ts=ts, test_file=self.test_file, test_method=test_method(request))
            if request.node.rep_setup.failed or request.node.rep_call.failed:
                path_failed = os.path.join(path, 'failed')
                if not os.path.exists(path_failed):
                    os.mkdir(path_failed)
                screenshot_path = os.path.join(path_failed, screenshot_name)
            elif request.node.rep_setup.passed or request.node.rep_call.passed:
                path_passed = os.path.join(path, 'passed')
                if not os.path.exists(path_passed):
                    os.mkdir(path_passed)
                screenshot_path = os.path.join(path_passed, screenshot_name)
            self.driver.get_screenshot_as_file(screenshot_path)
        request.addfinalizer(fin)


    def get_page_source(self):
        """
        Получить исходных код экрана в виде xml
        :return:
        """
        with open(self.path_source_file(), 'w') as file_:
            file_.write(self.driver.page_source)
