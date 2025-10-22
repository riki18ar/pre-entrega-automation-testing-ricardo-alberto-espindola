import pytest
from selenium.webdriver.common.by import By
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helpers import login_saucedemo, get_driver

@pytest.fixture(scope="session")    
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
def test_login(driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text
    assert titulo == "Products"   
    time.sleep(1)
def test_catalogo(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_list")
    assert len(products) > 0
    time.sleep(1)
def test_carrito(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0 
    products[0].find_element(By.TAG_NAME, "button").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1"
    time.sleep(2) 