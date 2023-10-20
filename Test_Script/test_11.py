from POM.ProductPage import *
from Generic.verify_title import *
from time import sleep

# Test 1.1

#input data
input1 = ['S', 'M']  # product size button

def test_11(setup):
    driver = setup
    verify_title("Typescript React Shopping cart", driver)
    p = ProductPage(driver)
    p.bt_size(input1)
    p.bt_add_to_cart_all()
    p.cart_bt()
    p.verify_filter_size(input1)



