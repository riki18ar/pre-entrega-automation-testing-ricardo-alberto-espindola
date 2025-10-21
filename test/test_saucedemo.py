import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helpers import login_saucedemo, get_driver

@pytest.fixture(scope="session")    
def driver():
    # configuracion para consultar a selenium web driver.
    driver = get_driver()
    yield driver
    driver.quit()
def test_login(driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text
    assert titulo == "Products"   
    # login de usuario con username y password.
    # click en boton login.
    # redireccionar a la pagina de inventario.
    # verificar el titulo de la pagina de inventario.
    #def test_catalogo():
    # login con usuario y password.
    # click en boton login.
    # podamos verificar el titulo, pero del html del catalogo.
    # verificar si existen productos en la pagina y estan visibles.
    # verificar elementos importantes de la pagina.
    #def test_carrito():
    # login con usuario y password.
    # click en boton login.
    # redireccionar a la pagina del carrito de compras.
    # comprobar que el carrito aparezcan productos correctamente.