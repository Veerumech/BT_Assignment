from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Generic.Logs import *
from Generic.screenshot import take_screenshot
from time import sleep

def verify_element(func):
    def inner(*args, **kwargs):
        wait = WebDriverWait(args[0], 15)
        logg("info", "verifying element in DOM")
        # args[0].implicitly_wait(10)
        assert wait.until(EC.visibility_of_element_located(args[1])), take_screenshot()
        assert wait.until(EC.element_to_be_clickable(args[1])), take_screenshot()
        return func(*args, **kwargs)
    return inner




















