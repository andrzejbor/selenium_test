import locators
from element import BasePageElement


class BasePage:
    """Base clas to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class GooglePage(BasePage):
    """Google search page"""

    def search_in_google(self, search_text):
        BasePageElement.set_input_value_and_press_enter(self.driver, search_text, locators.GoogleSearchLocators.INPUT_SEARCH_FIELD)

    def go_to_wiki_page(self):
        BasePageElement.click_on_element(self.driver, locators.GoogleSearchLocators.WIKI_LINK)


class DefaultPage(BasePage):

    def accept_cookie(self):
        BasePageElement.click_on_element(self.driver, locators.AcceptCookies.ACCEPT_BUTTON)


class WikipediaPage(BasePage):

    def get_animal_information(self):
        table_content = BasePageElement.get_information_from_table(self.driver, locators.WikiLocators.ANIMAL_TABLE)
        attribute_list = table_content[0].text.split("\n")
        attribute_list = attribute_list[attribute_list.index("Domena"):(attribute_list.index("Gatunek")+2)]
        return attribute_list
