from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Replace 'YOUR_WEBSITE_URL' with the URL of the website you want to open
website_url = 'YOUR_WEBSITE_URL'
# Replace 'YOUR_BUTTON_CLASS' with the class name of the button you want to click
button_class = 'YOUR_BUTTON_CLASS'

# Function to initialize the WebDriver
def initialize_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=775,563")
    return webdriver.Chrome(options=options)

# Function to perform the initial interactions and return the driver instance and button element
def initial_interactions(driver):
    driver.get(website_url)
    try:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, button_class)))
        return button
    except TimeoutException:
        print("Button not found.")
        return None

# Function to perform the desired actions
def automate(driver, button):
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(2)
        button.click()
        time.sleep(5)
        driver.refresh()
    except Exception as e:
        print("Error:", e)

# Main function
def main():
    driver = initialize_driver()
    try:
        button = initial_interactions(driver)
        if button:
            while True:
                automate(driver, button)
                time.sleep(2100)  # 35 minutes = 35 * 60 seconds
                driver.refresh()
                button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, button_class)))
                time.sleep(2)  # Wait for the page to load completely
                driver.execute_script("window.focus();")
    except KeyboardInterrupt:
        print("Program stopped manually.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
