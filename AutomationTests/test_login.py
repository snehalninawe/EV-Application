from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.implicitly_wait(10)

    driver.get("https://account.evgo.com/login")

    driver.find_element(By.NAME, "email").send_keys(
        "test@example.com"
    )

    driver.find_element(By.NAME, "password").send_keys(
        "test123"
    )
    time.sleep(2)

    driver.find_element(
        By.XPATH,
        "//span[2]"
    ).click()

    assert "login" not in driver.current_url.lower()

    driver.quit()