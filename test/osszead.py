from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/agnessrancsik/Selenium/Masodikora_1030/test/chromedriver")
driver.get("https://srancsika.github.io/firstproject/")

#driver.find_element(By.ID, "a-input").send_keys("1")
first_number=input("Elso szam?")
first_input_field = driver.find_element(By.ID, "a-input")
print(type(first_input_field))
#first_input_field.send_keys("4")
first_input_field.send_keys(first_number)
#first_input_field.screenshot("first-input.png")
second_number=input("Masodik szam?")
driver.find_element(By.ID, "b-input").send_keys(second_number)

driver.find_element(By.ID, "submit-button").click()
eredmeny = driver.find_element(By.ID, "result-input").get_attribute("value")

driver.save_screenshot("result.png")
print(eredmeny)
expected = str(int(first_number) + int(second_number))
print(expected)
assert eredmeny == expected