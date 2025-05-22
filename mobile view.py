from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait = WebDriverWait(driver, 10)

# Add products to cart
product_ids = [
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-test.allthethings()-t-shirt-(red)"
]

for pid in product_ids:
    try:
        button = wait.until(EC.element_to_be_clickable((By.ID, pid)))
        button.click()
        print(f"Added product with ID: {pid}")
    except Exception as e:
        print(f"Could not add product with ID: {pid} — {e}")

# Open cart
cart_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
cart_link.click()

time.sleep(2)  # Wait for cart page to load fully

# Remove products one by one by clicking the "Remove" buttons in the cart
while True:
    try:
        remove_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']")))
        remove_btn.click()
        print("Removed one product")
        time.sleep(3)
    except:
        print("No more Remove buttons found, all products removed.")
        break

driver.quit()


