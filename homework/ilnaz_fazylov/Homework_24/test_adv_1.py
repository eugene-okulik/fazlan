import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest


class Products:
    URL = "https://www.demoblaze.com/index.html"
    PRODUCT_LINK = (By.CLASS_NAME, "hrefch")
    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")
    PRODUCT_NAME = (By.CLASS_NAME, "name")
    CART_LINK = (By.CSS_SELECTOR, "#cartur")
    product_in_cart_NAME = (By.XPATH, "//td[2]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_product_in_new_tab(self):
        self.driver.get(self.URL)
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_LINK))
        products = self.driver.find_elements(*self.PRODUCT_LINK)
        product = random.choice(products)
        product_name = product.text
        # self.scroll_to_element(product)
        # self.wait.until(EC.element_to_be_clickable(product))
        while len(self.driver.window_handles) < 2:
            ActionChains(self.driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
        return product_name

    def switch_to_new_tab(self):
        # WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def add_product_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        add_button.click()
        self.accept_alert()
        return self.driver.find_element(*self.PRODUCT_NAME).text

    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        Alert(self.driver).accept()

    def close_new_tab_and_return(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        product_in_cart = self.wait.until(EC.presence_of_element_located(self.product_in_cart_NAME))
        return product_in_cart.text

    def check_product_in_cart(self, added_product, product_in_cart):
        assert added_product in product_in_cart, f"Expected '{added_product}' in cart, but got '{product_in_cart}'"


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_add_product_in_cart(driver):
    product = Products(driver)
    product.open_product_in_new_tab()
    product.switch_to_new_tab()
    added_product = product.add_product_to_cart()
    product.close_new_tab_and_return()
    product_in_cart = product.open_cart()
    product.check_product_in_cart(added_product, product_in_cart)
