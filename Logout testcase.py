from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.ID, "login-button").click()

time.sleep(3)


driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(3)


driver.find_element(By.ID, "logout_sidebar_link").click()

time.sleep(3)

if "saucedemo.com" in driver.current_url and "login" in driver.current_url:
    print("Logout successful!")
else:
    print("Logout failed!")

driver.quit()

