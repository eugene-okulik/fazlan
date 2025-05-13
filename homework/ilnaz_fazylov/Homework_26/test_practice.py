import random
from playwright.sync_api import Page
from faker import Faker

fake = Faker('en_US')


def remove_footer(page: Page):
    try:
        page.locator('#fixedban').wait_for(state='visible', timeout=5000)
        page.evaluate("document.querySelector('#fixedban')?.remove()")
        page.locator('footer').wait_for(state='visible', timeout=5000)
        page.evaluate("document.querySelector('footer')?.remove()")
    except TimeoutError:
        pass


def test_fill_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form', timeout=60000)
    page.wait_for_selector('#firstName')
    remove_footer(page)

    # Имя
    page.locator('#firstName').fill(fake.first_name())

    # Фамилия
    page.locator('#lastName').fill(fake.last_name())

    # Email
    page.locator('#userEmail').fill(fake.email())

    # Пол (Male)
    page.locator(f"label[for='gender-radio-{random.randint(1, 3)}']").click()

    # Мобильный номер
    page.locator('#userNumber').fill(fake.numerify(text="##########"))

    # Дата рождения
    page.evaluate("""
        const input = document.getElementById('dateOfBirthInput');
        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        nativeInputValueSetter.call(input, '03 Jan 1990');
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """)

    # Предмет
    subjects = ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce',
                'Accounting', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']

    subject_input = page.locator('#subjectsInput')
    subject_input.fill(random.choice(subjects))
    page.wait_for_selector('#subjectsInput')
    subject_input.press('Tab')

    # Хобби
    for i in range(1, random.randint(2, 4)):
        page.locator(f"label[for='hobbies-checkbox-{i}']").click()

    # Адрес
    page.locator('#currentAddress').fill(fake.address())

    # Заполнение поля "State"
    state_dropdown = page.locator('#state')
    state_dropdown.click()
    state_dropdown.locator('text=Haryana').click()

    # Заполнение поля "City"
    city_dropdown = page.locator('#city')
    city_dropdown.click()
    city_dropdown.locator('text=Panipat').click()

    # Submit
    page.locator('#submit').click()
