from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

import time

edge_options = Options()
#edge_options.add_argument("--headless")

driver = webdriver.Edge()

driver.get("https://launchpad.binance.com/es")
driver.maximize_window()
time.sleep(6)