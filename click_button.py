from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

# Replace 'YOUR_WEBSITE_URL' with the URL of the website you want to open
website_url = 'YOUR_WEBSITE_URL'
# Replace 'YOUR_BUTTON_CLASS' with the class name of the button you want to click
button_class = 'YOUR_BUTTON_CLASS'

# Function to perform the desired actions
def automate():
    # Open the website
    driver.get(website_url)
    while True:
        try:
            # Wait for the button to be clickable
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, button_class)))
            # Find the parent element (in this case, the body)
            parent_element = driver.find_element(By.TAG_NAME, 'body')
            # Find the button element within the parent element
            button = parent_element.find_element(By.CLASS_NAME, button_class)
            # Scroll the button into view
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            # Click the button
            button.click()
            time.sleep(5)  # Wait for 5 seconds before retrying
            # refresh the page
            driver.refresh()
            break
        except (TimeoutException, ElementClickInterceptedException):
            print("Button not clickable. Retrying...")
            # If button not clickable, refresh the page and try again
            driver.refresh()
            time.sleep(5)  # Wait for 5 seconds before retrying

# Setting up the Chrome driver
driver = webdriver.Chrome()

# Infinite loop to run the automation until stopped manually
try:
    while True:
        automate()
        # Sleep for 35 minutes
        time.sleep(2100)  # 35 minutes = 35 * 60 seconds
except KeyboardInterrupt:
    print("Program stopped manually.")
finally:
    # Close the browser window
    driver.quit()
