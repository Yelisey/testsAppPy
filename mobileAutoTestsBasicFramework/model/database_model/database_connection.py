import os
import sqlite3
import logging


class DataBaseConnection(object):

    __config_name = "database_for_test"

    def __init__(self, log: logging.Logger, test_path):
        """
        Конструктор для инициализации параметров
        :param log: логирование
        :param test_path: директория тестов
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        self.test_path = test_path


    def __check_table_exists(self, table_name: str, conn):
        """
        Проверка существования таблицы
        :param table_name: название таблицы
        :param conn: соединение
        :rtype boolean
        :return: True - таблица существует, False - не существует
        """
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT name FROM sqlite_master WHERE type='table' AND name =? ''',
            (table_name,
             ))
        if cursor.rowcount > 0:
            return True
        cursor.close()
        return False

    def __get_database_connection(self, table_name: str):
        """
        Установить соединение с базой данных
        :param table_name: название таблицы
        :rtype connection
        :return: соединение с базой данных
        """
        database_path = os.path.join(
            os.path.dirname(
                self.test_path),
            "DB_for_test")
        if not os.path.exists(database_path):
            os.makedirs(database_path)
        try:
            config_file = os.path.join(database_path, self.__config_name + ".db")
            conn = sqlite3.connect(config_file)
            if self.__check_table_exists(table_name, conn):
                self.log.info(
                    "Таблица: '{0}' уже есть в базе данных".format(table_name))
            else:
                self.__create_table(table_name, conn)
            return conn
        except sqlite3.OperationalError as error:
            self.log.critical(
                "Не удалось создать базу данных из-за ошибки: '{0}'".format(error))
            assert False

    def __create_table(self, table_name: str, conn):
        """
        Создание таблицы в базе данных
        :param table_name: название таблицы
        :param conn: соединение с базой данных
        :rtype boolean
        :return: True, если таблица создалась, и False - если нет
        """
        try:
            self.log.info(
                "Создаем таблицу '{0}' в базе данных".format(table_name))
            cursor = conn.cursor()
            cursor.execute(
                '''CREATE TABLE '{0}' (key PRIMARY KEY, method, value)'''.format(table_name))
            conn.commit()
            return True
        except sqlite3.OperationalError as error:
            self.log.critical(
                "Не удалось создать таблицу в базе данных из-за ошибки '{0}'".format(error))
            return False

    def insert_data(self, table_name, key: str, method, value: str):
        """
        Вставить данные в таблицу
        :param table_name: название таблицы
        :param key: ключ (название элемента)
        :param method: метод для поиска локатора
        :param value: значение локатора
        :return:
        """
        try:
            conn = self.__get_database_connection(table_name)
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO '{0}' VALUES (?, ?, ?)'''.format(
                table_name), (key, method, value))
            conn.commit()
        except sqlite3.OperationalError as error:
            self.log.critical(
                "Вставить данные в таблицу базы данных не получилось из-за ошибки: '{0}'".format(error))
            assert False

    def update_data(self, table_name, key: str, value: str):
        """
        Обновление данных в таблице
        :param table_name: название таблицы
        :param key: ключ (название элемента)
        :param value: значение локатора
        :return:
        """
        try:
            conn = self.__get_database_connection(table_name)
            cursor = conn.cursor()
            cursor.execute(
                '''UPDATE '{0}' SET value = ? WHERE key= ?'''.format(table_name), (value, key))
            conn.commit()
        except sqlite3.OperationalError as error:
            self.log.critical(
                "Обновить данные в таблице не получилось из-за ошибки: '{0}'".format(error))
            assert False

    def delete_data(self, table_name, key: str):
        """
        Удаление данных из таблицы
        :param table_name: название таблицы
        :param key: ключ (название элемента)
        :return:
        """
        try:
            conn = self.__get_database_connection(table_name)
            cursor = conn.cursor()
            t = (key,)
            cursor.execute(
                '''DELETE FROM '{0}' WHERE key =?'''.format(table_name), t)
            conn.commit()
        except sqlite3.OperationalError as error:
            self.log.critical(
                "Удалить запись из базы данных не получилось из-за ошибки: '{0}'".format(error))
            assert False

    def select_data(self, table_name, key: str):
        """
        Получение данных из таблицы
        :param table_name: название таблицы
        :param key: ключ (название элемента)
        :rtype string object
        :return: значения из таблицы
        """
        try:
            conn = self.__get_database_connection(table_name)
            cursor = conn.cursor()
            t = (key,)
            for row in cursor.execute(
                    '''SELECT method, value from '{0}' WHERE key =?'''.format(table_name), t):
                return row
        except sqlite3.OperationalError as error:
            self.log.critical(
                "Получить данные из таблицы не получилось из-за ошибки: '{0}'".format(error))
            assert False
