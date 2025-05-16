import pytest
from playwright.sync_api import BrowserContext
from pages.base_page import BasePage
from pages.register_page import RegisterPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1280, 'height': 1080})
    yield page
    page.close()


@pytest.fixture()
def base_page(page):
    return BasePage(page)


@pytest.fixture()
def register_page(page):
    return RegisterPage(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
