from selenium.webdriver.common.by import By
import time
from generation.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckboxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators
from pages.base_page import BasePage
import random


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return full_name, email, current_address, permanent_address

    def click_submit(self):
        self.element_is_clickable(self.locators.SUBMIT).click()

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckboxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data2 = []
        for box in checked_list:
            # title_item = box.find_element(by=By.XPATH, value=".//ancestor::span[@class='rct-text']")
            title_item = box.find_element(by=By.XPATH, value=self.locators.TITLE_ITEM)
            # title_item = box.find_element_by_xpatch(self.locators.TITLE_ITEM) - устаревшая версия
            data2.append(title_item.text)
        return str(data2).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()

    # data11 = str(data11).replace(' ', '').replace('doc', '').replace('.', '').lower()
    # data22 = str(data22).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    # def click_random_radio_button(self): - для рандомного вызова
    #     item_list = self.elements_are_present(self.locators.INPUT_RADIO_BUTTON)
    #     count = 0
    #     while count == 0:
    #         item = item_list[random.randint(0, 1)]
    #         self.go_to_element(item)
    #         item.click()
    #         count -=1
    # =======================================================================================
    # def click_order_radio_button(self): - для последовательного вызова и проверки тут
    #     item_list = self.elements_are_present(self.locators.INPUT_RADIO_BUTTON)
    #     for i in range(len(item_list)):
    #         self.go_to_element(item_list[i])
    #         item_list[i].click()
    #         input_item = item_list[i]
    #         output_item = self.element_is_present(self.locators.OUTPUT_RADIO_BUTTON)
    #         if output_item.text != input_item.text:
    #             print("Ошибочные значения")
    #             break
    #         time.sleep(2)
    #         print(f'{output_item.text} = {input_item.text}')
    # =========================================================================================
    # def click_order_radio_button2(self): - мое решение №1
    #     item_list = self.elements_are_present(self.locators.INPUT_RADIO_BUTTON)
    #     a=[]
    #     b=[]
    #     for i in range(len(item_list)):
    #         self.go_to_element(item_list[i])
    #         item_list[i].click()
    #         input_item = item_list[i]
    #         output_item = self.element_is_present(self.locators.OUTPUT_RADIO_BUTTON)
    #         a.append(input_item.text)
    #         b.append(output_item.text)
    #         if output_item.text != input_item.text:
    #             print("Ошибочные значения")
    #             break
    #         time.sleep(2)
    #         print(f'{output_item.text} = {input_item.text}')
    #     return a, b
    # ==================================================================================
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            # преобразуем из кортежа в список
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            # убираем разделители/n
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(by=By.XPATH, value=self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_present(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.check_count_rows())
        return data


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text
