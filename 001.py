import os 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

print("Погодь, браузер ща запустица)")

options = Options()

options.headless = True

driver = webdriver.Firefox(options=options)

driver.get("https://www.youtube.com")
print("Браузер запущен, падажжи)")
time.sleep(3)
element_bar = driver.find_element(By.XPATH, """//input[@id="search"]""")
element_bar.send_keys(input("\nПоиск: "))

print("\n")

element_search_button = driver.find_element(By.XPATH, """//*[@id="search-icon-legacy"]""")
element_search_button.click()

time.sleep(3)

videos =  driver.find_elements(By.ID, "video-title")

ssilki = []

for i in range(0, len(videos)):
    ssilki.append(videos[i].get_attribute('href'))
    print(str(i) + ". " + videos[i].text)
    if i == 9:
        break

numssilki = int(input("Какое видео посмотришь (ответ цифрой): "))

comand = "vlc " + str(ssilki[numssilki])
os.system(comand)
