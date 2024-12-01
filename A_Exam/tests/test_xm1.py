from selenium.webdriver.support import expected_conditions as EC  # Ensure this is imported correctly

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    """
    Pytest fixture to set up and tear down the Selenium WebDriver.
    Configures the WebDriver to ignore SSL certificate errors.
    """
    # Set up Chrome options to handle SSL certificate issues
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--start-maximized")  # Maximize the browser

    # Set up the WebDriver service
    service = Service('../driver/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver  # Provide the WebDriver to the test
    driver.quit()  # Ensure the browser is closed after the test


def test_google(driver):
    # driver = webdriver.Chrome()  # Replace with the driver for your browser if not Chrome
    # driver.maximize_window()

    try:
        # Navigate to Google
        driver.get("https://www.google.com/")

        # Find the search bar using XPath and type "Selenium WebDriver"
        search_bar = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
        search_bar.send_keys("Selenium WebDriver")
        search_bar.send_keys(Keys.ENTER)  # Simulate Enter key

        # Wait for results to load
        time.sleep(3)

        # Take a screenshot of the results page
        driver.save_screenshot("results.png")
        print("Screenshot saved as 'results.png'")
    finally:
        # Close the browser
        driver.quit()

def test_dropdown(driver):
    try:
        # Navigate to the Formstone dropdown demo page
        driver.get("https://formstone.it/components/dropdown/demo/")

        # Wait for the dropdown to be visible and clickable
        wait = WebDriverWait(driver, 10)
        dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='demo_groups-dropdown-selected']")))

        # Click the dropdown button to open the menu
        dropdown_button.click()
        time.sleep(3)

        # Wait for the dropdown options to load and select an option by visible text
        option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='demo_groups-dropdown']//button[@role='option'][normalize-space()='Three']")))
        option.click()

        # Print the selected option to the console
        selected_option = "Three"  # This is hardcoded since we know what we selected
        print(f"Selected option: {selected_option}")
        time.sleep(5)

    finally:
        # Close the browser
        driver.quit()




