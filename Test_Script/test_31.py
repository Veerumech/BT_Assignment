from POM.ProductPage import *
from Generic.verify_title import *


product_order = [1, 2, 4, 5, 3]    # order of products adding to cart

def test_31(setup):
    driver = setup
    verify_title("Typescript React Shopping cart", driver)
    p = ProductPage(driver)
    p.bt_add_to_cart_multi(product_order)
    cart_count = len(product_order)
    p.cart_bt()
    e_cart_price = p.product_price_order_cart()
    p.verify_cart_count(cart_count)
    p.verify_cart_price(e_cart_price)
    p.clear_all_prod_cart()
    p.verify_cart_count(0)
    p.verify_cart_price(0)

