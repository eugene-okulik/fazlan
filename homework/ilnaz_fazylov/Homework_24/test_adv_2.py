import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    accept_cookie(chrome_driver)
    yield chrome_driver
    chrome_driver.quit()


def accept_cookie(driver):
    wait = WebDriverWait(driver, 10)
    accept_btn = wait.until(EC.element_to_be_clickable((By.ID, 'accept-btn')))
    accept_btn.click()


def move_to_item_and_click(driver):
    wait = WebDriverWait(driver, 10)
    items = driver.find_elements(By.XPATH, '//*[@class="item product product-item"]')
    for elem in range(1, len(items)):
        item = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f'//*[@class="item product product-item"][{elem}]')))
        add_to_cart_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"(//button[@title='Add to Cart'])[{elem}]")))
        ActionChains(driver).move_to_element(item).click(add_to_cart_btn).perform()
        is_item = check_item_in_cart(driver)
        if is_item:
            item_name = driver.find_element(By.XPATH, f'(//*[@class="product name product-item-name"])[{elem}]').text
            return item_name


def check_item_in_cart(driver):
    wait = WebDriverWait(driver, 10)
    is_item = 1
    try:
        error = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'The requested qty')]"))).text
        if error:
            driver.back()
            is_item = 0
    except Exception:
        return is_item


def check_add_item_in_cart(driver, item_name):
    wait = WebDriverWait(driver, 10)
    success_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'You added')]"))).text
    counter = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'counter-number')))
    counter.click()
    item_in_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="product-item-name"]'))).text
    assert success_text == f'You added {item_name} to your shopping cart.', 'Text is incorrect'
    assert item_name == item_in_cart, f"Expected '{item_name}' in cart, but got '{item_in_cart}'"


def test_add_item_in_cart(driver):
    item_name = move_to_item_and_click(driver)
    check_add_item_in_cart(driver, item_name)
