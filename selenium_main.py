from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import page
import excel_report

options = Options()
# options.add_argument('--headless')
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
default_page = page.DefaultPage(driver)
default_page.accept_cookie()

animal_list = ['lama', 'owca', 'koza']
result_list = []

for animal in animal_list:
    driver.get("https://www.google.com")

    google_page = page.GooglePage(driver)
    google_page.search_in_google(animal)
    google_page.go_to_wiki_page()

    wiki_page = page.WikipediaPage(driver)
    result_list.append(wiki_page.get_animal_information())

excel_report.create_excel_file(result_list, 'Animals.xlsx', animal_list)
driver.quit()




