from pages.base_page import BasePage
import allure
from playwright.sync_api import expect
from pages.locators import sale_locators as sale_loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step('Check deals quantity not')
    def check_deals_quantity_not_(self, quantity):
        deals = self.find_element(sale_loc.DEALS)
        expect(deals, 'Not all deals are loaded').not_to_have_count(quantity)

    @allure.step('Click to gear link')
    def click_gear_link(self):
        return self.click(sale_loc.GEAR)
