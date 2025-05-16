import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import register_locator as reg_loc
from pages.locators import exp_results_locators as exp_loc
from tests.data.register import user


class RegisterPage(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Fill register form by first_name, last_name, email, password')
    def fill_register_form(self, first_name, last_name, email, password):
        self.find_element(reg_loc.FIRST_NAME).fill(first_name)
        self.find_element(reg_loc.LAST_NAME).fill(last_name)
        self.find_element(reg_loc.EMAIL).fill(email)
        self.find_element(reg_loc.PASSWORD).fill(password)
        self.find_element(reg_loc.CONFIRM_PASSWORD).fill(password)

    @allure.step('Submit action')
    def submit(self):
        expect(self.find_element(reg_loc.SUBMIT)).to_be_visible()
        return self.click(reg_loc.SUBMIT)

    @allure.step('Check register form is visible')
    def check_register_form_visible(self):
        expect(self.find_element(reg_loc.FIRST_NAME)).to_be_visible()
        expect(self.find_element(reg_loc.LAST_NAME)).to_be_visible()
        expect(self.find_element(reg_loc.EMAIL)).to_be_visible()
        expect(self.find_element(reg_loc.PASSWORD)).to_be_visible()
        expect(self.find_element(reg_loc.CONFIRM_PASSWORD)).to_be_visible()

    @allure.step('Check text success register')
    def check_text_success_register(self, text):
        success_register = self.find_element(exp_loc.SUCCESS_REGISTER)
        expect(success_register, f"Expected '{text}' but got '{success_register}'").to_have_text(text)

    @allure.step('Check first_name, last_name, email in contact information')
    def check_contact_information(self, first_name, last_name, email):
        contact_information = self.find_element(reg_loc.CONTACT_INFO)
        expect(contact_information, f"Expected {user['first_name']} but got {first_name}").to_contain_text(first_name)
        expect(contact_information, f"Expected {user['last_name']} but got {last_name}").to_contain_text(last_name)
        expect(contact_information, f"Expected {user['email']} but got {email}").to_contain_text(email)

    @allure.step('Check text for short password')
    def check_text_short_password(self, text):
        weak_pass = self.find_element(reg_loc.PASSWORD_ERROR)
        expect(weak_pass, f"Expected '{text}' but got '{weak_pass}'").to_have_text(text)
