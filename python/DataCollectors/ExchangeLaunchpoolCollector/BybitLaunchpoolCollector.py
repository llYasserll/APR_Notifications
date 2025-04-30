from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import logging

import time

driver = webdriver.Edge()

driver.get("https://www.bybit.com/es-419/trade/spot/launchpool")
driver.maximize_window()
time.sleep(6)

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%H:%M:%S'
)

elements_earntokens=len(driver.find_elements(By.XPATH, "(//div[contains(@class, 'LaunchPoolPage')])[1]/div[3]/div[contains(@class,'NoEndActivites')]"))
elements=len(driver.find_elements(By.XPATH, "(//div[contains(@class, 'LaunchPoolPage')])[1]/div[3]/div[contains(@class,'NoEndActivites')]"))

i=0

while i < elements_earntokens:
    
    #pool = driver.find_element(By.XPATH, f"(//div[contains(@class, 'LaunchPoolPage')])[1]/div[3]/div[contains(@class,'NoEndActivites')][{i+1}]/div[2]/div/div[2]/div[2]/div[{j+1}]/div[1]/div[1]/div/div[1]/div[1]")
    #apr = driver.find_element(By.XPATH, f"(//div[contains(@class, 'LaunchPoolPage')])[1]/div[3]/div[contains(@class,'NoEndActivites')][{i+1}]/div[2]/div/div[2]/div[2]/div[{j+1}]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div")
    #logging.info(pool)

    elements_token= len(driver.find_elements(By.XPATH, f"(//div[contains(@class, 'LaunchPoolPage')])[1]/div[3]/div[contains(@class,'NoEndActivites')][{i+1}]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[1]"))
    j=0
    while j < elements_token:
        token = driver.find_element(By.XPATH, f"(//div[contains(@class, 'LaunchPoolPage')])[1]/div[3]/div[contains(@class,'NoEndActivites')][{i+1}]/div[2]/div/div[2]/div[2]/div[{j+1}]/div[1]/div[1]/div[1]/div[1]/div[1]")
        j+=1
        print(f"token -> {token.text}" )
    
    #print(f"pool -> {pool.text}")
    #print(f"apr -> {apr.text}")
    i+=1






##


