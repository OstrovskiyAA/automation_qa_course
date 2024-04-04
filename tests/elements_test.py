import time
from conftest import driver
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://www.google.ru')
    page.open()
    time.sleep(2)
