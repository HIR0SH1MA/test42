import configparser
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read the configuration file
config = configparser.ConfigParser()
config.read("config.ini")

# Set up the browser and the wait
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Uncomment this line if you want to use a headless browser
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# Open the website and wait for it to load
driver.get(config["Website"]["url"])
wait.until(EC.visibility_of_element_located((By.NAME, "username")))

# Fill in the registration form
try:
    username = driver.find_element_by_name("username")
    username.send_keys(config["Registration"]["username"])
    password = driver.find_element_by_name("password")
    password.send_keys(config["Registration"]["password"])
    email = driver.find_element_by_name("email")
    email.send_keys(config["Registration"]["email"])
    
    # Random delay to simulate human behavior
    time.sleep(random.uniform(0.5, 1.5))
    
    # Additional point 1: Fill in the "First Name" and "Last Name" fields
    first_name = driver.find_element_by_name("first_name")
    first_name.send_keys(config["Registration"]["first_name"])
    last_name = driver.find_element_by_name("last_name")
    last_name.send_keys(config["Registration"]["last_name"])
    
    # Additional point 2: Select a random value from the "Country" drop-down list
    country_dropdown = driver.find_element_by_name("country")
    country_options = country_dropdown.find_elements_by_tag_name("option")
    country_options.pop(0)  # Remove the first option which is a dummy value
    random_country = random.choice(country_options)
    random_country.click()
    
    # Additional point 3: Check the "Terms and Conditions" checkbox
    terms_checkbox = driver.find_element_by_name("terms")
    terms_checkbox.click()
    
    # Additional point 4: Submit the form by pressing the "Enter" key
    submit_button = driver.find_element_by_name("submit")
    submit_button.send_keys(Keys.RETURN)
    
    # Random delay to simulate human behavior
    time.sleep(random.uniform(1.5, 2.5))
    
    # Check if the registration was successful
    success_message = driver.find_element_by_class_name("success-message")
    if success_message.is_displayed():
        print("Registration successful!")
    else:
        print("Registration failed!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
