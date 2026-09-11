from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import allure
import pytest


@pytest.mark.ui
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Поисковые подсказки")
@allure.feature("Поиск")
@allure.title("Отображение подсказок при поиске")
def test_get_suggestions(driver) -> None:
    """Вводит запрос и проверяет отображение подсказок."""
    main_page = MainPage(driver)

    with allure.step("Ввести посковый запрос"):
        main_page.enter_search("Гордость и Предубеждение")
    with allure.step("Проверить, что подсказки отображаются"):
        main_page.check_suggestions_visibility()
    with allure.step("Проверить наличие подсказок"):
        assert main_page.check_suggestions_visibility()


@pytest.mark.ui
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Поиск по невалидному запросу")
@allure.feature("Поиск")
@allure.title("Отсутствие результатов при невалидном поиске")
def test_invalid_input(driver) -> None:
    """Проверяет отсутсвие результатов при невалидном запросе."""
    main_page = MainPage(driver)

    main_page.search_by_enter("()+=")

    with allure.step("Проверить, что появлется текст ошибки"):
        assert "не принес результатов" in main_page.get_search_error()


@pytest.mark.ui
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Карточка товара")
@allure.feature("Каталог")
@allure.title("Открытие карточки товара")
def test_open_product_page(driver) -> None:
    """Проверяет корректность открытия карточки товара из каталога."""
    main_page = MainPage(driver)
    catalog_page = CatalogPage(driver)
    product_page = ProductPage(driver)

    with allure.step("Ввести поисковый запрос и кликнуть по кнопке поиска"):
        main_page.search("Гордость и предубеждение")
    with allure.step("Кликнуть по обложке книги"):
        catalog_page.click_book_cover("Гордость и предубеждение")

    with allure.step("Проверить название книги в заголовке карточки товара"):
        assert "Гордость и предубеждение" in product_page.get_book_title()


@pytest.mark.ui
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Поиск книг")
@allure.feature("Поиск")
@allure.title("Поиск книг по жанру")
def test_search_by_genre(driver) -> None:
    """Проверяет корректность поиска книг по жанру."""
    main_page = MainPage(driver)
    catalog_page = CatalogPage(driver)

    genre = "детективы"
    with allure.step("Ввести поисковый запрос по жанру и нажать Enter"):
        main_page.search_by_enter(genre)

    with allure.step("Проверить название жанра в заголовке каталога"):
        assert genre in catalog_page.get_search_title()


@pytest.mark.ui
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Оформление заказа")
@allure.feature("Корзина")
@allure.title("Переход к оформлению заказа")
def test_proceed_to_checkout(driver) -> None:
    """Проверяет переход к оформлению заказа
    для неавторизованного пользователя"""
    main_page = MainPage(driver)
    catalog_page = CatalogPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    with allure.step("Ввести посковый запрос"):
        main_page.search("Гордость и предубеждение")
    with allure.step("Кликнуть по обложке книги"):
        catalog_page.click_book_cover("Гордость и предубеждение")
    with allure.step("Кликнуть по кнопке купить"):
        product_page.click_buy_button()
    with allure.step("Кликнуть по кнопке оформить"):
        catalog_page.click_cart_button()
    with allure.step("Кликнуть по кнопке корзины"):
        cart_page.click_checkout_button()

    with allure.step("Проверить появление окна авторизации"):
        assert "Вход" in cart_page.get_auth_title()
