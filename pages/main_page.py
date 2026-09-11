from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure
from selenium.common.exceptions import TimeoutException


class MainPage:
    search_input = (By.ID, "app-search")
    search_button = (By.CSS_SELECTOR, ".search-form__button-search")
    suggestion = (By.CSS_SELECTOR, ".suggests-list-item__link")
    search_error = (By.CSS_SELECTOR, ".search-title__head")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Выполнить поиск по запросу")
    def search(self, search_query: str) -> None:
        """Выполняет поиск по заданному запросу."""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_input)
        )
        search_input.send_keys(search_query)
        WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.suggestion)
                )
        search_input.send_keys(Keys.ESCAPE)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    @allure.step("Ввести поисковый запрос без запуска поиска")
    def enter_search(self, search_query: str) -> None:
        """Вводит поисковый запрос без запуска поиска."""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_input)
        )
        search_input.send_keys(search_query)

    @allure.step("Проверить отображение подсказок")
    def check_suggestions_visibility(self) -> None:
        """Проверяет отображение подсказок"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.suggestion)
        ).is_displayed

    @allure.step("Проверть наличие сообщения об ошибке")
    def get_search_error(self) -> str:
        """Возвращает текст сообщения об ошибке."""
        search_error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_error)
        )
        return search_error.text.strip()

    @allure.step("Выполнить поиск с помощью клавиши Enter")
    def search_by_enter(self, search_query: str) -> None:
        """Выполняет поиск по запросу с помощью клавиши Enter."""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_input)
        )
        search_input.send_keys(search_query, Keys.ENTER)

        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.search_error)
            )
        except TimeoutException:
            WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable(self.search_button)
            ).click()
