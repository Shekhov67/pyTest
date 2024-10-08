from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from random import randint
from selenium.webdriver.common.action_chains import ActionChains
from googletrans import Translator

@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://staging.connectable.site/")
    #driver.get("https://connectable.site/")
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

    element = page.find_element(By.XPATH, '(//div[@class="ant-collapse-header"])[46]')

    element.execute_script("arguments[0].scrollIntoView(true);", element)

    element.click()

    inp_element_1 = page.find_element(By.XPATH, '(//input)[3]')

    text_1 = inp_element_1.get_attribute('value')

    text_area_1 = page.find_element(By.XPATH, '(//textarea)[1]')

    area_element_1 = text_area_1.get_attribute('value')

    text_area_2 = page.find_element(By.XPATH, '(//textarea)[2]')

    area_element_2 = text_area_2.get_attribute('value')

    inp_element_2 = page.find_element(By.XPATH, '(//input)[4]')

    text_2 = inp_element_2.get_attribute('value')
###########  EN
    translator = Translator()

    inp_trans_text_1_eng = translator.translate(text_1, src='ru', dest='en')

    print(inp_trans_text_1_eng.text)

    area_trans_text_1_eng = translator.translate(area_element_1, src='ru', dest='en')

    print(area_trans_text_1_eng.text)

    area_trans_text_2_eng = translator.translate(area_element_2, src='ru', dest='en')

    print(area_trans_text_2_eng.text)

    inp_trans_text_2_eng = translator.translate(text_2, src='ru', dest='en')

    print(inp_trans_text_2_eng.text)

    ##################UK

    inp_trans_text_1_uk = translator.translate(text_1, src='ru', dest='uk')

    print(inp_trans_text_1_uk.text)

    area_trans_text_1_uk = translator.translate(area_element_1, src='ru', dest='uk')

    print(area_trans_text_1_uk.text)

    area_trans_text_2_uk = translator.translate(area_element_2, src='ru', dest='uk')

    print(area_trans_text_2_uk.text)

    inp_trans_text_2_uk = translator.translate(text_2, src='ru', dest='uk')

    print(inp_trans_text_2_uk.text)

    ############## end translate

#####EN text add
    page.find_element(By.XPATH, "(//div[text()='EN'])[1]").click()

    inp_eng = page.find_element(By.XPATH, '(input)[7]')

    visib_inp = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(input)[7]')))

    visib_inp.clear()

    inp_eng.send_keys(inp_trans_text_1_eng.text)

    time.sleep(15)

    page.quit()