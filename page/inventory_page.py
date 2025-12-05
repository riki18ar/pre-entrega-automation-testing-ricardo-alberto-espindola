from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    # Constante que representa la URL actual de la página de inventario.
    URL_CURRENT = "/inventory.html"
    MENU_BUTTON_ID = (By.ID, "react-burger-menu-btn")
    LINK_LOGOUT_ID = (By.ID, "logout_sidebar_link")
    def __init__(self, driver):
        self.driver = driver
    # Verifica si el usuario está en la página de inventario.
    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url
    
    
    def logout(self):
        self.driver.find_element(*self.MENU_BUTTON_ID).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LINK_LOGOUT_ID)).click()   