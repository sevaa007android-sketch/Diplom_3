import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_counter_all_time(self):
        return int(self.get_text(self.locators.COUNTER_ALL_TIME))

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_counter_today(self):
        return int(self.get_text(self.locators.COUNTER_TODAY))

    @allure.step("Получить список номеров заказов в разделе «В работе»")
    def get_orders_in_work(self):
        elements = self.find_elements(self.locators.ORDERS_IN_WORK)
        # Убираем ведущие нули и преобразуем в строку без пробелов
        return [str(int(el.text.replace('\n', '').strip())) for el in elements if el.text.replace('\n', '').strip().isdigit()]
    
    @allure.step("Дождаться увеличения счетчика «Выполнено за всё время»")
    def wait_for_counter_all_time_increase(self, initial_all_time):
        self.wait.until(lambda d: self.get_counter_all_time() > initial_all_time)
        
    @allure.step("Дождаться увеличения счетчика «Выполнено за сегодня»")
    def wait_for_counter_today_increase(self, initial_today):
        self.wait.until(lambda d: self.get_counter_today() > initial_today)
        
    @allure.step("Дождаться что номер созданного заказа появляется в разделе «В работе»")
    def wait_for_orders_in_work(self, order_number):
        self.wait.until(lambda d: order_number in self.get_orders_in_work())    