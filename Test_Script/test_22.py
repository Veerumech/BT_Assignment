from POM.ProductPage import *
from Generic.verify_title import *

# Test 2.2

def test_22(setup):
    driver = setup
    verify_title("Typescript React Shopping cart", driver)
    p = ProductPage(driver)
    price = p.product_price(1)
    count = p.bt_add_to_cart_times(1, 3)   # index : product, times : quantity
    p.cart_bt()
    times = p.bt_plus_times(1, 2)           # index : product, times : quantity
    count = count + times
    e_new_price = price * count
    p.verify_cart_price(e_new_price)
