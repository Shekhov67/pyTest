import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from prompt_toolkit.keys import Keys

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

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'База знаний')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'База знаний')]").click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="badge ml2 text-12 secondary wide bold"]')))

    num_folder = page.find_element(By.XPATH, '//div[@class="badge ml2 text-12 secondary wide bold"]').text

    print(num_folder)

    for i in range(int(num_folder)):

        page.refresh()

        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   '(//div[@class="item pointer relative p1 radius2 folder"])[1]')))

        folder = page.find_element(By.XPATH, '(//div[@class="item pointer relative p1 radius2 folder"])[1]')

        folder_mouse = ActionChains(page)

        folder_mouse.move_to_element(folder).perform()

        wait.until(EC.presence_of_element_located((By.XPATH, '(//*[@class="svg-icon grey"])[1]')))

        page.find_element(By.XPATH, '(//*[@class="svg-icon grey"])[1]').click()

        wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@class="dropdown-item text-red"])[1]')))

        page.find_element(By.XPATH, '(//div[@class="dropdown-item text-red"])[1]').click()

        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ant-modal-body"]')))

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Да']")))

        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Да']")))

        page.find_element(By.XPATH, '//button[@class="ant-btn ant-btn-danger"]').click()

        wait.until_not(EC.presence_of_element_located((By.XPATH, '//div[@class="ant-modal-body"]')))

        page.delete_all_cookies()
