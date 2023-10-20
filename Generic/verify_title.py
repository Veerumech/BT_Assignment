from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Generic.screenshot import *
from Generic.Logs import *

def verify_title(title, driver):
    wait = WebDriverWait(driver, 10)
    try:
        logg("info", "checking title")
        wait.until(EC.title_is(title))
    except:
        logg("error", "Title not matches")
        take_screenshot(driver)
        raise Exception ("Title Not matches")

def verify_cart_order(loc, eCartOrder, driver):
    wait = WebDriverWait(driver, 10)
    try:
        logg("info", "checking order of cart")
        wait.until(EC.text_to_be_present_in_element(loc, eCartOrder))
    except:
        logg("error", "Order of cart is not matching")
        take_screenshot(driver)
        raise Exception ("Order of cart is not matching")


# def verify_size_value(loc, etext, driver):
#     wait = WebDriverWait(driver, 10)
#     try:
#         logg("info", "checking text")
#         wait.until(EC.(loc,etext))
#     except:
#         logg("error", "Text not matches")
#         take_screenshot(driver)
#         raise Exception ("Text Not matches")





