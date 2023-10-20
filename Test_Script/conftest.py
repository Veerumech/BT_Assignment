from selenium.webdriver import Chrome
import pytest
from Generic.Logs import *
from time import sleep


@pytest.fixture
def setup():
    logg("info", "Launching Browser")
    driver = Chrome()
    logg("info", "Entering URL")
    driver.get("https://react-shopping-cart-67954.firebaseapp.com/")
    driver.maximize_window()
    sleep(3)
    yield driver
    logg("info", "Closing Browser")
    driver.close()


