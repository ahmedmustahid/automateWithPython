from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import urllib

count = 0
for year in range(2020,2022):
    for month in range(6,10):
        imgList = "imagelist-"+str(year)+str(month).zfill(2)
        website="https://ameblo.jp/pusan1128/"+imgList+".html"
        print(website)
        path="./chromedriver"
        options = Options()
        #options.headless = True
        options.add_argument("--headless")
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service, options= options)
        driver.get(website)
        containers = driver.find_elements(By.XPATH, '//img[@class="_27myuTAX _3QqJNJb_"]')
        for container in containers:
            count = count + 1
            #if not count>16:
            #    continue
            print(count)
            links = container.get_attribute('srcset')
            print(links)
            if len(links)<10:
                continue
            imgLink = links.split(",")[-1]
            print(imgLink)
            imgLink = imgLink.split()[0]
            print(imgLink)
            urllib.request.urlretrieve(imgLink, "images/"+str(count)+".jpg")
        #break
