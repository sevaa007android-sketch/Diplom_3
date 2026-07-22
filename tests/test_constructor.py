import allure
import pytest
from pages.main_page import MainPage
from pages.ingredient_modal import IngredientModal
from data import BASE_URL

@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход на страницу конструктора по клику на кнопку «Конструктор»")
    def test_constructor_tab_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert BASE_URL == main_page.get_current_url()

    @allure.title("Клик на ингредиент — открывается модальное окно с деталями")
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        modal = IngredientModal(driver)
        assert modal.is_modal_open() is True

    @allure.title("Модальное окно закрывается по клику на крестик")
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        modal = IngredientModal(driver)
        modal.close_modal()
        modal.wait_for_modal_closed()
        assert modal.is_modal_open() is False

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        initial_counter = int(main_page.get_first_ingredient_counter())
        main_page.drag_first_ingredient_to_constructor()
        main_page.wait_for_counter_increase(initial_counter)
        new_counter = int(main_page.get_first_ingredient_counter())
        assert new_counter > initial_counter