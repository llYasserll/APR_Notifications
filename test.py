from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()

driver.get("https://www.gate.io/es/startup-mining")
driver.maximize_window()
time.sleep(5)
print(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/div").text)

driver.quit()