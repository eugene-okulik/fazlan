import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    yield chrome_driver
    chrome_driver.quit()


def test_choose_language(driver):
    start_button = driver.find_element(By.XPATH, '//div[@id="start"]/button')
    start_button.click()
    wait = WebDriverWait(driver, 7)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish')))
    finish_text = driver.find_element(By.CSS_SELECTOR, '#finish').text
    assert finish_text == 'Hello World!', 'Текст не совпадает'
