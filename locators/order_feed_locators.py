from selenium.webdriver.common.by import By

class OrderFeedLocators:
    COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number__')]")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__')]")
    ORDERS_IN_WORK = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")