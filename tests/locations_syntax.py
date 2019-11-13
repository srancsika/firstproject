from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/agnessrancsik/Selenium/Masodikora_1030/tests/chromedriver")
driver.get("http://www.learnwebservices.com/locations/server")


print("A Locations alkalmazásban olvasd be Dobogókő koordinátáját! Milyen a típusa?")
coordinates = driver.find_element(By.XPATH, "//tr[td[text() = 'Dobogókő']]/td[3]").text
print(type(coordinates))
print(coordinates)


print("A Locations alkalmazásban olvasd be Alattyán azonosítóját! Írd ki a típusát!")
city_id = driver.find_element(By.XPATH, "//tr[td[text() = 'Alattyán']]/td[1]").text
print(type(city_id))
print(city_id)


print("A Locations alkalmazásban olvasd be a 9277 azonosítójú település nevét! Írd ki a típusát!")
city_name = driver.find_element(By.XPATH, "//tr[td[text() = '9277']]/td[2]").text
print(type(city_name))
print(city_name)


print("Próbáld meg Bakonybánk azonosítóját egész számmá konvertálni, és írd ki a változó típusát!")
bakonybank = int(driver.find_element(By.XPATH, "//tr[td[text() = 'Bakonybánk']]/td[1]").text)
print(type(bakonybank))
print(bakonybank)


print("Próbáld meg Zsámbék koordinátáját egész számmá konvertálni, és írd ki a változó típusát!")
zsambek = driver.find_element(By.XPATH, "//tr[td[text() = 'Zsámbék']]/td[3]").text
zsambek_lat = zsambek[0:11]
zsambek_lon = zsambek[12:]
zsambek_lat = float(zsambek_lat)
zsambek_lon = float(zsambek_lon)
print(type(zsambek_lat))
print(type(zsambek_lon))
print(zsambek_lat)
print(zsambek_lon)


line = "windows 2000; Windows Server 2000; kétezer"
parts = line.split(";")
print (parts)
print(parts[0])
print(parts[1])
print(parts[2])


print ("Kérdezd le Velence és Báta azonosítóját, majd add össze!")
velence_id = driver.find_element(By.XPATH, "//tr[td[text() = 'Velence']]/td[1]").text
bata_id = driver.find_element(By.XPATH, "//tr[td[text() = 'Báta']]/td[1]").text
print (int(velence_id) + int(bata_id))


print("Keresd ki a 9876 azonosítójú település nevét, majd írd ki az első három karakterét!")
kilencnyolchethat = driver.find_element(By.XPATH, "//tr[td[text() = '9876']]/td[2]").text
print(kilencnyolchethat[:3])


print("Keresd ki a 9898 azonosítójú település nevét, majd írd ki visszafele!")
vissza = driver.find_element(By.XPATH, "//tr[td[text() = '9898']]/td[2]").text
print(vissza[::-1])


print("Keresd ki a 9742 azonosítójú település nevét, majd írd ki a hosszát, hogy hány karakterből áll!")
kilenchetnegyketto = driver.find_element(By.XPATH, "//tr[td[text() = '9742']]/td[2]").text
print(len(kilenchetnegyketto))


print("Keresd ki a 11115 azonosítójú település nevét, majd írd ki a csupa nagy és csupa kisbetűvel!")
tizenegyketszermeg5 = driver.find_element(By.XPATH, "//tr[td[text() = '11115']]/td[2]").text
print(tizenegyketszermeg5.upper())
print(tizenegyketszermeg5.lower())


print("Keresd ki a 11116, 11117, 11118 azonosítójú település nevét, majd írd ki egymástól kötőjelekkel elválasztva!")
tizenhat = driver.find_element(By.XPATH, "//tr[td[text() = '11116']]/td[2]").text
tizenhet = driver.find_element(By.XPATH, "//tr[td[text() = '11117']]/td[2]").text
tizennyolc = driver.find_element(By.XPATH, "//tr[td[text() = '11118']]/td[2]").text
print(str(tizenhat) + "-" + str(tizenhet) + "-" + str(tizennyolc))


print("Írd ki Tolmács koordinátáit, de space-szel elválasztva, és tizedespont helyett tizedes vesszővel!")
tolmacs = driver.find_element(By.XPATH, "//tr[td[text() = 'Tolmács']]/td[3]").text
coords = tolmacs.split(",")
coords[0] = coords[0].replace(".",";")
coords[1] = coords[1].replace(".",";")
print(str(coords[0]) + ' ' + str(coords[1]))


print("Keresd ki a Tiszakerecseny és Tiszarád koordinátáit! Add értékül négy lebegőpontos változóval!")
kerecs = driver.find_element(By.XPATH, "//tr[td[text() = 'Tiszakerecseny']]/td[3]").text
rad = driver.find_element(By.XPATH, "//tr[td[text() = 'Tiszarád']]/td[3]").text
kerecs_coords = kerecs.split(",")
rad_coords = rad.split(",")
kerecs1 = float(kerecs_coords[0])
kerecs2 = float(kerecs_coords[1])
rad1 = float(rad_coords[0])
rad2 = float(rad_coords[1])
print(kerecs1)
print(kerecs2)
print(rad1)
print(rad2)


print("Az előző két településnek vond ki egymásből a szélességi és hosszúsági koordinátáit!")
print (kerecs1 - rad1)
print(kerecs2 - rad2)


print("Írd ki, hogy a 11262 azonosítójú településben szerepel-e a margit szó (True vagy False!")
margit = driver.find_element(By.XPATH, "//tr[td[text() = '11262']]/td[2]").text
print("margit" in margit)
print(margit)


driver.close()