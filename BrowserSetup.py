from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class BrowserSetup:
    # This class sets up the initial browser settings to get into the game.
    def __init__(self, url_open):
        self.url_to_open = url_open  # URL to the cookie clicker game.
        self.driver = None  # The selenium driver.

        self.set_browser_up()  # Construct the function to run on startup.

    def set_browser_up(self):
        # This defines the driver, opens the browser, maximizes it and clicks through the language selection.

        # Define Selenium Driver.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.url_to_open)

        # Maximize the Window
        self.driver.maximize_window()

        # Wait 5 Seconds for page to load.
        time.sleep(5)

        # Select English as the language
        english_button = self.driver.find_element(By.ID, value="langSelect-EN")
        english_button.click()

        # Wait 5 seconds for page to load after clicking language.
        time.sleep(5)
