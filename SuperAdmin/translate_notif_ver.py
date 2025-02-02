
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from random import randint
from selenium.webdriver.common.action_chains import ActionChains
@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.get("https://staging.connectable.site/")
    #driver.get("https://connectable.site/")
    driver.get("https://intranetable.team/")
    driver.implicitly_wait(50)
    return driver



def test_create_notification(page):

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys('w.project.portal3@gmail.com')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    page.find_element(By.XPATH, '//div[@class="btn f-centered pointer icon outline text-center small"]').click()

    element = page.find_element(By.XPATH, '(//div[@class="f-grow-1"])[18]')

    element.execute_script("arguments[0].scrollIntoView(true);", element)

    element.click()

    page.find_element(By.XPATH, "//div[text()='Настройки оповещений']").click()

    for i in range(1, 2):

        element = page.find_element(By.XPATH, f'(//div[@class="ant-collapse-header"])[{i}]')  # выбор уведомления для перевода

        element.execute_script("arguments[0].scrollIntoView(true);", element)

        element.click()

        inp_element_3 = page.find_element(By.XPATH, '(//input)[3]') #Заголовок

        text_3 = inp_element_3.get_attribute('value')

        text_area_1 = page.find_element(By.XPATH, '(//textarea)[1]')# Текст краткого шаблона

        area_element_1 = text_area_1.get_attribute('value')

        text_area_2 = page.find_element(By.XPATH, '(//textarea)[2]')# Текст полного шаблона

        area_element_2 = text_area_2.get_attribute('value')

        inp_element_4 = page.find_element(By.XPATH, '(//input)[4]')# Параметры

        text_4 = inp_element_4.get_attribute('value')

        file = open('data/notific.txt', 'a')
        file.write(text_3 + '\n')
        file.write(area_element_1 + '\n')
        file.write(area_element_2 + '\n')
        file.write(text_4 + '\n')
        file.close()