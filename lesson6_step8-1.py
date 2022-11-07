from selenium import webdriver
import time

try:
	link = "http://suninjuly.github.io/registration2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	elements = browser.find_elements(by='xpath',
	                                 value="//input[contains(@placeholder, 'email') or contains(@placeholder, 'first "
	                                       "name') or contains(@placeholder, 'last name') ]")
	for element in elements:
		element.send_keys("xxxxxx")
	# Отправляем заполненную форму
	button = browser.find_element(by='css selector', value="button.btn")
	button.click()

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)

	# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element(by='tag name', value='h1')
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text

	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта и количество заполненных
	# полей равно трем
	assert "Congratulations! You have successfully registered!" == welcome_text and len(elements) == 3

finally:
	time.sleep(3)
	browser.quit()
