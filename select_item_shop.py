from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url = 'https://www.saucedemo.com/'
driver = webdriver.Chrome(
    executable_path='C:\\Py\\pythonSelenium\\chromedriver.exe')  # Выбрали, с каким браузером будем работать, где его драйвер
driver.get(base_url)
driver.maximize_window()


def click_some_element(path):
    element = driver.find_element(By.XPATH, path)
    element.click()


def enter_some_text(path, text):
    element = driver.find_element(By.XPATH, path)
    element.send_keys(text)


def wanna_text(path):
    element = driver.find_element(By.XPATH, path)
    return element.text


login_st_us, password_all = 'standard_user', 'secret_sauce'
items = ('1 - Sauce Labs Bike Light, 9.99 \n2 - Sauce Labs Bolt T-Shirt, 15.99 \n3 - Sauce Labs Onesie, 7.99 \n4 - '
         'Test.allTheThings() T-Shirt (Red), 15.99 \n5 - Sauce Labs Backpack, 29.99 \n6 - Sauce Labs Fleece Jacket, '
         '49.99')
"""Login"""
enter_some_text('//input[@id="user-name"]', login_st_us)
enter_some_text('//input[@id="password"]', password_all)
click_some_element('//input[@id="login-button"]')
print('Speak Friend and Enter! \nPlease select one of the following items and enter the item number:', items)
num_item = input()
while num_item not in ['1', '2', '3', '4', '5', '6']:
    print('You may have made a mistake. Try entering the number again.', items)
    num_item = input()
num_item = int(num_item) - 1
path_name_item = f'//a[@id="item_{num_item}_title_link"]'
print(path_name_item)
nums = {5: 1, 1: 2, 2: 3, 6: 4, 3: 5, 4: 6} #небольшая подсказка для ориентирования по ценам на сайте
"""Info product"""
product_value = wanna_text(path_name_item)
product_price = float(wanna_text('(//div[@class="inventory_item_price"])[' + str(nums[num_item + 1]) + ']').replace('$', ''))
"""Add to cart"""
click_some_element('(//button[@class="btn btn_primary btn_small btn_inventory "])[' + str(nums[num_item + 1]) + ']')
print('Select product')
"""Let's go to the Cart"""
click_some_element('//a[@class="shopping_cart_link"]')
print('Go to the cart')
"""In the cart"""
cart_product_value = wanna_text(path_name_item)
cart_product_1_price = float(wanna_text('//div[@class="item_pricebar"]/div').replace('$', ''))
assert product_value == cart_product_value
print("В корзине тот же товар")
assert product_price == cart_product_1_price
print("В корзине товар за те же деньги ")
"""Checkout"""
click_some_element('//button[@id="checkout"]')
print('Click Checkout')
"""Select User Info"""
faker = Faker('en_US')
enter_some_text('//input[@name="firstName"]', faker.first_name())
enter_some_text('//input[@name="lastName"]', faker.last_name())
enter_some_text('//input[@id="postal-code"]', faker.postcode())
time.sleep(5) #чтобы посмотреть, что введено
click_some_element('//input[@id="continue"]')
"""Finish """
finish_value_product = wanna_text(path_name_item)
finish_price_product = float(wanna_text('//div[@class="summary_info"]/div[6]').replace('Item total: $', ''))
assert product_value == finish_value_product
print("В заказе тот же товар")
assert product_price == finish_price_product
print("В заказе товар за те же деньги ")
