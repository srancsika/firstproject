from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/agnessrancsik/Selenium/Masodikora_1030/tests/chromedriver")
driver.get("https://srancsika.github.io/firstproject/")

a_input = driver.find_element(By.ID, "a-input")
b_input = driver.find_element(By.ID, "b-input")
c_input = driver.find_element(By.ID, "c-input")

a_input.send_keys("2")
b_input.send_keys("3")
c_input.send_keys("4")

driver.find_element(By.ID, "calculate-button").click()
line = driver.find_element(By.XPATH, "//li[last()]")

assert line == "a = 2, b = 3, c = 4: Általános"

driver.save_screenshot("result.png")