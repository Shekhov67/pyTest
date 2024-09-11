import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint

class TestCrudPosts:

    def __init__(self, posts_line):
        self.line = posts_line

    def crudPosts(self, posts_line):

        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("https://staging.connectable.site/login")
        page = driver
        workspace = 'pytest'
        userLog = 't2@gmail.com'
        password = '111111'
        # createText - переменная для ввода текста в создаваеммом посте
        createText = 'AutoPyTest2'
        updateText = 'updateTextPyTest'

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

                page.find_element(By.XPATH,
                                  f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]').click()
        except:
            print('Муд блок не появился')

        WebDriverWait(page, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Стена')]")))

        page.find_element(By.XPATH, "//*[contains(text(), 'Стена')]").click()

        wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{posts_line}']")))

        page.find_element(By.XPATH, f"//div[text()='{posts_line}']").click()

        (page.find_element(
            By.XPATH, "//textarea[@placeholder ='Напишите текст сообщения. Используйте @, чтобы кого-то упомянуть']").
         click())

        (page.find_element(
            By.XPATH, "//textarea[@placeholder ='Напишите текст сообщения. Используйте @, чтобы кого-то упомянуть']").
         send_keys(createText))

        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Опубликовать']")))

        page.find_element(By.XPATH, "//div[text()='Опубликовать']").click()

        wait.until(EC.presence_of_element_located((By.XPATH, f"(//div[text()= '{createText}'])[1]")))

        wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'small')])[2]")))

        page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@d,'13.707Z')]")))

        page.find_element(By.XPATH, "//*[contains(@d,'13.707Z')]").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='post-wrapper col py6 px4 gap4']")))

        wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{createText}']")))

        gettext = page.find_element(By.XPATH, f"//div[text()='{createText}']").text

        assert gettext == createText, "Текст поста на стене != текст открытого поста"

        wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'small')])[1]")))

        page.find_element(By.XPATH, "(//div[contains(@class,'small')])[1]").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@d,'8.31003Z')]")))

        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@d,'8.31003Z')]")))

        page.find_element(By.XPATH, "//*[contains(@d,'8.31003Z')]").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-drawer-content']")))

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-drawer-body']")))

        wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea)[2]")))

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dropdown-menu show']")))

        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='ant-drawer ant-drawer-right ant-drawer-open create-group-drawer']")))

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".input-wrapper")))

        page.find_element(By.CSS_SELECTOR, ".input-wrapper").click()

        page.find_element(By.XPATH, "(//textarea)[2]").clear()

        page.find_element(By.XPATH, "(//textarea)[2]").send_keys(updateText)

        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="btn f-centered pointer primary text-center"]')))

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer primary text-center"]').click()

        wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{updateText}']")))

        gettext2 = page.find_element(By.XPATH, f"//div[text()='{updateText}']").text

        wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{updateText}']")))

        assert gettext2 == updateText, "Обновленный текст не совпадает"

        page.find_element(By.XPATH, "//div[text()='Назад в ленту']").click()

        gettext3 = page.find_element(By.XPATH, f"//div[text()='{updateText}']").text

        assert gettext3 == updateText, "Проверка обновленного поста на стене"

        page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

        icon_delete = page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[5]')

        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@d, '8.1046')])[1]")))

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(@d, '8.1046')])[1]")))

        icon_delete.click()

        wait.until(EC.element_to_be_clickable
                   ((By.XPATH, '//div[@class="ant-notification-notice-message"]')))

        alertDeletedPost = page.find_element(By.XPATH, '//div[text()="Пост удален"]').text

        print(alertDeletedPost)

        assert alertDeletedPost == "Пост удален", " Проверка алерта удаления поста  "


test_line_news = TestCrudPosts('Лента событий')
test_line_news.crudPosts('Лента событий')

test_line_company = TestCrudPosts('Новости компании')#добавить логику нажатия чек бокса новости компании
test_line_company.crudPosts('Новости компании')