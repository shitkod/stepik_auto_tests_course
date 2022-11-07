from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".form-control.first[required]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".form-control.second[required]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".form-control.third[required]")
    input3.send_keys("IP@mail.ru")
    input4 = browser.find_element_by_css_selector(".second_block .form-control.first")
    input4.send_keys("89456784567")
    input5 = browser.find_element_by_css_selector(".second_block .form-control.second")
    input5.send_keys("Samara")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()