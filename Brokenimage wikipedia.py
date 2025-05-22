from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Start Chrome browser
driver = webdriver.Chrome()
driver.get("https://demoqa.com/broken")
driver.maximize_window()

# Find all image elements
images = driver.find_elements(By.TAG_NAME, "img")

# List to store broken image URLs
broken_images = []

# Check each image
for img in images:
    src = img.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)

# Print results
if broken_images:
    print("Broken Images Found:")
    for url in broken_images:
        print(url)
else:
    print("No broken images found.")

# Close browser
driver.quit()