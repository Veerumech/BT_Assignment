from POM.ProductPage import *
from Generic.verify_title import *
from time import sleep


def test_12(setup):
    driver = setup
    verify_title("Typescript React Shopping cart", driver)
    p = ProductPage(driver)
    p.bt_size(['S'])
    p.bt_add_to_cart_all()
    p.cart_bt()
    p.verify_filter_size(['S'])
    driver.refresh()
    p.bt_size(['M'])
    p.bt_add_to_cart_all()
    p.cart_bt()
    p.verify_filter_size(['M'])
    driver.refresh()
    p.bt_size(['S', 'M'])
    p.bt_add_to_cart_all()
    p.cart_bt()
    p.verify_filter_size(['M', 'S'])
