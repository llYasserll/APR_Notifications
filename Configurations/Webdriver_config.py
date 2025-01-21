from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    options=Options()
    
    options.add_argument("--headless")
    
    driver = webdriver.Edge(service=Service, options=Options)
    return driver
