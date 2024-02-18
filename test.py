from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl


book = openpyxl.open('ConnAutoTest.xlsx', read_only=True)

sheet = book.active

print(sheet[1] [0].value)

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://staging.connectable.site/login")

try:

    inpWork = driver.find_element(By.XPATH, '//input[@placeholder="Workspace"]')

    inpWork.send_keys('testing3')

    inpMail = driver.find_element(By.XPATH, '//input[@placeholder="E-mail"]')

    inpMail.send_keys('t2@gmail.com')

    inpPass = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')

    inpPass.send_keys('111111')

    btnLog = driver.find_element(By.XPATH, '//div[text()="Log in"]')
    btnLog.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="page-block mood-block col"]')))

    #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="page-block mood-block col"]')))

    moodBlock = driver.find_element(By.XPATH, '//div[@class="page-block mood-block col"]')
    par = moodBlock.get_attribute('innerText')
    print(par)
    time.sleep(2)
except:
    print('Not element mood block')
finally:
    driver.quit()