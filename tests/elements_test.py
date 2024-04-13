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
        test_box_page.scroll_down()
        test_box_page.click_submit()
        output_name, output_email, output_current_address, output_permanent_address = test_box_page.check_filled_form()
        print()
        print(output_name)
        print(output_email)
        print(output_current_address)
        print(output_permanent_address)
        # print(test_box_page.check_filled_form()) - первый вариант вывода информации
        time.sleep(2)


