import re
import json
from playwright.sync_api import Page, Route, expect


def test_change_phone_name(page: Page):
    change_name = 'яблокофон 16 про'

    def change_phone_name(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = change_name
        body['body']['digitalMat'][0]['productName'] = change_name
        body['body']['digitalMat'][0]['familyTypes'][0]['tabTitle'] = change_name
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile('/shop/api/digital-mat'), change_phone_name)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('(//*[@class="rf-hcard-copy"])[1]').click()
    phone_name = page.locator("(//*[@id='rf-digitalmat-overlay-label-0'])[1]")
    expect(phone_name).to_have_text(change_name)
