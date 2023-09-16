from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument("--disable-infobars")
# driver = webdriver.Chrome(options = chrome_options)
# driver.get("https://www.faceit.com/en/csgo/room/1-0ec43dc8-be2f-4e97-9d1b-5e82d7db0f77")
# driver.implicitly_wait(5)
# el = driver.find_element(By.NAME, "roster1")
# print(el.text)


def get_nicknames(url: str, team_number: int):
    """Team on the left has number1. Team on the right has number2"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(url)
    driver.implicitly_wait(5)
    all_nicknames = (driver.find_element(By.NAME,f"roster{team_number}").text).split("\n")
    required_nicknames = [all_nicknames[0],all_nicknames[2], all_nicknames[4], all_nicknames[6], all_nicknames[8]]
    return required_nicknames

members = get_nicknames("https://www.faceit.com/en/csgo/room/1-0ec43dc8-be2f-4e97-9d1b-5e82d7db0f77",1)
print(members)