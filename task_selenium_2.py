import datetime
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
base_url = 'https://demoqa.com/date-picker'
driver = webdriver.Chrome(executable_path='C:\\Py\\pythonSelenium\\chromedriver.exe') #Выбрали, с каким браузером будем работать, где его драйвер
driver.get(base_url)
driver.maximize_window()

time.sleep(2)

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()

now_date = datetime.datetime.now()
end_date = now_date + datetime.timedelta(days=10) #добавили 10 дней, чтобы самостоятельно не считать дни в месяце и прочее
end_date = end_date.strftime("%d") #сохранили себе только строковый день
print(end_date)
date_10 = driver.find_element(By.XPATH, "//div[contains(@class, '" + end_date + "')]") #класс содержит число
date_10.click()