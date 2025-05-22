from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser and go to IMDb
driver = webdriver.Chrome()
driver.get("https://www.imdb.com/")
driver.maximize_window()
time.sleep(2)

# List of movies to search
movies = ["Interstellar", "King Kong", "End Game", "Karate Kid", "Finding Dory"]

# Loop through each movie
for movie in movies:
    # Search movie
    search_box = driver.find_element(By.ID, "suggestion-search")
    search_box.clear()
    search_box.send_keys(movie)
    driver.find_element(By.ID, "suggestion-search-button").click()
    time.sleep(4)

# Close browser
driver.quit()




