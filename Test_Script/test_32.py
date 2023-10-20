from POM.ProductPage import *
from Generic.verify_title import *


product_order = [1, 2, 4]    # order of products adding to cart


def test_32(setup):
    driver = setup
    verify_title("Typescript React Shopping cart", driver)
    p = ProductPage(driver)
    p.bt_add_to_cart_multi(product_order)
    p.cart_bt()
    e_cart_price = p.cart_price()
    p.bt_checkout()
    p.verify_alert_checkout_price(e_cart_price)
    driver.refresh()
    p.cart_bt()
    p.verify_cart_count(0)
