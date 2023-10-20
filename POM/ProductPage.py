from Generic.wrapper import *
from Generic.Logs import *
from Generic.screenshot import *

loc_size = {"XS" : ("xpath", "//div[@class='sc-bj2vay-1 hcyKTa']//span[.='XS']"),
        "S" : ("xpath", "//div[@class='sc-bj2vay-1 hcyKTa']//span[.='S']"),
        "M" : ("xpath", "//div[@class='sc-bj2vay-1 hcyKTa']//span[.='M']"),
        "ML" : ("xpath", "//div[@class='sc-bj2vay-1 hcyKTa']//span[.='ML']"),
        "L" : ("xpath", "//div[@class='sc-bj2vay-1 hcyKTa']//span[.='L']"),
        "XL" : ("xpath", "//div[@class='sc-bj2vay-1 hcyKTa']//span[.='XL']"),
        "XXL" : ("xpath", "//div[@class='sc-bj2vay-1 hcyKTa']//span[.='XXL']")}
def loc_product(index):
    return ("xpath", f"(//div[contains(@class,'sc-124al1g-2')]){[index]}//button")
def loc_product_name(index):
    return ("xpath",f"(//div[contains(@class,'sc-124al1g-2')]){[index]}/p")
def loc_product_price1(index):
    return ("xpath", f"(//div[contains(@class,'sc-124al1g-2')]){[index]}//button/..//div/p[1]/b[1]")
def loc_product_price2(index):
    return ("xpath", f"(//div[contains(@class,'sc-124al1g-2')]){[index]}//button/..//div/p[1]/span[1]")

loc_product_list = ("class name", "sc-124al1g-4.eeXMBo")
loc_bt_close = ("xpath", "//button[@class='sc-1h98xa9-0 gFkyvN']")
loc_cart_bt = ("class name", "sc-1h98xa9-0.gFkyvN")
loc_prod_size_in_cart = ("class name", "sc-11uohgb-3.gKtloF")
loc_cart_price = ("xpath", "//p[@class='sc-1h98xa9-9 jzywDV']")
loc_cart_order = ("xpath", "//div[@class='sc-11uohgb-0 hDmOrM']/div[1]/p[1]")
loc_plus_bt = ("xpath", "//button[.='+']")
loc_cart_product = ("xpath", "(//div[@class='sc-11uohgb-4 bnZqjD'])/p")
loc_prod_cart_price = ("xpath", "//div[@class='sc-11uohgb-4 bnZqjD']/p")
loc_cart_count = ("class name", "sc-1h98xa9-3.VLMSP")
loc_clear_prod_cart = ("xpath", "//button[@title='remove product from cart']")
loc_checkout = ("class name", "sc-1h98xa9-11.gnXVNU")


