from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from selenium.webdriver.common.action_chains import ActionChains

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

    page.quit()