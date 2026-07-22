import allure
import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_modal import OrderModal
from data import FEED_URL

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Переход на страницу ленты заказов по клику на кнопку")
    def test_order_feed_tab_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert main_page.get_current_url() == FEED_URL

    @allure.title("Счётчик «Выполнено за всё время» увеличивается после создания заказа")
    def test_order_counter_all_time_increases(self, driver, authorized_user):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        initial_all_time = feed_page.get_counter_all_time()
        main_page.click_constructor()
        main_page.drag_first_ingredient_to_constructor()
        main_page.wait_for_counter_increase(0)
        main_page.click_checkout()
        order_modal = OrderModal(driver)
        order_modal.close_modal()

        main_page.click_order_feed()
        feed_page.wait_for_counter_all_time_increase(initial_all_time)
        new_all_time = feed_page.get_counter_all_time()
        assert new_all_time > initial_all_time

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после создания заказа")
    def test_order_counter_today_increases(self, driver, authorized_user):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        initial_today = feed_page.get_counter_today()
        main_page.click_constructor()
        main_page.drag_first_ingredient_to_constructor()
        main_page.wait_for_counter_increase(0)
        main_page.click_checkout()
        order_modal = OrderModal(driver)
        order_modal.close_modal()

        main_page.click_order_feed()
        feed_page.wait_for_counter_today_increase(initial_today)
        new_today = feed_page.get_counter_today()
        assert new_today > initial_today

    @allure.title("Номер созданного заказа появляется в разделе «В работе»")
    def test_order_number_appears_in_work(self, driver, authorized_user):
        main_page = MainPage(driver)
        main_page.drag_first_ingredient_to_constructor()
        main_page.wait_for_counter_increase(0)
        main_page.click_checkout()
        order_modal = OrderModal(driver)
        order_number = order_modal.get_order_number()
        order_modal.close_modal()
        main_page.click_order_feed()
        feed_page = OrderFeedPage(driver)
        feed_page.wait_for_orders_in_work(order_number)
        assert order_number in feed_page.get_orders_in_work()