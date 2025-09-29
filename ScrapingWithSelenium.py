from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")
time.sleep(3)

# Enter keyword
keyword = "restaurants in Mumbai"
search_box = driver.find_element(By.ID, "searchboxinput")
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Scroll to load more results
scrollable_div = driver.find_element(By.XPATH, "//div[@role='feed']")
for _ in range(5):  # adjust number for more results
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
    time.sleep(2)

# Extract listings
listings = driver.find_elements(By.XPATH, "//a[contains(@href, '/place/')]")

for l in listings:
    name = l.get_attribute("aria-label")
    link = l.get_attribute("href")
    print(name, link)

driver.quit()
