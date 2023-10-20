from POM.ProductPage import *
from Generic.verify_title import *
from time import sleep

# Test 1.2

# input data
input1 = ['S']          # product size button
input2 = ['M']          # product size button
input3 = ['S', 'M']     # product size button


def test_12(setup):
    driver = setup
    verify_title("Typescript React Shopping cart", driver)
    p = ProductPage(driver)
    p.bt_size(input1)
    p.bt_add_to_cart_all()
    p.cart_bt()
    p.verify_filter_size(input1)
    driver.refresh()
    p.bt_size(input2)
    p.bt_add_to_cart_all()
    p.cart_bt()
    p.verify_filter_size(input2)
    driver.refresh()
    p.bt_size(input3)
    p.bt_add_to_cart_all()
    p.cart_bt()
    p.verify_filter_size(input3)
