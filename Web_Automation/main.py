from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class WebAutomation:
    def __init__(self):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chrome_options.add_argument("--start-maximized")
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        # Set up the Chrome WebDriver service
        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Open login page
        print("Navigating to login page...")
        self.driver.get('https://demoqa.com/login')

        # Wait for username and password fields to load
        username_field = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Enter credentials and log in
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)
        print("Login successful!")

    def fill_form(self):
        # Navigate to the form section
        print("Navigating to the form section...")
        element = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        element.click()

        form_btn = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="item-0"]')))
        self.driver.execute_script("arguments[0].click();", form_btn)

        # Fill the form fields
        print("Filling the form...")
        full_name = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.ID, "userName")))
        full_name.send_keys("HUba LUBA")
        print("Entered full name successfully.")

        user_email = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.ID, "userEmail")))
        user_email.send_keys("valusageonly@gmail.com")
        print("Entered email successfully.")

        user_address = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
        user_address.send_keys("America, England")
        print("Entered current address successfully.")

        permanent_address = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
        permanent_address.send_keys("America, England")
        print("Entered permanent address successfully.")

        # Submit the form
        submit_btn = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.ID, 'submit')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        self.driver.execute_script("arguments[0].click();", submit_btn)
        print("Form submitted successfully!")

    def download(self):
        # Navigate to the download section
        print("Navigating to the download section...")
        download_area = WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="item-7"]')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", download_area)
        self.driver.execute_script("arguments[0].click();", download_area)

        # Wait for the download button and click it
        download_btn = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.ID, 'downloadButton')))
        self.driver.execute_script("arguments[0].click();", download_btn)
        print("File downloaded successfully!")

    def close(self):
        # Close the browser after the user has finished
        input("Press Enter to close the automated window...")
        self.driver.quit()
        print("Browser closed successfully!")

# Example usage
if __name__ == "__main__":
    web_automation = WebAutomation()
    web_automation.login("username", "password")
    web_automation.fill_form()
    web_automation.download()
    web_automation.close()
