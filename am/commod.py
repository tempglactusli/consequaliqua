from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

try:
    # Replace 'driver' with your actual WebDriver instance name
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
    agree_button = wait.until(EC.element_to_be_clickable((By.ID, 'agree_btn')))
    agree_button.click()
except TimeoutException:
    print("The element was not clickable within the given time.")
