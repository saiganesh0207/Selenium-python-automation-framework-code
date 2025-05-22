from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

time.sleep(2)


upload = driver.find_element(By.ID, "uploadfile")


upload.send_keys(r"C:\Users\SaiGaneshChintha(Qua\Desktop\pexels-crisdip-35358-128756.jpg")

time.sleep(5)
driver.quit()




