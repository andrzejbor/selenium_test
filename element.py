import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePageElement(object):
    """Base page class that initialized on every page object class."""

    @staticmethod
    def set_input_value_and_press_enter(driver, value, locator):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).clear()
        driver.find_element(*locator).send_keys(value)
        driver.find_element(*locator).send_keys(Keys.ENTER)

    @staticmethod
    def click_on_element(driver, locator):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()


    @staticmethod
    def get_information_from_table(driver, locator):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        return driver.find_elements(*locator)
