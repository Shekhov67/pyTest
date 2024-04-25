import time
from langdetect import detect, DetectorFactory
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint

@pytest.fixture()
def workspace():
    client = 'testing1'
    return client
@pytest.fixture()
def userLog():
    user = 't2@gmail.com'
    return user
@pytest.fixture()
def password():
    passw = '111111'
    return passw

@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    #driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://intranetable.team/")
    return driver

def test_text(page, workspace, userLog, password):
    wait = WebDriverWait(page, 5)

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys(f'{workspace}')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'{userLog}')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(f'{password}')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="page-block mood-block col"]')))

        moodBlock = page.find_element(By.XPATH, '//div[@class="page-block mood-block col"]')

        print(moodBlock)

        if moodBlock:
            num = randint(1, 10)

            print(f'Рандомное число для оценки настроения {num}')

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '(//div[@class="rate-cell text-16 semibold f-centered pointer"])[10]')))

            (page.find_element(By.XPATH, f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]').
             click())
    except:
        print('Муд блок не появился')

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Administration')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Administration')]").click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Company data')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Company data')]").click()

    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, "//html")))

    text_detection = page.find_element(By.XPATH, "//html").text

    print(text_detection)

    list_text = text_detection.split()

    print(list_text)

    print(len(list_text))

    print(detect(list_text[1]))

    for i in range(len(list_text)):

        time.sleep(1)

        detect_language = detect(list_text[i])

        if detect_language == 'ru':
            print(f'Текст на русском языке: {list_text[i]}')

