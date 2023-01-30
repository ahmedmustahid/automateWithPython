from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "./chromedriver"

options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options= options)

driver.get(website)

containers = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]')

titles, subtitles, links = [], [], []
for container in containers:
    title = container.find_element(By.XPATH, value='./a/h3').text
    subtitle = container.find_element(By.XPATH, value='./a/p').text
    link = container.find_element(By.XPATH, value='./a').get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

myDict = {"title": titles, "subtitle":subtitles, "link": links}

df_headlines = pd.DataFrame(myDict)
df_headlines.to_csv("headlines-headless.csv")

driver.quit()
