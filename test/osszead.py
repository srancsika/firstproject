from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/agnessrancsik/Selenium/Masodikora_1030/chromedriver")
driver.get("https://srancsika.github.io/firstproject/")


class TestOsszeadas():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def test_osszeadas(self):
    self.driver.get("https://srancsika.github.io/firstproject/")
    self.driver.set_window_size(1226, 731)
    self.driver.find_element(By.ID, "elsoAdat").click()
    self.driver.find_element(By.ID, "elsoAdat").send_keys("1")
    self.driver.find_element(By.ID, "masodikAdat").click()
    self.driver.find_element(By.ID, "masodikAdat").send_keys("2")
    self.driver.find_element(By.ID, "gomb").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "Location has saved"