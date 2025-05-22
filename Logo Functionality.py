from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:

    driver.get("https://www.imdb.com/")
    time.sleep(3)


    search_box = driver.find_element(By.ID, "suggestion-search")
    search_box.send_keys("Titanic")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)


    logo_link = driver.find_element(By.ID, "home_img_holder")
    logo_link.click()
    time.sleep(3)


    if driver.current_url.startswith("https://www.imdb.com"):
        print("Test Passed: Navigated back to homepage after clicking IMDb logo.")
    else:
        print(f"Test Failed: Not redirected to homepage. Current URL: {driver.current_url}")

finally:
    driver.quit()
