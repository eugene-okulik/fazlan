import pytest
from data.register import user
from data.expected_results import SUCCESS_MESSAGES, VALIDATE_MESSAGES


@pytest.mark.smoke
def test_register_page_title(register_page):
    register_page.open_page()
    register_page.check_page_title('Create New Customer Account')


@pytest.mark.smoke
def test_register_form_visible(register_page):
    register_page.open_page()
    register_page.check_register_form_visible()


@pytest.mark.smoke
def test_successful_register(register_page):
    register_page.open_page()
    register_page.fill_register_form(user['first_name'], user['last_name'], user['email'], user['password'])
    register_page.submit()
    register_page.check_text_success_register(SUCCESS_MESSAGES['register'])
    register_page.check_contact_information(user['first_name'], user['last_name'], user['email'])


@pytest.mark.regress
def test_short_password_validation(register_page):
    register_page.open_page()
    register_page.fill_register_form(user['first_name'], user['last_name'], user['email'], "1234567")
    register_page.submit()
    register_page.check_text_short_password(VALIDATE_MESSAGES['weak_password'])
