# import time
# from conftest import driver
# from pages.base_page import BasePage
#
#
# def test(driver):
#     page = BasePage(driver, 'https://www.google.ru')
#     page.open()
#     time.sleep(2)
import time
from conftest import driver
from pages.elements_page import TextBoxPage


class TestTextBox:
    def test_text_box(self, driver):
        test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        test_box_page.open()
        test_box_page.fill_all_fields()
        test_box_page.click_submit()
        time.sleep(5)
