# Web Automation with Selenium

This Python script automates web interactions using Selenium. It opens a specified website, finds a specific button by its class name, and clicks it every 35 minutes while refreshing the page before each click.

## Prerequisites

- Python 3.x installed on your system. You can download it from [here](https://www.python.org/downloads/).
- Selenium library installed. You can install it via pip:
  ```
  pip install selenium
  ```
- Chrome WebDriver installed. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your system PATH.

## Usage

1. Clone or download this repository to your local machine.

2. Open the `click_button.py` file in a text editor.

3. Replace `'YOUR_WEBSITE_URL'` with the URL of the website you want to automate.

4. Replace `'YOUR_BUTTON_CLASS'` with the class name of the button you want to click.

5. Save the changes.

6. Open a terminal or command prompt.

7. Navigate to the directory containing the `click_button.py` file.

8. Run the script using the following command:
   ```
   python click_button.py
   ```

9. The script will open the specified website, find and click the specified button every 35 minutes, and refresh the page before each click. It will continue running until you stop it manually.

## Notes

- Make sure to keep the terminal or command prompt window open while the script is running.
- You can stop the script manually by pressing `Ctrl + C` in the terminal or command prompt.

---
