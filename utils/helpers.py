from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
CHROME_BINARY_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = CHROME_BINARY_PATH
    chrome_options.add_argument("--disable-save-password-bubble")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.popups": 0
    }
    chrome_options.add_experimental_option("prefs", prefs)  
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    return driver 
def login_saucedemo(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user-name"))
    ).send_keys(USERNAME)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys(PASSWORD)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "login-button"))
    ).click()
    time.sleep(2)
    try:
        time.sleep(0.5)
        Alert(driver).accept()
        print("Alert accepted")
    except Exception as e:
        pass
    time.sleep(2)