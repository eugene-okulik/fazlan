from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as eco_loc
import allure
from playwright.sync_api import expect


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Check items quantity by locator')
    def check_items_quantity(self, quantity):
        items = self.find_element(eco_loc.ITEMS)
        expect(items, 'Not all items are loaded').to_have_count(quantity)

    @allure.step('Check text for added item to compare by text')
    def check_text_add_item_to_compare(self, text):
        success_compare = self.find_element(eco_loc.SUCCESS_COMPARE)
        expect(success_compare).to_be_visible()
        expect(success_compare, f"Expected text '{text}', but got '{success_compare}'").to_have_text(text)

    @allure.step('Check add item to compare by item_name')
    def check_add_item_to_compare(self, item_name):
        compare_item = self.find_element(eco_loc.COMPARE_ITEM)
        expect(compare_item, f"Expected '{item_name}' for compare, but got '{compare_item}'").to_have_text(item_name)

    @allure.step('Check add item without options by text')
    def check_add_item_without_options(self, text):
        warning_message = self.find_element(eco_loc.WARNING_ADD)
        expect(warning_message).to_be_visible()
        expect(warning_message, f"Expected text '{text}', but got '{warning_message}'").to_have_text(text)

    @allure.step('Move mouse to item card')
    def move_mouse_to_item_card(self):
        return self.move_mouse_to_element(eco_loc.ITEM_CARD)

    @allure.step('Get item name')
    def get_item_name(self):
        return self.get_text_of_(eco_loc.ITEM)

    @allure.step('Add item to compare')
    def add_item_to_compare(self):
        expect(self.find_element(eco_loc.ADD_TO_COMPARE)).to_be_enabled()
        return self.click(eco_loc.ADD_TO_COMPARE)

    @allure.step('Add item to cart')
    def add_item_to_cart(self):
        expect(self.find_element(eco_loc.ADD_TO_CART)).to_be_enabled()
        return self.click(eco_loc.ADD_TO_CART)
