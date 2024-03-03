from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://staging.connectable.site/login")
    return driver

def test_createPostsNewsline(page):

    #createText - переменная для ввода текста в создаваеммом посте

    createText = 'AutoPyTest2'

    updateText = 'updateTextPyTest'

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('testing4')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys('t2@gmail.com')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, "//div[text()=' Стена ']")))

    page.find_element(By.XPATH, "//div[text()=' Стена ']").click()

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Лента событий']")))

    page.find_element(By.XPATH, "//div[text()='Лента событий']").click()

    page.find_element(By.XPATH, "//textarea[@placeholder ='Напишите текст сообщения. Используйте @, чтобы кого-то упомянуть']").click()

    page.find_element(By.XPATH, "//textarea[@placeholder ='Напишите текст сообщения. Используйте @, чтобы кого-то упомянуть']").send_keys(createText)

    page.find_element(By.XPATH, "//div[text()='Опубликовать']").click()

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, f"(//div[text()= '{createText}'])[1]")))

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'small')])[2]")))

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    page.find_element(By.XPATH, "(//div[text()=' Открыть '])[1]").click()

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='post-wrapper col py6 px4 gap4']")))

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{createText}']")))

    gettext = page.find_element(By.XPATH, f"//div[text()='{createText}']").text

    assert gettext == createText, "Текст поста на стене != текст открытого поста"

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[1]").click()

    page.find_element(By.XPATH, "(//div[text()=' Редактировать '])[1]").click()

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-drawer-content']")))

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-drawer-body']")))

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, "(//textarea)[2]")))

    wait = WebDriverWait(page, 5)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dropdown-menu show']")))

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='ant-drawer ant-drawer-right ant-drawer-open create-group-drawer']")))

    page.find_element(By.XPATH, "//div[@class='input-wrapper f-align-center bg-white medium px2']").click()

    page.find_element(By.XPATH, "(//textarea)[2]").clear()

    page.find_element(By.XPATH, "(//textarea)[2]").send_keys(updateText)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()=' Сохранить ']")))

    page.find_element(By.XPATH, "//div[text()=' Сохранить ']").click()

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{updateText}']")))

    gettext2 = page.find_element(By.XPATH, f"//div[text()='{updateText}']").text

    WebDriverWait(page, 5).until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{updateText}']")))

    assert gettext2 == updateText, "Обновленный текст не совпадает"

    page.find_element(By.XPATH, "//div[text()='Назад в ленту']").click()

    gettext3 = page.find_element(By.XPATH, f"//div[text()='{updateText}']").text

    assert gettext3 == updateText, "Проверка обновленного поста на стене"

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    page.find_element(By.XPATH, "(//div[text()=' Удалить '])[1]").click()

    wait.until(EC.element_to_be_clickable
               ((By.XPATH, '//div[@class="ant-notification-notice-message"]')))

    alertDeletedPost = page.find_element(By.XPATH, '//div[text()="Пост удален"]').text

    print(alertDeletedPost)

    assert alertDeletedPost == "Пост удален", " Проверка алерта удаления поста "









