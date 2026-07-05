from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")