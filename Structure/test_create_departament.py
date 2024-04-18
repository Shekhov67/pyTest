import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint

@pytest.fixture()
def workspace():
    client = 'pytest'
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
    driver.get("https://staging.connectable.site/")
    return driver

def test_create(page, workspace, userLog, password):

    wait = WebDriverWait(page, 5)

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

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '(//div[@class="rate-cell text-16 semibold f-centered pointer"])[10]')))

            (page.find_element(By.XPATH, f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]').
             click())
    except:
        print('Муд блок не появился')

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Структура')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Структура')]").click()

    for i in range(200):

        count_dep = '//div[@class="new-dept btn f-centered pointer text-center secondary icon"]'

        num = page.find_elements(By.XPATH, count_dep)

        select_num_dep = randint(1, len(num)+1)

        print(select_num_dep)

        create_dep = f'(//div[@class="new-dept btn f-centered pointer text-center secondary icon"])[{select_num_dep}]'

        wait.until(EC.presence_of_element_located((By.XPATH, create_dep)))

        time.sleep(2)

        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card-structure col p0"]')))

        page.find_element(By.XPATH, create_dep).click()

        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ant-modal-content"]')))

        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="ant-modal-content"]')))

        wait.until(EC.presence_of_element_located((By.XPATH, '//input')))

        wait.until(EC.element_to_be_clickable((By.XPATH, '//input')))

        page.find_element(By.XPATH, '//input').send_keys(f'Питонский отдел {i}')

        wait.until(EC.presence_of_element_located((By.XPATH, '//textarea')))

        wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea')))

        page.find_element(By.XPATH, '//textarea').send_keys(f'Это питонский отдел {i} созданный с помощью автотестов')

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Сохранить']")))

        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Сохранить']")))

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()