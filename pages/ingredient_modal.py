import allure
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators

class IngredientModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = IngredientModalLocators()

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_open(self):
        try:
            self.find(self.locators.MODAL_OPENED)
            return True
        except:
            return False

    @allure.step("Закрыть модальное окно (клик по крестику)")
    def close_modal(self):
        self.click(self.locators.MODAL_CLOSE_BUTTON)

    @allure.step("Дождаться закрытия модального окна")
    def wait_for_modal_closed(self):
        self.wait_for_invisibility(self.locators.MODAL_OPENED)