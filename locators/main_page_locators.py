from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")   # <-- возвращаем
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@href, '/ingredient/')])[1]")
    FIRST_INGREDIENT_COUNTER = (By.XPATH, "(//a[contains(@href, '/ingredient/')])[1]//p[contains(@class, 'counter_counter__num__')]")
    CONSTRUCTOR_DROP_TARGET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__')]")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")