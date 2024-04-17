from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from openpyxl import Workbook, load_workbook
from faker import Faker

@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://staging.connectable.site/login")
    return driver



def test_first(page):
    '''page это драйвер с уже запущенной старницей'''

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('pytest')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys('t2@gmail.com')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    WebDriverWait(page, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), ' Администрирование')]")))

    page.find_element(By.XPATH, "//*[contains(text(), ' Администрирование')]").click()

    for i in range(100):

        faker = Faker('RU')
        email = f'py{i}@gmail.com'
        job = faker.job()
        name = faker.first_name_male()
        last_name = faker.last_name_male()

        WebDriverWait(page, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Новый сотрудник']")))

        page.find_element(By.XPATH, "//div[text()='Новый сотрудник']").click()

        WebDriverWait(page, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-body']")))

        page.find_element(By.XPATH, "//input[@placeholder='Введите имя сотрудника']").send_keys(f'{name}')
        page.find_element(By.XPATH, "//input[@placeholder='Введите отчество сотрудника']").send_keys('Питонович')
        page.find_element(By.XPATH, "//input[@placeholder='Введите фамилию сотрудника']").send_keys(f'{last_name}')
        page.find_element(By.XPATH, "//input[@placeholder='Должность']").send_keys(f'{job}')
        page.find_element(By.XPATH, "//input[@placeholder='Введите e-mail']").send_keys(f'{email}')
        page.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys('111111')
        page.find_element(By.XPATH, "//input[@placeholder='Подтверждение пароля']").send_keys('111111')
        page.find_element(By.XPATH, "(//button[@class='ant-btn ant-btn-primary'])[2]").click()

        WebDriverWait(page, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class= 'anticon anticon-close ant-notification-close-icon']")))

        page.find_element(By.XPATH, "//*[@class= 'anticon anticon-close ant-notification-close-icon']").click()

