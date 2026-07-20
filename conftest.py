import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from helpers import generate_user_data
from locators.main_page_locators import MainPageLocators

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser} not supported")
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def authorized_user(driver):
    user_data = generate_user_data()
    main_page = MainPage(driver)
    main_page.click_personal_account()
    login_page = LoginPage(driver)
    login_page.click_register_link()
    reg_page = RegistrationPage(driver)
    reg_page.register(user_data['name'], user_data['email'], user_data['password'])
    main_page.click_personal_account()
    login_page.login(user_data['email'], user_data['password'])
    main_page.wait_for_invisibility(MainPageLocators.LOGIN_BUTTON_MAIN)
    main_page.wait_for_visibility(MainPageLocators.CONSTRUCTOR_BUTTON)
    # Небольшая задержка для синхронизации состояния сессии после логина
    time.sleep(0.5)
    return user_data