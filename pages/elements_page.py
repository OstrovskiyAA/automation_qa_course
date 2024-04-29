from selenium.webdriver.common.by import By

from generation.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckboxPageLocators
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
                count-=1
            else:
                break
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data2 =[]
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