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
from pages.elements_page import TextBoxPage, CheckBoxPage


class TestTextBox:
    def test_text_box(self, driver):
        test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        test_box_page.open()
        # input_data = test_box_page.fill_all_fields()
        full_name, email, current_address, permanent_address = test_box_page.fill_all_fields()
        test_box_page.scroll_down()
        test_box_page.click_submit()
        output_name, output_email, output_current_address, output_permanent_address = test_box_page.check_filled_form()
        print()
        assert full_name == output_name, "the full name doesn't match"
        assert email == output_email, "the full name doesn't match"
        assert current_address == output_current_address, "the full name doesn't match"
        assert permanent_address == output_permanent_address, "the full name doesn't match"
        # output_data = test_box_page.check_filled_form()
        # assert input_data == output_data
        time.sleep(5)
class TestCheckbox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        print(input_checkbox)
        print(output_result)
        assert input_checkbox == output_result, 'check box did not match'