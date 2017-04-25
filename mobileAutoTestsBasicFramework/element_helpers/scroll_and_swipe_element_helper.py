from element_helpers.find_element_helper import FindElementHelper
from element_helpers.wait_element_helper import WaitElementHelper
from element_helpers.service_function_helper import ServiceFunctionHelper
from selenium.common.exceptions import NoSuchElementException as error
from model.parameter_driver_for_helper import ParameterDriverForHelper
from time import sleep

import logging


class ScrollAndSwipeElementHelper(ParameterDriverForHelper):

    def __init__(
            self,
            log: logging.Logger,
            find_element_helper: FindElementHelper,
            wait_element_helper: WaitElementHelper,
            service_function_helper: ServiceFunctionHelper):
        """
        Конструктор для инициализации параметров
        :param log: Инициализация логов
        :param find_element_helper: Инициализация хелпера для поиска элементов
        :param wait_element_helper: Инициализация хелпера ожидания
        """
        super().__init__()
        assert isinstance(log, logging.Logger)
        self.log = log
        assert isinstance(wait_element_helper, WaitElementHelper)
        assert isinstance(find_element_helper, FindElementHelper)
        assert isinstance(service_function_helper, ServiceFunctionHelper)
        self.find_element_helper = find_element_helper
        self.wait_element_helper = wait_element_helper
        self.service_function_helper = service_function_helper

    # TODO Будет добавлена поддержка swipe для XCUITest https://github.com/facebook/WebDriverAgent/commit/143332260c53561bb7e544ae4e2d4b8dc649ac8d
    def swipe_element(
            self,
            locator,
            direction,
            duration=3000,
            value_for_swipe=100):
        """
        Свайп вверх/вниз/влево/вправо

        :param locator: Локатор элемента для свайпа
        :param direction: Направление элемента для свайпа
        :param duration: Продолжительность
        :param value_for_swipe: Интенсивность свайпа
        :return:
        """
        map_area_attributes = self.get_element_attributes(locator)
        try:
            self.log.info("Свайп по экрану")
            if direction == 'up':
                self.driver.swipe(
                    map_area_attributes['center_x'],
                    map_area_attributes['center_y'],
                    map_area_attributes['center_x'],
                    map_area_attributes['center_y'] - value_for_swipe,
                    duration
                )
            elif direction == 'down':
                self.driver.swipe(
                    map_area_attributes['center_x'],
                    map_area_attributes['center_y'],
                    map_area_attributes['center_x'],
                    map_area_attributes['center_y'] + value_for_swipe,
                    duration
                )
            elif direction == 'left':
                self.driver.swipe(
                    map_area_attributes['center_x'],
                    map_area_attributes['center_y'],
                    map_area_attributes['center_x'] - value_for_swipe,
                    map_area_attributes['center_y'],
                    duration
                )
            elif direction == 'right':
                self.driver.swipe(
                    map_area_attributes['center_x'],
                    map_area_attributes['center_y'],
                    map_area_attributes['center_x'] + value_for_swipe,
                    map_area_attributes['center_y'],
                    duration
                )
                self.log.info(
                    "Свайп в направлении: '{0}' прошел успешно".format(direction))
            else:
                raise Exception(
                    "Неправильное направление: '{0}' для свайпа!".format(direction))
        except error:
            self.log.critical(
                "Свайп в направлении: '{0}' не работает!".format(direction))

    def get_element_attributes(self, locator):
        """
        Получить атрибуты у элемента

        :param locator: Локатор для элемента
        :return: Атрибуты элемента
        """
        element = self.wait_element_helper.wait_until_element_visible(
            locator, timeout=5)
        return {
            'center_x': (element.size['width'] / 2) + element.location['x'],
            'center_y': (element.size['height'] / 2) + element.location['y']
        }

    def pull_to_refresh(self, direction=True):
        """
        Pull to refresh экрана сверху вниз - если direction == True, и снизу вверх - если direction == False

        :param direction: Направление свайпа
        :return:
        """
        window_size = self.driver.get_window_size()
        starty = window_size["height"] * 0.90
        endy = window_size["height"] * 0.20
        startx = window_size["width"] / 2
        sleep(3)
        if direction:
            self.driver.swipe(startx, endy, startx, starty, 3000)
        else:
            self.driver.swipe(startx, starty, startx, endy, 3000)

    def scroll_to_direction(
            self,
            element="window_size",
            direction="down",
            time_sleep=5):
        """
        Скролл вверх/вниз

        :param element: Локатор элемента для скролла
        :param direction: Направление скролла
        :param time_sleep: time_sleep - время, которое нужно подождать перед тем, как выполнить скролл на устройстве
        :return:
        """
        platform = self.service_function_helper.get_device_capabilities('platformName')
        if platform == 'iOS':
            self.driver.execute_script("mobile: scroll", {"direction": "down"})
        else:
            value_height_device = int(self.driver.get_window_size().get("height"))
            value_width_device = int(self.driver.get_window_size().get("width"))
            value_x_scroll = value_width_device / 2
            value_end_y_scroll = value_height_device * 0.2
            value_start_y_scroll = value_height_device * 0.8
            if element != "window_size":
                scroll_element = self.wait_element_helper.wait_until_element_visible(
                    element, time_sleep)
                value_x_scroll = int((scroll_element.location.get("x") + 5))
            if direction == "down":
                self.log.info("Начало скролла вниз")
                try:
                    self.driver.swipe(

                        start_x=value_x_scroll,
                        start_y=value_start_y_scroll,
                        end_x=value_x_scroll,
                        end_y=value_end_y_scroll,
                    )
                    self.log.info("Скролл вниз прошел успешно")
                except Exception:
                    self.log.critical("Не удалось проскроллить вниз!!")
                    pass
            elif direction == "up":
                self.log.info("Начало скролла вверх")
                try:
                    self.driver.swipe(

                        start_x=value_x_scroll,
                        start_y=value_end_y_scroll,
                        end_x=value_x_scroll,
                        end_y=value_start_y_scroll,
                    )
                    self.log.info("Скролл вверх прошел успешно")
                except error:
                    self.log.critical("Не удалось проскроллить вверх!!")
                    pass

    def scroll_while_element_is_visible(
            self,
            target_element_locator,
            limit=5,
            scroll_element="window_size",
            direction="down"):
        """
        Скроллить пока элемент виден

        :param target_element_locator: Локатор для видимого элемента
        :param limit: Количество возможных скроллов по экрану
        :param scroll_element: Локатор элемента для скролла
        :param direction: Направление скролла
        :return:
        """
        scroll_element = scroll_element
        direction = direction
        for i in range(0, limit):
            if self.find_element_helper.is_visible_element(
                    target_element_locator):
                self.scroll_to_direction(scroll_element, direction)
            else:
                break

    def scroll_while_element_is_invisible(
            self,
            target_element_locator,
            limit=5,
            scroll_element="window_size",
            direction="down"):
        """
        Скроллить пока элемент не виден

        :param target_element_locator: Локатор элемента, который нужно найти
        :param limit: Количество возможных скроллов по экрану
        :param scroll_element: Локатор элемента для скролла
        :param direction: Направление скролла
        :return:
        """
        scroll_element = scroll_element
        direction = direction
        for i in range(0, limit):
            if self.find_element_helper.is_visible_element(
                    target_element_locator) == False:
                self.scroll_to_direction(scroll_element, direction)
            else:
                break