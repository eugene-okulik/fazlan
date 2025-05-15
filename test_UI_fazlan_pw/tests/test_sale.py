import pytest


@pytest.mark.smoke
def test_sale_page_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_title('Sale')


@pytest.mark.smoke
def test_sale_has_deals(sale_page):
    sale_page.open_page()
    sale_page.check_deals_quantity_not_(0)


@pytest.mark.regress
def test_gear_link(sale_page):
    sale_page.open_page()
    sale_page.click_gear_link()
    sale_page.check_page_title('Gear')
