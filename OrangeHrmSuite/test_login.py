import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.fixture(scope="module")
def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
    chrome_options.add_argument("--disable-infobars")  # Disable the info bar
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--incognito")  # Open browser in incognito mode  
    chrome_driver_path = "/usr/local/bin/chromedriver"  # Replace with your ChromeDriver path
    service = Service(chrome_driver_path)
    driver=webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(setup_browser):
    driver=setup_browser

    # Open the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Wait for the page to load
    time.sleep(2)

    # Locate username and password input fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Enter the login credentials
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")

    # Submit the form by simulating pressing ENTER
    password_field.send_keys(Keys.RETURN)

    # Wait for login to complete (adjust time depending on your internet speed)
    time.sleep(5)

      # Verify successful login
    try:
        driver.implicitly_wait(5)
        # Check if dashboard is displayed after login
        assert "Dashboard" in driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div/div/span/h6").text
        print("Login test passed.")
        pytest.exitcode = 0  # Set exit code to 0 for success
    except AssertionError:
        print("Login test failed.")
        pytest.exitcode = 1  # Set exit code to 1 for failure
        raise  # Re-raise the exception for pytest to handle

if __name__ == "__main__":
    pytest.main()
