import pytest
from selenium import webdriver
from config import ui_url


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ui_url)
    yield driver

    driver.quit()
