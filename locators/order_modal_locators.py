from selenium.webdriver.common.by import By

class OrderModalLocators:
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__') and contains(@class, 'text_type_digits-large')]")
    CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close_modified__')]")
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")