from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get('https://www.imdb.com/')
driver.maximize_window()

images = driver.find_elements(By.TAG_NAME, 'img')
broken_images = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}

for image in images:
    src = image.get_attribute('src')
    if src:
        try:
            response = requests.get(src, headers=headers)
            if response.status_code != 200:
                broken_images.append(src)
                print(f'Broken image found: {src} (Status: {response.status_code})')
        except Exception as e:
            print(f'Error checking image {src}: {e}')

if broken_images:
    print('\nList of broken images:')
    for broken_image in broken_images:
        print(broken_image)
else:
    print('No broken images found.')

driver.quit()
