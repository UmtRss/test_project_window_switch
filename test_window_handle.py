from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

def test_window_switch():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")

    main_window = driver.current_window_handle

    driver.find_element(By.LINK_TEXT, "Click Here").click()

    windows = driver.window_handles
    for handle in windows:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    assert driver.title == "New Window"
    driver.quit()
