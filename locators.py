from selenium.webdriver.common.by import By


class AcceptCookies(object):
    """A class for accept cookies locators"""

    ACCEPT_BUTTON = (By.XPATH, "//div[text()='Zaakceptuj wszystko']")


class GoogleSearchLocators(object):
    """A class for Google search locators"""

    INPUT_SEARCH_FIELD = (By.XPATH, "//input[@title='Szukaj']")
    WIKI_LINK = (By.XPATH, "//h3[contains(text(),'– Wikipedia')]")


class WikiLocators(object):

    ANIMAL_TABLE = (By.XPATH, "//table[@class='infobox infobox-zwierzeta']")