import time
from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from TestSuites.smoke.test_module import url


@pytest.fixture()
def workspace():
    client = 'testing9'
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
    driver.implicitly_wait(50)
    driver.maximize_window()
    driver.get(url)
    return driver

def test_upload(page, workspace, userLog, password):
    #createText - переменная для ввода текста в создаваеммом посте
    createText = 'AutoPyTest2'

    updateText = 'updateTextPyTest'

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys(f'{workspace}')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'{userLog}')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(f'{password}')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    try:
        moodBlock = page.find_element(By.XPATH, '//div[@class="page-block mood-block col"]')

        print(moodBlock)

        if moodBlock:

            num = randint(1, 10)

            print(f'Рандомное число для оценки настроения {num}')

            page.find_element(By.XPATH,
                              f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]').click()
    except:
        print('Муд блок не появился')

    page.find_element(By.XPATH, "//*[contains(text(), 'Стена')]").click()

    try:

        page.find_element(By.XPATH, "//input[@accept]").send_keys('C:\\Users\\shehs\\PycharmProjects\\pyTest\\Load Files\\111.png')

        page.find_element(By.XPATH, '//textarea[@id="inputField"]').send_keys('Тестовая загрузка файла в пост 1')

        page.find_element(By.XPATH, "//div[text()='Опубликовать']").click()

        page.refresh()

        page.find_element(By.XPATH, "//input[@accept]").send_keys('C:\\Users\\shehs\\PycharmProjects\\pyTest\\Load Files\\222.png')

        page.find_element(By.XPATH, '//textarea[@id="inputField"]').send_keys('Тестовая загрузка файла в пост 2')

        page.find_element(By.XPATH, "//div[text()='Опубликовать']").click()

    except:
        pytest.fail('Не грузит файл')