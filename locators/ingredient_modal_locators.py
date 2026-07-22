from selenium.webdriver.common.by import By

class IngredientModalLocators:
    MODAL_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__')]//button[contains(@class, 'Modal_modal__close_modified__')]")