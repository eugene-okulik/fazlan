from playwright.sync_api import Page


def test_fill_form_auth(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('user')
    page.get_by_role('textbox', name='password').fill('pass')
    page.get_by_role('button', name='Login').click()
