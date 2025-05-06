import pytest
import random
from faker import Faker
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker('en_US')

subjects = ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce',
            'Accounting', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']

hobbies = ['Sports', 'Reading', 'Music']


@pytest.fixture(scope='session')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get('https://demoqa.com/automation-practice-form#google_vignette')
    remove_footer(chrome_driver)
    scroll_page_down(chrome_driver)
    yield chrome_driver
    chrome_driver.quit()


def remove_footer(driver):
    wait = WebDriverWait(driver, 1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#fixedban')))
    driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
    driver.execute_script("document.getElementById('fixedban').style.display = 'none';")


def scroll_page_down(driver):
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")


def fill_form(driver):
    # Имя
    driver.find_element(By.ID, "firstName").send_keys(fake.first_name())

    # Фамилия
    driver.find_element(By.ID, "lastName").send_keys(fake.last_name())

    # Email
    driver.find_element(By.ID, "userEmail").send_keys(fake.email())

    # Пол (Male)
    driver.find_element(By.CSS_SELECTOR, f"label[for='gender-radio-{randint(1, 3)}']").click()

    # Мобильный номер
    driver.find_element(By.ID, "userNumber").send_keys(fake.numerify(text="##########"))

    # Дата рождения
    driver.execute_script("""
        const input = document.getElementById('dateOfBirthInput');
        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        nativeInputValueSetter.call(input, '03 Jan 1990');
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """)

    # Предмет
    subject_input = driver.find_element(By.ID, "subjectsInput")
    subject_input.send_keys(random.choice(subjects))
    subject_input.send_keys(Keys.RETURN)

    # Хобби
    for i in range(1, randint(2, 4)):
        driver.find_element(By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{i}']").click()

    # Адрес
    driver.find_element(By.ID, "currentAddress").send_keys(fake.address())

    # State
    driver.find_element(By.ID, "react-select-3-input").send_keys("Haryana")
    driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.RETURN)

    # City
    driver.find_element(By.ID, "react-select-4-input").send_keys("Panipat")
    driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.RETURN)

    # Submit
    driver.find_element(By.ID, "submit").click()

    result_table = driver.find_elements(By.XPATH, '//div[@class="table-responsive"]//td')
    values = [element.text for element in result_table]
    return values


def pars_submit_data(driver):
    values = fill_form(driver)
    keys = values[::2]  # Четные индексы (0, 2, 4): ключи
    vals = values[1::2]  # Нечетные индексы (1, 3, 5): значения
    result_dict = dict(zip(keys, vals))
    return result_dict


def test_print_result(driver):
    print()
    for field, value in pars_submit_data(driver).items():
        print(f'{field}: {value}')
