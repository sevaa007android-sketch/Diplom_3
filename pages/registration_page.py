import allure
from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegistrationPageLocators()

    @allure.step("Ввести имя")
    def set_name(self, name):
        self.find(self.locators.NAME_FIELD).send_keys(name)

    @allure.step("Ввести email")
    def set_email(self, email):
        self.find(self.locators.EMAIL_FIELD).send_keys(email)

    @allure.step("Ввести пароль")
    def set_password(self, password):
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажать кнопку «Зарегистрироваться»")
    def click_register_button(self):
        self.click(self.locators.REGISTER_BUTTON)

    @allure.step("Зарегистрироваться с данными")
    def register(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_register_button()

    @allure.step("Получить текст ошибки пароля")
    def get_password_error(self):
        return self.get_text(self.locators.PASSWORD_ERROR)