import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def generate_text():
    length = random.randint(2, 25)
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_text


def test_id_name(driver):
    random_text = generate_text()
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_input = driver.find_element(By.NAME, 'text_string')
    text_input.send_keys(random_text)
    # text_input.send_keys(Keys.ENTER)
    text_input.submit()
    wait = WebDriverWait(driver, 3)
    text_output = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#result-text')))
    assert text_output.get_attribute('innerText') == random_text


# def test_placeholder(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     text_input = driver.find_element(By.CSS_SELECTOR, '.form-control')
#     assert text_input.get_attribute('placeholder') == 'Submit me'
