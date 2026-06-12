from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_search_valid_station():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.evgo.com/find-a-charger/")

    time.sleep(3)

    # Search box
    search_box = driver.find_element(By.XPATH, "//input[@type='text']")

    search_box.send_keys("Mumbai")
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    
    
    driver.quit()
