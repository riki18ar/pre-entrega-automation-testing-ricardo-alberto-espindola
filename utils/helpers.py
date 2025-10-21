from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.chrome.service import Service
#import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
CHROME_BINARY_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = CHROME_BINARY_PATH
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    return driver
def login_saucedemo(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user-name"))
    ).send_keys(USERNAME)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys(PASSWORD)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "login-button"))
    ).click()
    #driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    # driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    #driver.find_element(By.ID, "password").send_keys(PASSWORD)
    # driver.find_element(By.ID, "login-button").click()
    #time.sleep(2)  # Esperar a que la página cargue después del login