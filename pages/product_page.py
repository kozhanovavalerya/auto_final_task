from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import StaleElementReferenceException


class ProductPage:
    # book_title = (By.CSS_SELECTOR,
    #               ".product-offer__buttons "
    #               "[data-testid-button-mini-product-card='canBuy']")
    book_title = (By.CSS_SELECTOR, ".product-detail-page__title")

    buy_button = (
        By.CSS_SELECTOR,
        '[data-testid-button-mini-product-card="canBuy"]'
    )

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получить заголовок книги")
    def get_book_title(self) -> str:
        """Возвращает заголовок в карточке товара"""
        book_title = WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(self.book_title)
        )
        return book_title.text.strip()

    @allure.step("Клик по кнопке Купить")
    def click_buy_button(self) -> None:
        "Кликает по кнопке купить в карточке товара."
        for _ in range(3):
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.buy_button)
                ).click()
                return
            except StaleElementReferenceException:
                pass
