import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get('https://www.qa-practice.com/elements/select/single_select')
    yield chrome_driver
    chrome_driver.quit()


def test_choose_language(driver):
    dropdown = driver.find_element(By.NAME, 'choose_language')
    language_select = Select(dropdown)

    languages = [language.text for language in language_select.options if language.get_attribute('value').strip()]
    selected_language = random.choice(languages)
    language_select.select_by_visible_text(selected_language)

    driver.find_element(By.ID, 'submit-id-submit').click()
    result_language = driver.find_element(By.CSS_SELECTOR, '#result-text').text
    assert selected_language == result_language, 'Выбранный язык не совпадает'
