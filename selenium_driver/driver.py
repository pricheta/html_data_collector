from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


selenium_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
