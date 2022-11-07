from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    link = "http://suninjuly.github.io/file_input.html"
    
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
#x_element = browser.find_element(By.ID, "input_value")
 #   x = x_element.text
  #  print(x)
   # y = calc(x)
    
    input = browser.find_element(By.NAME, "firstname")
    input.send_keys('d')
    
    input = browser.find_element(By.NAME, "lastname")
    input.send_keys('d')
    
    input = browser.find_element(By.NAME, "email")
    input.send_keys('ddddd@mail.ru')
    
    input_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 't.txt')           # добавляем к этому пути имя файла 
    input_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()