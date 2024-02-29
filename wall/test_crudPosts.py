from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://staging.connectable.site/login")
    return driver

def test_createPostsNewsline(page):

    createText = 'AutoPyTest1'

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('testing4')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys('t2@gmail.com')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, "//div[text()=' Стена ']")))

    page.find_element(By.XPATH, "//div[text()=' Стена ']").click()

    page.find_element(By.XPATH, "//div[text()='Лента событий']").click()

    page.find_element(By.XPATH, "//textarea[@placeholder ='Напишите текст сообщения. Используйте @, чтобы кого-то упомянуть']").click()

    page.find_element(By.XPATH, "//textarea[@placeholder ='Напишите текст сообщения. Используйте @, чтобы кого-то упомянуть']").send_keys(createText)

    page.find_element(By.XPATH, "//div[text()='Опубликовать']").click()

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, f"(//div[text()= '{createText}'])[1]")))

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'small')])[2]")))

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    page.find_element(By.XPATH, "(//div[text()=' Открыть '])[1]").click()

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, "//div[@class='post-wrapper col py6 px4 gap4']")))

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{createText}']")))

    time.sleep(2)

    gettext = page.find_element(By.XPATH, f"//div[text()='{createText}']").text

    assert gettext == createText, "Текст поста на стене != текст открытого поста"

    time.sleep(2)







