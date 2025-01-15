from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

edge_options = Options()
edge_options.add_argument("--headless")

driver = webdriver.Edge(options=edge_options)

driver.get("https://www.gate.io/es/startup-mining")
driver.maximize_window()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/div"))
    )
    print(element.text)
except Exception as e:
    print("Error:", e)

driver.quit()