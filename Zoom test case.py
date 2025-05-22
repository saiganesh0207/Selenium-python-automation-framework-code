from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.imdb.com/")
driver.maximize_window()
time.sleep(4)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scrolled down")
time.sleep(4)

driver.execute_script("window.scrollTo(0, 0);")
print("Scrolled up")
time.sleep(4)

driver.execute_script("document.body.style.zoom='125%'")
print("Zoomed In")
time.sleep(4)

driver.execute_script("document.body.style.zoom='75%'")
print("Zoomed Out")
time.sleep(4)

driver.execute_script("document.body.style.zoom='100%'")
print("Reset Zoom")
time.sleep(4)

driver.quit()
