from Generic.decorator import *
from time import sleep


@verify_element
def click_element(driver, loc):
    driver.find_element(*loc).click()

@verify_element
def text_element(driver, loc):
    text = driver.find_element(*loc).text
    return text

@verify_element
def text_elements(driver, loc):
    eles = driver.find_elements(*loc)
    list = []
    for ele in eles:
        text = ele.text
        list.append(text)
    return list
