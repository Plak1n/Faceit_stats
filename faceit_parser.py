from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.faceit.com/en/csgo/room/1-0ec43dc8-be2f-4e97-9d1b-5e82d7db0f77")
driver.implicitly_wait(5)
el = driver.find_element(By.NAME, "roster1")
print(el.text)
