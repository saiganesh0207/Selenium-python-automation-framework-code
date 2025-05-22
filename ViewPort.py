from selenium import webdriver
import time


driver = webdriver.Chrome()

# Common device viewports (width x height)
viewports = [
    (1920, 1080),   # Full HD Desktop
    (1366, 768),    # Laptop
    (1440, 900),    # MacBook Pro
    (1536, 864),    # Desktop HD+
    (1280, 720),    # HD Ready
    (1024, 768),    # iPad (Landscape)
    (768, 1024),    # iPad (Portrait)
    (414, 896),     # iPhone XR/11/11 Pro Max
    (375, 812),     # iPhone X/XS
    (375, 667),     # iPhone 6/7/8
    (360, 800),     # Android large phone
    (320, 568),     # iPhone SE
]

driver.get('https://www.imdb.com/')

try:
    for width, height in viewports:
        print(f"Setting window size to: {width}x{height}")
        driver.set_window_size(width, height)
        time.sleep(2)  # Pause to observe each viewport

finally:
    print("Closing browser...")
    driver.quit()
