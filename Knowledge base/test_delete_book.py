import time

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

    wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@class="f-grow-1"])[7]')))

    page.find_element(By.XPATH, '(//div[@class="f-grow-1"])[7]').click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Материалы']")))

    materials = page.find_element(By.XPATH, "//div[text()='Материалы']")

    page.execute_script("arguments[0].scrollIntoView(true);", materials)

    num_materials = page.find_element(By.XPATH, '(//div[@class="badge ml2 text-12 secondary wide bold"])[2]').text

    print(num_materials)

    for i in range(int(num_materials)):

        wait.until(EC.presence_of_element_located((By.XPATH, '//img[@src="/assets/img/blank_doc_48.a43200c3.svg"]')))

        material = page.find_element(By.XPATH, '//img[@src="/assets/img/blank_doc_48.a43200c3.svg"]')

        material_mouse = ActionChains(page)

        material_mouse.move_to_element(material).perform()

        #найти веб элемент(метериалы) по несколькоим xpath

        wait.until(EC.presence_of_all_elements_located((By.XPATH, '')))

        page.find_element(By.XPATH, '(//*[@class="svg-icon grey"])[1]').click()

        wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@class="dropdown-item text-red"])[1]')))

        page.find_element(By.XPATH, '(//div[@class="dropdown-item text-red"])[1]').click()

        time.sleep(3)