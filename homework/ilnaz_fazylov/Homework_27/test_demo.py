from playwright.sync_api import Page, expect, BrowserContext


def test_accept_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda alert: alert.accept())
    page.get_by_role('link', name='Click').click()
    result = page.locator('#result')
    expect(result).to_contain_text('Ok')


def test_tabs(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(link).to_be_enabled()


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator("#colorChange")
    element_handle = button.element_handle()
    page.wait_for_function(
        "(el) => el.classList.contains('text-danger')",
        arg=element_handle
    )
    expect(button).to_contain_class("text-danger")
    button.click()
