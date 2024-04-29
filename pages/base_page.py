from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
    def open(self):
        self.driver.get(self.url)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def element_is_visible(self, locator, timeout=100):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=100):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=100):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=100):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    # def find_element_by_xpath(self, locator, timeout=100):
    #     return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    def element_is_not_visible(self, locator, timeout=100):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=100):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)