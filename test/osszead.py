from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("//Users//agnessrancsik//Selenium//Masodikora_1030//test//chromedriver")
driver.get("https://srancsika.github.io/firstproject/")


driver = webdriver.Chrome()
driver.get("https://srancsika.github.io/firstproject/")
driver.find_element(By.ID, "elsoAdat").send_keys("1")
driver.find_element(By.ID, "masodikAdat").send_keys("2")

header_text = driver.find_element(By.XPATH, "//h1").text
assert header_text == "Számológép"

driver.find_element(By.ID, "gomb").click()

driver.close()