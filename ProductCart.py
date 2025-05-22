from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(4)

# Add 5 products
product_ids = [
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-onesie"
]
time.sleep(3)
for pid in product_ids:
    driver.find_element(By.ID, pid).click()
    time.sleep(3)

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(3)

# Check items count in cart
items = driver.find_elements(By.CLASS_NAME, "cart_item")
print(f"Items in cart: {len(items)}")

time.sleep(4)

driver.quit()
