# import time
# from conftest import driver
# from pages.base_page import BasePage
#
#
# def test(driver):
#     page = BasePage(driver, 'https://www.google.ru')
#     page.open()
#     time.sleep(2)
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from conftest import driver
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


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
class TestRadioButton:
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        # radio_button_page.click_order_radio_button() - для последовательного вызова и проверки тут
        # radio_button_page.click_random_radio_button() - для рандомного нажатия
        # a, b = radio_button_page.click_order_radio_button2() - мое решение №1
        # assert a == b, 'radio-buttons did not match'
        # time.sleep(2)
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', 'the radio button "YES" did not match'
        assert output_impressive == 'Impressive', 'the radio button "IMPRESSIVE" did not match'
        assert output_no == 'No', 'the radio button "NO" did not match'
class TestWebTable:
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        print(new_person)
        print(table_result)
        assert new_person in table_result

    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0,5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        print(key_word)
        print(table_result)
        assert key_word in table_result, "the person was not found in the table"

    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        print(age)
        print(row)
        assert age in row, "the age was not found in the table"

    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == "No rows found", "the string was not deleted in the table"

    def test_web_table_change_count_rows(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        web_table_page.scroll_down()
        count = web_table_page.select_up_to_some_rows()
        assert count == [5, 10, 20, 25, 50, 100]

class TestButtonsPage:
    def test_different_click_on_the_buttons(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        double = button_page.click_on_different_button('double')
        right = button_page.click_on_different_button('right')
        click = button_page.click_on_different_button('click')
        time.sleep(4)
        print(double)
        print(right)
        print(click)
        assert double == "You have done a double click", 'the double did not match in the buttons'
        assert right == "You have done a right click", 'the right did not match in the buttons'
        assert click == "You have done a dynamic click", 'the click did not match in the buttons'



