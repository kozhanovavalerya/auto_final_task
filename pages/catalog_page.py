from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CatalogPage:

    cart_button = (By.CSS_SELECTOR, '[data-testid-button-header="cart"]')
    search_title = (By.CSS_SELECTOR, ".search-title__head")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по обложке книги")
    def click_book_cover(self, book_name: str) -> None:
        """Находит книгу в каталоге и кликает по ее обложке."""
        book_cover = (
                By.XPATH,
                f'//a[contains(@title, "{book_name}")]'
            )
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(book_cover)
        ).click()

    @allure.step("Клик по кнопке карзины")
    def click_cart_button(self) -> None:
        """Кликает по кнопке корзины в header."""
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.cart_button)
        ).click()

    @allure.step("Получить заголовок результатов поиска")
    def get_search_title(self) -> str:
        "Возвращает текст заголовка результатов поиска."
        search_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_title)
        )
        return search_title.text.strip()
