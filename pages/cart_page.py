from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    checkout_button = (By.CSS_SELECTOR,
                       '[data-testid-button-cart="goToCheckout"]')

    auth_page = (
        By.CSS_SELECTOR, ".ui-header-modal__title"
    )

    cart_page_title = (
        By.CSS_SELECTOR, ".cart-page__title"
    )

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Перейти к оформлению заказа")
    def click_checkout_button(self) -> None:
        """Нажимает на кнопку Оформить заказ"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    @allure.step("Получить заголовок окна авторизации")
    def get_auth_title(self) -> str:
        """ Возвращает текст заголовка окна авторизации"""
        auth_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.auth_page)
        )
        return auth_title.text.strip()
