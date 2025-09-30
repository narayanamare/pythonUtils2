from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")
time.sleep(3)

# Step 1: Enter search keyword
keyword = "restaurants in Mumbai"
search_box = driver.find_element(By.ID, "searchboxinput")
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Step 2: Scroll through results to load more
scrollable_div = driver.find_element(By.XPATH, "//div[@role='feed']")
for _ in range(3):  # scroll multiple times to load more
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
    time.sleep(2)

# Step 3: Collect all business listings
listings = driver.find_elements(By.XPATH, "//a[contains(@href, '/place/')]")

print(f"Found {len(listings)} listings")

# Step 4: Loop through and simulate a click
for i, listing in enumerate(listings[:5]):  # limit to first 5 for demo
    print(f"\nVisiting listing {i+1}...")

    try:
        listing.click()   # simulate user click
        time.sleep(4)     # wait for profile panel to load

        # Extract details from the side panel
        try:
            name = driver.find_element(By.XPATH, "//h1").text
        except:
            name = "N/A"

        try:
            address = driver.find_element(By.XPATH, "//button[@data-item-id='address']").text
        except:
            address = "N/A"

        try:
            phone = driver.find_element(By.XPATH, "//button[@data-item-id='phone']").text
        except:
            phone = "N/A"

        print("Name:", name)
        print("Address:", address)
        print("Phone:", phone)

    except Exception as e:
        print("Error visiting listing:", e)

    # Go back to the results panel
    driver.back()
    time.sleep(3)

driver.quit()
