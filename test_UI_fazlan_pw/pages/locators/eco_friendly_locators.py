from random import randint

ITEMS = "//*[@class='item product product-item']"
item_number = randint(1, 12)
ITEM_CARD = f"//*[@class='item product product-item'][{item_number}]"
ITEM = f"(//*[@class='product name product-item-name'])[{item_number}]"
COMPARE_ITEM = "//*[@class='product-item-name']"
ADD_TO_COMPARE = f"(//a[@title='Add to Compare'])[{item_number}]"
ADD_TO_CART = f"(//button[@title='Add to Cart'])[{item_number}]"
WARNING_ADD = "//*[contains(text(), 'You need')]"
SUCCESS_COMPARE = "//*[contains(text(), 'You added product')]"
