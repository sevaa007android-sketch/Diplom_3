import allure
import time
from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators
from locators.main_page_locators import MainPageLocators

class OrderModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderModalLocators()

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        self.wait_for_text_not_equal(self.locators.ORDER_NUMBER, "9999")
        text = self.get_text(self.locators.ORDER_NUMBER)
        # Убираем ведущие нули, преобразуя в int и обратно в строку
        return str(int(text))

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        close_btn = self.find(self.locators.CLOSE_BUTTON)
        self.execute_script("arguments[0].click();", close_btn)
        self.wait_for_invisibility(self.locators.OVERLAY)
        self.wait_for_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        time.sleep(0.5)