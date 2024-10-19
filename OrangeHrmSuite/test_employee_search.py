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

# Login to OrangeHRM
def test_search_employee(setup_browser):
    driver=setup_browser
    driver.implicitly_wait(5)
    # Open the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Locate username and password input fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Enter the login credentials
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")

    # Submit the form by simulating pressing ENTER
    password_field.send_keys(Keys.RETURN)

   
    # Navigate to the PIM section (Personal Information Management)
    driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']").click()

   

    # Find the employee search input (by Name or Employee ID) and perform a search
    search_employee_name_field = driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/input")
    search_employee_name_field.send_keys("Rahul Mulge Patil")  # Replace with any employee name to search

    # Click the search button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

   

    # Verify if the search results contain the expected employee name
    search_results = driver.find_elements(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div")
    search_name_results = driver.find_element(By.XPATH,"//div[contains(text(),'Rahul Mulge')]")

    if len(search_results) > 0:
        print("Employee search test passed: Employee found in the search results!")
    else:
        print("Employee search test failed: No employee found.")


      # Verify successful login
    try:
        driver.implicitly_wait(5)
        # Check if dashboard is displayed after login
        assert len(search_results) > 0
        pytest.exitcode = 0  # Set exit code to 0 for success
    except AssertionError:
        print("Login test failed.")
        pytest.exitcode = 1  # Set exit code to 1 for failure
        raise  # Re-raise the exception for pytest to handle

if __name__ == "__main__":
    pytest.main()



