from playwright.sync_api import Page, expect, Locator
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the page')
    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    @allure.step('Reload the page')
    def reload_page(self):
        return self.page.reload()

    @allure.step('Check the page title')
    def check_page_title(self, title):
        expect(self.page).to_have_title(title)

    def wait_for_visible_element(self, locator):
        element = self.find_element(locator)
        return element.wait_for(state='visible', timeout=5000)

    @allure.step('Find element by locator')
    def find_element(self, locator: tuple) -> Locator:
        return self.page.locator(locator)

    @allure.step('Click element by locator')
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step('Move mouse to element by locator')
    def move_mouse_to_element(self, locator):
        return self.find_element(locator).hover()

    @allure.step('Get text of element by locator')
    def get_text_of_(self, locator):
        return self.find_element(locator).inner_text()
