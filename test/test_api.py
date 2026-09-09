import requests
from config import base_url, headers
import allure
import pytest


@pytest.mark.api
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Добавление товара")
@allure.feature("Корзина")
@allure.title("Добавление товара в корзину")
def test_add_to_cart() -> None:
    """Добавляет товар в корзину и проверяет его наличие."""
    product_id = {
        "id": 3136715
    }

    with allure.step("Отправка запроса на добавление товара в корзину"):
        resp = requests.post(
            f"{base_url}/web/api/v1/cart/product",
            json=product_id,
            headers=headers
        )

    assert resp.status_code == 200

    with allure.step("Проверка содержимого корзины"):
        resp = requests.get(
            f"{base_url}/web/api/v1/cart",
            headers=headers
        )

    with allure.step("Проверка статус-кода ответа"):
        assert resp.status_code == 200

    with allure.step("Проверка наличия id товара в ответе"):
        response = resp.json()
        assert response["products"][0]["goodsId"] == 3136715


@pytest.mark.api
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Поиск товара")
@allure.feature("Каталог")
@allure.title("Поиск товара по названию")
def test_search_by_name() -> None:
    """Проверяет поиск книги по названию"""
    book_name = "Онегин"
    params = {
        "phrase": book_name
    }

    with allure.step("Отправка поискового запроса с названием книги"):
        resp = requests.get(
                f"{base_url}/web/api/v2/search/product?phrase={book_name}",
                headers=headers,
                params=params
            )

    with allure.step("Проверка статус-кода ответа"):
        assert resp.status_code == 200

    with allure.step("Проверка наличия названия книги в ответе"):
        response = resp.json()
        title = response["data"]["attributes"]["seo"]["title"].lower()
        assert book_name.lower() in title


@pytest.mark.api
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Поиск товара")
@allure.feature("Каталог")
@allure.title("Поиск товара по автору")
def test_search_by_author() -> None:
    """Проверяет поиск книги по автору"""
    author_name = "Пушкин"
    params = {
        "phrase": author_name
    }

    with allure.step("Отправка поискового запроса с именем автора"):
        resp = requests.get(
                f"{base_url}/web/api/v2/search/product?phrase={author_name}",
                headers=headers,
                params=params
            )

    with allure.step("Проверка статус-кода ответа"):
        assert resp.status_code == 200

    with allure.step("Проверка наличия имени автора в ответе"):
        response = resp.json()
        title = response["data"]["attributes"]["seo"]["title"].lower()
        assert author_name.lower() in title


@pytest.mark.api
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Поиск товара")
@allure.feature("Каталог")
@allure.title("Поиск товара без параметра phrase")
def test_search_without_param_phrase() -> None:
    """Проверяет ошибку при поиске без параметра phrase"""

    with allure.step("Отправка поискового запроса без параметра"):
        resp = requests.get(
            f"{base_url}/web/api/v2/search/product",
            headers=headers,
        )

    with allure.step("Проверка статус-кода ответа"):
        assert resp.status_code == 400

    with allure.step("Проверка текста ошибки"):
        response = resp.json()
        assert response["errors"][0]["title"] == "Phrase обязательное поле"


@pytest.mark.api
@allure.epic("Интернет-магазин Читай-Город")
@allure.story("Добавление товара")
@allure.feature("Корзина")
@allure.title("Добавление товара в корзину по несуществующему id")
def test_search_nonexistent_product() -> None:
    """Проверяет ошибку при добавлении несуществующего товара"""
    product_id = {
        "id": 6679840980248
    }

    with allure.step(
            "Отправка запроса на добавление несуществующего товара в корзину"):
        resp = requests.post(
            f"{base_url}/web/api/v1/cart/product",
            json=product_id,
            headers=headers
        )

    with allure.step("Проверка статус-кода ответа"):
        assert resp.status_code == 400

    with allure.step("Проверка текста ошибки"):
        response = resp.json()
        assert response["message"] == "данного товара не существует"
