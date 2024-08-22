
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.get("https://intranetable.team/")
    #driver.get("https://connectable.site/")
    driver.get("https://staging.connectable.site/")
    #driver.implicitly_wait(5)
    return driver
def test_first(page):
    '''page это драйвер с уже запущенной старницей'''

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('testing9')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys('t2@gmail.com')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    WebDriverWait(page, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), ' Администрирование')]")))

    page.find_element(By.XPATH, "//*[contains(text(), ' Администрирование')]").click()

    for i in range(50):
        #sex = 'female'
        fake = Faker('ru_RU')
        email = f'ii{i}@gmail.com'
        job = fake.job()
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        midd_name = fake.middle_name_male()
        phone = fake.phone_number()
        print(first_name, midd_name, last_name, email)

        WebDriverWait(page, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Новый сотрудник']")))

        page.find_element(By.XPATH, "//div[text()='Новый сотрудник']").click()

        WebDriverWait(page, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-body']")))

        page.find_element(By.XPATH, "//input[@placeholder='Введите имя сотрудника']").send_keys(first_name)
        page.find_element(By.XPATH, "//input[@placeholder='Введите отчество сотрудника']").send_keys(midd_name)
        page.find_element(By.XPATH, "//input[@placeholder='Введите фамилию сотрудника']").send_keys(last_name)
        page.find_element(By.XPATH, "//input[@placeholder='Должность']").send_keys(job)
        page.find_element(By.XPATH, "(//input[@placeholder='Телефон'])[1]").send_keys(phone)
        page.find_element(By.XPATH, "//input[@placeholder='Введите e-mail']").send_keys(email)
        page.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys('111111')
        page.find_element(By.XPATH, "//input[@placeholder='Подтверждение пароля']").send_keys('111111')
        page.find_element(By.XPATH, "(//button[@class='ant-btn ant-btn-primary'])[2]").click()

        WebDriverWait(page, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class= 'anticon anticon-close ant-notification-close-icon']")))

        page.find_element(By.XPATH, "//*[@class= 'anticon anticon-close ant-notification-close-icon']").click()

