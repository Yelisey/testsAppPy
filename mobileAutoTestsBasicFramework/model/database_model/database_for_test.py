from model.database_model.database_connection import DataBaseConnection
from model.database_model.database_interface import DataBaseInterface

import logging


class DataForTest(object):

    def __init__(self, log: logging.Logger, test_path: str):
        """
        Конструктор для инициализации параметров
        :param log: логирование
        :param test_path: директория тестов
        :param i_database: добавление метода и значения для локатора
        :param dbconn: методы для работы с базой данных (зсоздание таблицы, запись, удаление и получение данных)
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        self.test_path = test_path
        self.i_database = DataBaseInterface()
        self.dbconn = DataBaseConnection(log, test_path)
