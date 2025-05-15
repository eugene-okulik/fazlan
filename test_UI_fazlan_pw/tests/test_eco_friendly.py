import pytest
from data.expected_results import WARN_MESSAGES


@pytest.mark.smoke
def test_eco_friendly_page_title(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_page_title('Eco Friendly')


@pytest.mark.smoke
def test_items_quantity(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_items_quantity(12)


@pytest.mark.smoke
def test_add_item_to_compare(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.reload_page()
    eco_friendly_page.move_mouse_to_item_card()
    eco_friendly_page.add_item_to_compare()
    item_name = eco_friendly_page.get_item_name()
    eco_friendly_page.check_text_add_item_to_compare(f'You added product {item_name} to the comparison list.')
    eco_friendly_page.check_add_item_to_compare(item_name)


@pytest.mark.regress
def test_add_item_to_cart_without_options(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.reload_page()
    eco_friendly_page.move_mouse_to_item_card()
    eco_friendly_page.add_item_to_cart()
    eco_friendly_page.check_add_item_without_options(WARN_MESSAGES['add_to_cart'])
