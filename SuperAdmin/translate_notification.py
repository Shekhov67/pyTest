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

    for i in range(1, 63):

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

    ########### translate  EN

        translator = Translator()

        inp_trans_text_3_eng = translator.translate(text_3, src='ru', dest='en')

        print(inp_trans_text_3_eng.text)

        area_trans_text_1_eng = translator.translate(area_element_1, src='ru', dest='en')

        print(area_trans_text_1_eng.text)

        area_trans_text_2_eng = translator.translate(area_element_2, src='ru', dest='en')

        print(area_trans_text_2_eng.text)

        inp_trans_text_4_eng = translator.translate(text_4, src='ru', dest='en')

        print(inp_trans_text_4_eng.text)

        ################## translate UK

        inp_trans_text_3_uk = translator.translate(text_3, src='ru', dest='uk')

        print(inp_trans_text_3_uk.text)

        area_trans_text_1_uk = translator.translate(area_element_1, src='ru', dest='uk')

        print(area_trans_text_1_uk.text)

        area_trans_text_2_uk = translator.translate(area_element_2, src='ru', dest='uk')

        print(area_trans_text_2_uk.text)

        inp_trans_text_4_uk = translator.translate(text_4, src='ru', dest='uk')

        print(inp_trans_text_4_uk.text)

        ############## end translate

    #####EN text add
        page.refresh()

        page.find_element(By.XPATH, "//div[text()='Settings of notifications']").click()

        element = page.find_element(By.XPATH, f'(//div[@class="ant-collapse-header"])[{i}]')  # выбор уведомления для перевода

        element.execute_script("arguments[0].scrollIntoView(true);", element)

        element.click()

        page.find_element(By.XPATH, "(//div[text()='EN'])[1]").click()

    #####Добавление "Заголовка"

        inp_eng5 = page.find_element(By.XPATH, '(//input)[5]')

        visib_inp5 = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(//input)[5]')))

        visib_inp5.clear()

        inp_eng5.send_keys(inp_trans_text_3_eng.text)

    ######## Добавление "Текст краткого шаблона"

        area_eng3 = page.find_element(By.XPATH, '(//textarea)[3]')

        visib_area3 = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(//textarea)[3]')))

        visib_area3.clear()

        area_eng3.send_keys(area_trans_text_1_eng.text)

    ######## Добавление "Текст полного шаблона"

        area_eng4 = page.find_element(By.XPATH, '(//textarea)[4]')

        visib_area4 = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(//textarea)[4]')))

        visib_area4.clear()

        area_eng4.send_keys(area_trans_text_1_eng.text)

    #####Добавление "Заголовка"

        inp_eng6 = page.find_element(By.XPATH, '(//input)[6]')

        visib_inp6 = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(//input)[6]')))

        visib_inp6.clear()

        inp_eng6.send_keys(inp_trans_text_4_eng.text)

        page.find_element(By.XPATH, "//div[text()='Save']").click()

        #####UK text add
        page.refresh()

        page.find_element(By.XPATH, "//div[text()='Settings of notifications']").click()

        element = page.find_element(By.XPATH, f'(//div[@class="ant-collapse-header"])[{i}]')  # выбор уведомления для перевода

        element.execute_script("arguments[0].scrollIntoView(true);", element)

        element.click()

        page.find_element(By.XPATH, "(//div[text()='UA'])[1]").click()

        #####Добавление "Заголовка"

        inp_uk5 = page.find_element(By.XPATH, '(//input)[5]')

        visib_inp5 = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(//input)[5]')))

        visib_inp5.clear()

        inp_uk5.send_keys(inp_trans_text_3_uk.text)

        ######## Добавление "Текст краткого шаблона"

        area_uk3 = page.find_element(By.XPATH, '(//textarea)[3]')

        visib_area3 = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(//textarea)[3]')))

        visib_area3.clear()

        area_uk3.send_keys(area_trans_text_1_uk.text)

        ######## Добавление "Текст полного шаблона"

        area_uk4 = page.find_element(By.XPATH, '(//textarea)[4]')

        visib_area4 = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(//textarea)[4]')))

        visib_area4.clear()

        area_uk4.send_keys(area_trans_text_1_uk.text)

        #####Добавление "Заголовка"

        inp_uk6 = page.find_element(By.XPATH, '(//input)[6]')

        visib_inp6 = WebDriverWait(page, 5).until(EC.visibility_of_element_located((By.XPATH, '(//input)[6]')))

        visib_inp6.clear()

        inp_uk6.send_keys(inp_trans_text_4_uk.text)

        page.find_element(By.XPATH, "//div[text()='Save']").click()

        time.sleep(5)

        page.refresh()

        page.find_element(By.XPATH, "//div[text()='Settings of notifications']").click()

    page.quit()