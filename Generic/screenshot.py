from datetime import datetime

def take_screenshot(driver):
    d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    driver.save_screenshot(f"../defects/{d}.png")

