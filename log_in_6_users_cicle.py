from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

base_url = 'https://www.saucedemo.com/'
driver = webdriver.Chrome(
    executable_path='C:\\Py\\pythonSelenium\\chromedriver.exe')  # Выбрали, с каким браузером будем работать
driver.get(base_url)
driver.maximize_window()


def click_some_element(path):
    element_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    element_click.click()


def enter_some_text(path, text):
    element_enter_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    element_enter_text.send_keys(text)


def wanna_text(path):
    element_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    return element_text.text


users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
password_all = 'secret_sauce'
blocked =[]
"""Login"""
for login in users:
    print(login + ' is using.')
    enter_some_text('//input[@id="user-name"]', login)
    enter_some_text('//input[@id="password"]', password_all)
    click_some_element('//input[@id="login-button"]')
    time.sleep(3)
    try:
        element = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        print('User is blocked.')
        driver.refresh()
        time.sleep(3)
    except NoSuchElementException as exception:
        assert wanna_text('//div[@id="header_container"]/div[2]/span') == 'Products'
        print('User log in!')
        click_some_element('//button[@id = "react-burger-menu-btn"]')
        click_some_element('//a[@id = "logout_sidebar_link"]')
        time.sleep(3)
print('All users are tested.')