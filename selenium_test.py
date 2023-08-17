import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = Options()
# options.add_argument('--headless')
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

# accept cookies
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Zaakceptuj wszystko']"))).click()

# search in google
google_input = (By.XPATH, "//input[@title='Szukaj']")
wait.until(EC.element_to_be_clickable(google_input))
element = driver.find_element(*google_input)
element.send_keys("Lama wikipedia")
element.send_keys(Keys.ENTER)

# wikipedia link
wiki_link = driver.find_element(By.XPATH, "//h3[contains(text(),'Lama – Wikipedia')]")
wait.until(EC.element_to_be_clickable(wiki_link))
wiki_link.click()


time.sleep(10)
driver.quit()


