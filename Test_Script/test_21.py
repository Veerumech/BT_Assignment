from POM.ProductPage import *
from Generic.verify_title import *

# Test 2.1

# Input data
product_order = [1, 2, 4, 5, 3]    # order of products adding to cart


def test_21(setup):
    driver = setup
    verify_title("Typescript React Shopping cart", driver)
    p = ProductPage(driver)
    prod = p.bt_add_to_cart_multi(product_order)
    prod_name = prod[0]
    prod_price = prod[1]
    p.cart_bt()
    p.verify_cart_order(prod_name)
    p.verify_cart_prod_pricelist(prod_price)