class ProductPage:
    def __init__(self,driver):
        self.driver = driver

    def bt_size(self, size):
        logg("info", "Clicking size button")
        for i in size:
            click_element(self.driver, loc_size[i])
            sleep(3)

    def prod_size_in_cart(self):
        logg("info", "Collecting product size in cart")
        text = text_elements(self.driver, loc_prod_size_in_cart)
        size = []
        for i in text:
            size.append((i.split())[0])
        return size

    def verify_filter_size(self, e_filter_size):
        logg("info", "Verifying filter size")
        a_prod_size_in_cart = self.prod_size_in_cart()
        a_prod_size = self.size_order_arrangement(a_prod_size_in_cart)
        e_prod_size = self.size_order_arrangement(e_filter_size)
        assert a_prod_size == e_prod_size, take_screenshot(self.driver)

    def size_order_arrangement(self, size_list):
        order = ['XS', 'S', 'M', 'ML', 'L', 'XL', 'XXL']
        list = []
        for i in order:
            if i in size_list:
                if i not in list:
                    list.append(i)
        return list

    def bt_add_to_cart_all(self):
        logg("info", "Adding all products to cart")
        products = text_elements(self.driver, loc_product_list)
        count = len(products)
        for i in range(count):
            self.bt_add_to_cart(i+1)
            self.bt_close()

    def bt_add_to_cart(self, index):
        logg("info", "Adding product to cart")
        click_element(self.driver, loc_product(index))

    def bt_close(self):
        logg("info", "Closing cart")
        click_element(self.driver, loc_bt_close)

    def product_price(self, index):
        logg("info", "Product price")
        a = text_element(self.driver, loc_product_price1(index))
        b = text_element(self.driver, loc_product_price2(index))
        amount = float(a) + float(b)
        return amount

    def cart_price(self):
        logg("info", "Total Cart price")
        cart_price = text_element(self.driver, loc_cart_price)
        new_price = cart_price.strip("$ ")
        return float(new_price)

    def product_name(self,index):
        logg("info", "product name")
        product_name = text_element(self.driver, loc_product_name(index))
        return product_name

    def product_name_order_cart(self):
        logg("info", "Product name in cart")
        products = text_elements(self.driver, loc_cart_order)
        return products

    def cart_bt(self):
        logg("info", "Clicking cart button")
        click_element(self.driver, loc_cart_bt)

    def plus_bt(self):
        logg("info", "Clicking plus button")
        click_element(self.driver, loc_plus_bt)

    def bt_add_to_cart_times(self, index, times):
        logg("info", f"Clicking add to cart button {times} times")
        for i in range(times):
            self.bt_add_to_cart(index)
            self.bt_close()
        return times

    def bt_plus_times(self, index, times):
        logg("info", f"Clicking plus button {times} times")
        for i in range(times):
            self.plus_bt()
        return times

    def verify_cart_price(self, e_total_price):
        logg("info", "Verifying cart price")
        print(self.cart_price())
        assert self.cart_price() == e_total_price, take_screenshot(self.driver)

    def bt_add_to_cart_multi(self, product_list):
        logg("info", "adding multiple product to cart")
        prod_name_list = []
        price_list = []
        for i in product_list:
            prod_name_list.append(self.product_name(i))
            price_list.append(self.product_price(i))
            self.bt_add_to_cart(i)
            self.bt_close()
        return prod_name_list, price_list

    def verify_cart_order(self,e_product_name_list):
        logg("info", "Verifying cart list order")
        cart_prod_name_list = self.product_name_order_cart()
        assert cart_prod_name_list == e_product_name_list, take_screenshot(self.driver)

    def prod_price_in_cart(self):
        price = text_elements(self.driver, loc_cart_product)
        price_int = []
        for i in price:
            price_int.append(float(i.strip('$ ')))
        return price_int

    def verify_cart_prod_pricelist(self, e_product_price_list):
        logg("info", "Verifying cart product price")
        cart_prod_price_list = self.prod_price_in_cart()
        assert cart_prod_price_list == e_product_price_list, take_screenshot(self.driver)

    def cart_count(self):
        logg("info", "cart count")
        cart_count = text_element(self.driver, loc_cart_count)
        return int(cart_count)

    def verify_cart_count(self, e_cart_count):
        logg("info", "Verifying cart count")
        a_cart_count = self.cart_count()
        assert a_cart_count == e_cart_count, take_screenshot(self.driver)

    def product_price_order_cart(self):
        logg("info", "Sum of individual product price in cart")
        products = text_elements(self.driver, loc_prod_cart_price)
        prod_price_cart = 0
        for prod in products:
            prod_price_cart = prod_price_cart + float(prod.strip("$ "))
        return prod_price_cart

    def clear_all_prod_cart(self):
        logg("info", "Removing product from cart")
        lent = self.cart_count()
        for i in range(lent):
            click_element(self.driver, loc_clear_prod_cart)

    def bt_checkout(self):
        logg("info", "Clicking checkout button")
        click_element(self.driver, loc_checkout)

    def verify_alert_checkout_price(self, e_cart_price):
        logg("info", "Verifying alert checkout price")
        alert = self.driver.switch_to.alert
        alert_text = (alert.text).split()
        alert_price = float(alert_text[4])
        alert.accept()
        assert alert_price == e_cart_price, take_screenshot()

