import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://localhost/litecart/admin/login.php?redirect_url=%2Flitecart%2Fadmin%2F")

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("admin")
password.send_keys("admin")

driver.find_element_by_name("login").click()

driver.quit()
