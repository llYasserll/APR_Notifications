from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

import time

edge_options = Options()
#edge_options.add_argument("--headless")

driver = webdriver.Edge()

driver.get("https://www.bybit.com/es-419/trade/spot/launchpool")
driver.maximize_window()
time.sleep(6)
comingSoon = driver.find_elements(By.XPATH, "//div[4]/div/div[3]/div/div/div[1]")
APR = driver.find_elements(By.XPATH, "//div[4]//div[3]/div/div/div[2]/div[2]/div[5]/div[1]/div[4]/div[1]/div[2]/div[1]")
coin = driver.find_elements(By.XPATH, "//div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/span")
#commingSoonDay = driver.find_element(By.XPATH, "//div[4]/div/div[3]/div[i]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div/span")
#commingSoonHours = driver.find_element(By.XPATH, "//div[4]/div/div[3]/div[i]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div/span")
#commingSoonMinutes = driver.find_element(By.XPATH, "//div[4]/div/div[3]/div[i]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[3]/div/span")
count_comingsoon = 0
for a in comingSoon:
    if 'Coming Soon' in a.text:
        print(a.text)
        count_comingsoon += 1
    #elif '' in i.text:
for b in APR:
    print(b.text)
for c in coin:
    print(c.text)
    



