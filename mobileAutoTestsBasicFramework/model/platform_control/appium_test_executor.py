import os
import pytest


class AppiumTestExecution(object):

    def __init__(self, test_support, test_timestamp):
        """
        Конструктор для инициализации параметров
        :param test_support: параметр-связка для обработки параметров запуска тестов
        :param test_timestamp: отметка времени теста
        :param result_folder: директория папки с тестовыми артефактами
        """
        self.test_support = test_support
        environment_class = self.test_support.get_module('device_environment')
        self.environment = environment_class(test_support)
        self.result_folder = os.path.join(
            self.test_support.project_root, 'results', test_timestamp)

    def get_test_result_prefix(self, config_section):
        """
        Префикс результатов теста
        :param config_section:
        :rtype str
        :return:
        """
        return ''

    def run_tests(self):
        """
        Проверка кода запуска теста
        :rtype int
        :return: код запуска теста
        """
        test_status = 0
        for config_section in self.test_support.env_config.sections():
            tmp_test_status = self.trigger_pytest(config_section)
            if tmp_test_status != 0:
                test_status = tmp_test_status
        return test_status

    def trigger_pytest(self, config_section):
        """ Запуск автотестов на разных конфигурациях
        Функция запуска pytest.main() с созданными агрументами заранее
        :param str config_section: секция в platform_control/environment.properties конфигурационном файле
        :rtype function
        :return: result pytest.main()
        """

        test_result_prefix = self.get_test_result_prefix(config_section)
        junit_xml_path = os.path.join(
            self.result_folder, config_section + '.xml')
        # TODO: необходимо в будущем, при необходимости расковырять html-репорты
        # html_path = os.path.join(self.result_folder, config_section + '.html')
        pytest_arguments_dict = {
            '--test_platform=': '--test_platform={0}'.format(self.test_support.test_platform),
            '--device_environment=': '--device_environment={0}'.format(self.test_support.device_environment),
            '--device_configuration=': '--device_configuration={0}'.format(config_section),
            '--junitxml=': '--junitxml={0}'.format(junit_xml_path),
            '--junit-prefix=': '--junit-prefix={0}'.format(test_result_prefix),
            # TODO: необходимо в будущем, при необходимости расковырять html-репорты
            # '--html=': '--html=' + html_path,
            # '--html-prefix=': '--html-prefix=' + test_result_prefix,
            '--instafail': '--instafail',
        }

        extra_pytest_arguments = self.environment.get_pytest_arguments(
            config_section)
        if extra_pytest_arguments:
            pytest_arguments_dict.update(extra_pytest_arguments)

        test_directory = self.test_support.get_opt('test_directory')
        if not test_directory:
            raise ValueError('Директория с тестами не найдена!')

        pytest_arguments = [
            os.path.join(self.test_support.project_root, test_directory),
        ]
        pytest_arguments.extend(pytest_arguments_dict.values())
        parallel_tests = int(self.test_support.get_opt('parallel_tests'))
        if parallel_tests > 1:
            pytest_arguments.extend(['-n', str(parallel_tests)])
        smoke = self.test_support.get_opt('smoke')
        if smoke:
            pytest_arguments.extend(['-m', 'smoke'])
        regress = self.test_support.get_opt('regress')
        if regress:
            pytest_arguments.extend((['-r', 'regress']))

        return pytest.main(pytest_arguments)
