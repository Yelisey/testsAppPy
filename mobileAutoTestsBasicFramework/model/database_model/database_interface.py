class DataBaseInterface(object):

    def set_method(self, table_name: str, key: str):
        """
        Запись метода для поиска локатора в таблицу
        :param table_name: название таблицы
        :param key: ключ (название элемента)
        :rtype str
        :return: метод для поиска локатора
        """
        print("Нужно ввести метод для поиска нового локатора (id/xpath...) !!!")
        global method
        while True:
            for cmd in [
                'Quit - Закрыть и не добавлять данные',
                    'YES - Добавить данные']:
                print('  %s - %s' % (cmd[:1], cmd))
            cmd = input("Пожалуйста, введите команду (Q/Y) ").upper()[:1]
            if cmd == 'Q':
                break
            elif cmd == 'Y':
                method = input(
                    " Введите тип локатора (id/xpath...) для таблицы '{0}' базы данных и локатора '{1}'". format(
                        table_name, key))
                break
            else:
                print("Вы не выбрали правильный вариант команды!!!")
        return method

    def set_value(self, table_name: str, key: str):
        """
        Запись значения локатора в таблицу
        :param table_name: название таблицы
        :param key: ключ (название элемента)
        :rtype str
        :return: значение локатора
        """
        print("На этом этапе вам нужно ввести value для вашего нового локатора!!!")
        global value
        while True:
            for cmd in [
                'Quit - Закрыть и не добавлять данные',
                    'YES - Добавить данные']:
                print('  %s - %s' % (cmd[:1], cmd))
            cmd = input("Пожалуйста, введите команду (Q/Y) ").upper()[:1]
            if cmd == 'Q':
                break
            elif cmd == 'Y':
                value = input(
                    " Введите value для локатора для таблицы '{0}' базы данных и локатора '{1}'". format(
                        table_name, key))
                break
            else:
                print("Вы не выбрали правильный вариант команды!!!")
        return value
