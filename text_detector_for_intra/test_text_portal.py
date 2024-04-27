from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from method_scan_ru_text import scan_ru_text

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

    #Поиск русских слов на странице
    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Company data')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Company data')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Rights and roles')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Rights and roles')]").click()

    scan_ru_text(page, wait)




