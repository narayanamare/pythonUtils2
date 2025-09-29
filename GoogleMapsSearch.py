from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (make sure you have ChromeDriver installed)
driver = webdriver.Chrome()

# Open Google Maps
driver.get("https://www.google.com/maps")

# Wait for page to load
time.sleep(3)

# Locate the search box
search_box = driver.find_element("id", "searchboxinput")

# Type your keyword
keyword = "restaurants near me"
search_box.send_keys(keyword)

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait to see results
time.sleep(5)

# Close browser
driver.quit()
