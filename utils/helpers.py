from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.chrome.service import Service
import time
CHROME_BINARY_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# Configuración del WebDriver para Chrome en modo headless . 
# def get_driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.implicitly_wait(10)
#     return driver
def get_driver():
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = CHROME_BINARY_PATH
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    return driver
def login_saucedemo(driver):
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Esperar a que la página cargue después del login