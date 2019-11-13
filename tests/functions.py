from selenium import webdriver
from selenium.webdriver.common.by import By


#print ("Írj egy függvényt, ami paraméterül kap egy nevet, és kiírja a település koordinátáját!")
def print_coords_by_name(name):
    xpath = "//tr[td[text() = 'name']]/td[3]".replace("name",name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)

def print_id_by_name(name):
    xpath = "//tr[td[text() = 'name']]/td[1]".replace("name", name)
    id = driver.find_element(By.XPATH, xpath).text
    print(id)

#print("Írj egy függvényt, ami paraméterül kap egy nevet, és visszaadja a település koordinátáját!")
def return_coords_by_name(name):
    xpath = "//tr[td[text() = 'name']]/td[3]".replace("name",name)
    coords = driver.find_element(By.XPATH, xpath).text
    return coords

#print("Írj egy függvényt, mely paraméterül kap egy azonosítót, és kikeresi a nevet!")
def print_name_by_id(id):
    xpath = "//tr[td[text() = 'id']]/td[2]".replace("id",str(id))
    name = driver.find_element(By.XPATH, xpath).text
    print(name)

#print("Írj egy függvényt, mely paraméterül kap egy azonosítót, és kikeresi a koordinátáját!")
def print_coords_by_id(id):
    xpath = "//tr[td[text() = 'id']]/td[3]".replace("id", str(id))
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)

#print("Írj egy függvényt, mely a paraméterül kapott értékekkel (név, koordináta kitölti az űrlapot, és felvesz egy kedvenc helyet!")
def create_location(name, id):
    driver.get("http://www.learnwebservices.com/locations/server")
    driver.find_element(By.ID, "nameInput").click()
    driver.find_element(By.ID, "nameInput").send_keys(name)
    driver.find_element(By.ID, "coordsInput").send_keys(id)
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    assert driver.find_element(By.CSS_SELECTOR, ".alert").text == "Location has saved."
    return(print_id_by_name(name))


driver = webdriver.Chrome("/Users/agnessrancsik/Selenium/Masodikora_1030/tests/chromedriver")
driver.get("http://www.learnwebservices.com/locations/server")

print_coords_by_name("Törökszentmiklós")
print_name_by_id(8734)
print_coords_by_id(8734)
create_location("Kukac", "1,1")