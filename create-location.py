from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/agnessrancsik/Selenium/Masodikora_1030/chromedriver")
driver.get("http://learnwebservices.com/locations/server")
driver.find_element(By.ID, "nameInput").send_keys("Hello Python")

title = driver.find_element(By.XPATH, "//h1").text
print(title)

driver.close()

assert title == "Locations"