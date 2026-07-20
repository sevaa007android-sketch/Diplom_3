import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from helpers import generate_user_data
from api.user_api import register_user, delete_user
from locators.main_page_locators import MainPageLocators
import time

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
    # 1. Генерируем данные пользователя
    user_data = generate_user_data()
    
    # 2. Регистрируем пользователя через API
    register_response = register_user(user_data)
    assert register_response.status_code == 200, "Не удалось зарегистрировать пользователя через API"
    token = register_response.json()["accessToken"]
    
    # 3. Логинимся через UI (чтобы браузер получил сессионные куки)
    main_page = MainPage(driver)
    main_page.click_personal_account()
    login_page = LoginPage(driver)
    login_page.login(user_data['email'], user_data['password'])
    
    # 4. Ожидаем загрузку главной страницы
    main_page.wait_for_invisibility(MainPageLocators.LOGIN_BUTTON_MAIN)
    main_page.wait_for_visibility(MainPageLocators.CONSTRUCTOR_BUTTON)
    # Небольшая задержка для синхронизации состояния сессии
    time.sleep(0.5)
    
    yield user_data  # возвращаем только данные пользователя (токен не нужен в тестах)
    
    # 5. Удаляем пользователя через API
    delete_user(token)