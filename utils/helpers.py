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

# Config del driver de Selenium para Google Chrome con opciones personalizadas.
def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = CHROME_BINARY_PATH
    prefs = {
        # Evita que aparezca el popup de guardar contraseñas
        "credentials_enable_service": False,
        # Desactiva la gestión de contraseñas segura del navegador.
        "profile.password_manager_leak_detection": False,
    }
    chrome_options.add_experimental_option("prefs", prefs)  
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    return driver
# Función para iniciar sesión en la pagina web de SauceDemo utilizando Selenium con espera implicita.  
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
    # Manejo de alertas si aparecen después del inicio de sesión. 
    try:
        time.sleep(0.5)
        Alert(driver).accept()
        print("Alert accepted")
    except Exception as e:
        pass
    time.sleep(2)