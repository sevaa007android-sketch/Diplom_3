import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Ввести email")
    def set_email(self, email):
        self.find(self.locators.EMAIL_FIELD).send_keys(email)

    @allure.step("Ввести пароль")
    def set_password(self, password):
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажать кнопку «Войти»")
    def click_login_button(self):
        self.click(self.locators.LOGIN_BUTTON)

    @allure.step("Авторизоваться с данными")
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

