from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys



@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://staging.connectable.site/login")
    driver.implicitly_wait(5)
    return driver

def test_createPostsNewsline(page):

    #createText - переменная для ввода текста в создаваеммом посте

    createText = 'AutoPyTest2'

    updateText = 'updateTextPyTest'

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('testing4')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys('t2@gmail.com')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, "//div[text()=' Стена ']")))

    page.find_element(By.XPATH, "//div[text()=' Стена ']").click()

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, "//div[text()='Лента событий']")))

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

    gettext = page.find_element(By.XPATH, f"//div[text()='{createText}']").text

    assert gettext == createText, "Текст поста на стене != текст открытого поста"

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[1]").click()

    page.find_element(By.XPATH, "(//div[text()=' Редактировать '])[1]").click()

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-drawer-body']")))

    WebDriverWait(page, '5').until(EC.presence_of_element_located((By.XPATH, "(//textarea)[2]")))

    page.find_element(By.XPATH, "(//textarea)[2]").clear()

    page.find_element(By.XPATH, "(//textarea)[2]").send_keys(updateText)

    page.find_element(By.XPATH, "//div[text()=' Сохранить ']").click()

    gettext2 = page.find_element(By.XPATH, f"//div[text()='{updateText}']").text

    WebDriverWait(page, "5").until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{updateText}']")))

    time.sleep(2)

    assert gettext2 == updateText, "Обновленный текст не совпадает"

    page.find_element(By.XPATH, "//div[text()='Назад в ленту']").click()

    gettext3 = page.find_element(By.XPATH, f"//div[text()='{updateText}']").text

    assert gettext3 == updateText, "Проверка обновленного поста на стене"

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    page.find_element(By.XPATH, "(//div[text()=' Удалить '])[1]").click()

    WebDriverWait(page, "5").until(EC.presence_of_element_located((By.XPATH, "//div[text()='Пост удален']")))

    alertDeletedPost = page.find_element(By.XPATH, "//div[text()='Пост удален']").text

    assert alertDeletedPost == "Пост удален", " Проверка алерта удаления поста "

    time.sleep(2)







