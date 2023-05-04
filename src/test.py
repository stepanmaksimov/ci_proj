import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get("https://www.saucedemo.com/")

input_username = driver.find_element(By.XPATH, "//*[@id=\"user-name\"]")
input_password = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
login_button = driver.find_element(By.XPATH, "//*[@id=\"login-button\"]")

input_username.send_keys("standard_user")
input_password.send_keys("secret_sauce")
login_button.send_keys(Keys.RETURN)

title_text = driver.find_element(By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")
if title_text.text == "Products":
    print("Мы попали на главную страницу")
else:
    print("Ошибка поиска элемента")
