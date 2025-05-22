from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/')
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, 'a')
hrefs = [link.get_attribute('href') for link in links]

print(f'Total links: {len(hrefs)}')

for href in hrefs:
    if href and href.startswith('http'):
        try:
            response = requests.get(href)
            if response.status_code >= 400:
                print(f'Broken link: {href} (Status: {response.status_code})')
        except Exception as e:
            print(f'Failed to access link: {href}, Exception: {e}')
    else:
        print(f'Skipping: {href}')

driver.quit()





