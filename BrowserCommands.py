from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.imdb.com/")
time.sleep(4)


search_box = driver.find_element(By.ID, "suggestion-search")
search_box.send_keys("Inception")
driver.find_element(By.ID, "suggestion-search-button").click()
time.sleep(2)


driver.find_element(By.XPATH, "//section//ul//li//a").click()
time.sleep(2)


driver.back()
print("Went back to search results page")
time.sleep(3)

driver.forward()
print("Went forward to movie detail page")
time.sleep(3)

driver.refresh()
print("Page refreshed")
time.sleep(2)


driver.minimize_window()
print("Window minimized")
time.sleep(3)

driver.maximize_window()
print("Window maximized")
time.sleep(4)


driver.quit()
print("Browser closed")

