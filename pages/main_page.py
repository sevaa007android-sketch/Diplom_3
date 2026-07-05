import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_modal_locators import OrderModalLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Клик по кнопке «Конструктор»")
    def click_constructor(self):
        self.click(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке «Лента заказов»")
    def click_order_feed(self):
        try:
            self.wait_for_invisibility(OrderModalLocators.OVERLAY)
        except:
            pass
        element = self.find(self.locators.ORDER_FEED_BUTTON)
        self.execute_script("arguments[0].scrollIntoView(true);", element)
        self.execute_script("arguments[0].click();", element)
        self.wait_for_url_contains("/feed")

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(self.locators.FIRST_INGREDIENT)

    @allure.step("Получить значение счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        return self.get_text(self.locators.FIRST_INGREDIENT_COUNTER)

    @allure.step("Клик по кнопке «Войти в аккаунт»")
    def click_login_button_main(self):
        self.click(self.locators.LOGIN_BUTTON_MAIN)

    @allure.step("Клик по кнопке «Личный кабинет»")
    def click_personal_account(self):
        self.click(self.locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Перетащить первый ингредиент в конструктор")
    def drag_first_ingredient_to_constructor(self):
        self.drag_and_drop(
            self.locators.FIRST_INGREDIENT,
            self.locators.CONSTRUCTOR_DROP_TARGET
        )

    @allure.step("Дождаться увеличения счётчика ингредиента")
    def wait_for_counter_increase(self, initial_value):
        self.wait.until(lambda driver: int(self.get_first_ingredient_counter()) > initial_value)

    @allure.step("Клик по кнопке «Оформить заказ»")
    def click_checkout(self):
        self.click(self.locators.CHECKOUT_BUTTON)

    @allure.step("Клик по логотипу")
    def click_logo(self):
        self.click(self.locators.LOGO)