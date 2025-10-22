import pytest
from selenium.webdriver.common.by import By
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.helpers import login_saucedemo, get_driver

@pytest.fixture(scope="session")
# Configuración del driver de Selenium para las pruebas.    
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
# Test que verifica el inicio de sesión exitoso en SauceDemo, validando que la url contenga /inventory.html y que el titulo sea Products.
def test_login(driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text
    assert titulo == "Products"
    driver.save_screenshot("login_exitoso.png")   
    time.sleep(1)
# Test para verificar que el catálogo de productos se carge correctamente en donde se pueda encontra en la pagina el elemento inventory_list.
def test_catalogo(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_list")
    assert len(products) > 0
    driver.save_screenshot("catalogo_pagina.png")
    time.sleep(1)
# Test para verificar que se puede agregar un producto al carrito de compras y se verifique se agregue correctamente.
def test_carrito(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0 
    products[0].find_element(By.TAG_NAME, "button").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1"
    driver.save_screenshot("carrito_item.png")
    time.sleep(2) 