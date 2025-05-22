from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Setup driver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

# Define a function to select sort option and wait
def sort_and_wait(option_text):
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text(option_text)
    print(f"Sorted by: {option_text}")
    time.sleep(4)

# 1. A to Z
sort_and_wait("Name (A to Z)")

# 2. Z to A
sort_and_wait("Name (Z to A)")

# 3. Price (low to high)
sort_and_wait("Price (low to high)")

# 4. Price (high to low)
sort_and_wait("Price (high to low)")

time.sleep(3)

# Close browser
driver.quit()




