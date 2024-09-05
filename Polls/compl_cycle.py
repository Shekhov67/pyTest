
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from selenium.webdriver.common.action_chains import ActionChains


def test_completing_poll_open():

    for i in range(1, 10):

        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        # driver.get("https://connectable.site/")
        driver.get("https://staging.connectable.site/")

        page = driver

        wait = WebDriverWait(page, 5)

        page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('pytest')

        page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'i{i}@gmail.com')

        page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

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

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Опросы')]")))

        page.find_element(By.XPATH, "//*[contains(text(), 'Опросы')]").click()

        page.find_element(By.XPATH, "//input[@placeholder='Искать']").send_keys('открытый')

        page.find_element(By.XPATH, "(//a[@class=''])[1]").click()

        try:

            page.find_element(By.XPATH, "//div[text()='Пройти опрос']").click()

        except:

            print(f"Пользователь i{i}@gmail.com проходил опрос")
            page.close()

        ##Кнопка следующий вопрос

        nxt = page.find_element(By.XPATH, "//div[text()='Следующий вопрос']")

        (page.find_element(By.XPATH, "//input[@type='text']").
         send_keys(f"Ответ на первый вопрос. Отвечал i{i}@gmail.com"))

        nxt.click()

        (page.find_element(By.XPATH, '//textarea[@class="ant-input"]').
         send_keys(f"Ответ на второй вопрос.Отвечал i{i}@gmail.com"))

        nxt.click()

        num = randint(1, 5)

        page.find_element(By.XPATH, f'//div[@aria-posinset="{num}"]').click()

        nxt.click()

        num = randint(1, 10)

        page.find_element(By.XPATH, f'//div[@aria-posinset="{num}"]').click()

        nxt.click()

        action = ActionChains(page)

        point = page.find_element(By.XPATH, '//div[@role="slider"]')

        num = randint(1, 338)

        action.click_and_hold(point).move_by_offset(num, 0).click().perform()

        nxt.click()

        num = randint(1, 5)

        page.find_element(By.XPATH, f'(//input[@type="radio"])[{num}]').click()

        nxt.click()

        num = randint(1, 5)

        num2 = randint(1, 5)

        while num == num2:
            num2 = randint(1, 5)

        page.find_element(By.XPATH, f'(//input[@type="checkbox"])[{num}]').click()

        page.find_element(By.XPATH, f'(//input[@type="checkbox"])[{num2}]').click()

        page.find_element(By.XPATH, "//div[text()='Завершить']").click()

        page.close()


def test_completing_poll_close():

    for i in range(1, 10):

        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        # driver.get("https://connectable.site/")
        driver.get("https://staging.connectable.site/")

        page = driver

        wait = WebDriverWait(page, 5)

        page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('pytest')

        page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'i{i}@gmail.com')

        page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

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

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Опросы')]")))

        page.find_element(By.XPATH, "//*[contains(text(), 'Опросы')]").click()

        page.find_element(By.XPATH, "//input[@placeholder='Искать']").send_keys('закрытый')

        page.find_element(By.XPATH, "(//a[@class=''])[1]").click()

        try:

            page.find_element(By.XPATH, "//div[text()='Пройти опрос']").click()

        except:

            print(f"Пользователь i{i}@gmail.com проходил опрос")
            page.close()

        ##Кнопка следующий вопрос

        nxt = page.find_element(By.XPATH, "//div[text()='Следующий вопрос']")

        (page.find_element(By.XPATH, "//input[@type='text']").
         send_keys(f"Ответ на первый вопрос. Отвечал i{i}@gmail.com"))

        nxt.click()

        (page.find_element(By.XPATH, '//textarea[@class="ant-input"]').
         send_keys(f"Ответ на второй вопрос.Отвечал i{i}@gmail.com"))

        nxt.click()

        num = randint(1, 5)

        page.find_element(By.XPATH, f'//div[@aria-posinset="{num}"]').click()

        nxt.click()

        num = randint(1, 10)

        page.find_element(By.XPATH, f'//div[@aria-posinset="{num}"]').click()

        nxt.click()

        action = ActionChains(page)

        point = page.find_element(By.XPATH, '//div[@role="slider"]')

        num = randint(1, 338)

        action.click_and_hold(point).move_by_offset(num, 0).click().perform()

        nxt.click()

        num = randint(1, 5)

        page.find_element(By.XPATH, f'(//input[@type="radio"])[{num}]').click()

        nxt.click()

        num = randint(1, 5)

        num2 = randint(1, 5)

        while num == num2:
            num2 = randint(1, 5)

        page.find_element(By.XPATH, f'(//input[@type="checkbox"])[{num}]').click()

        page.find_element(By.XPATH, f'(//input[@type="checkbox"])[{num2}]').click()

        page.find_element(By.XPATH, "//div[text()='Завершить']").click()

        page.close()


def test_completing_poll_anonym():
    for i in range(1, 10):

        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        # driver.get("https://connectable.site/")
        driver.get("https://staging.connectable.site/")

        page = driver

        wait = WebDriverWait(page, 5)

        page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('pytest')

        page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'i{i}@gmail.com')

        page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

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

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Опросы')]")))

        page.find_element(By.XPATH, "//*[contains(text(), 'Опросы')]").click()

        page.find_element(By.XPATH, "//input[@placeholder='Искать']").send_keys('анонимный')

        page.find_element(By.XPATH, "(//a[@class=''])[1]").click()

        try:

            page.find_element(By.XPATH, "//div[text()='Пройти опрос']").click()

        except:

            print(f"Пользователь i{i}@gmail.com проходил опрос")
            page.close()

        ##Кнопка следующий вопрос

        nxt = page.find_element(By.XPATH, "//div[text()='Следующий вопрос']")

        (page.find_element(By.XPATH, "//input[@type='text']").
         send_keys(f"Ответ на первый вопрос. Отвечал i{i}@gmail.com"))

        nxt.click()

        (page.find_element(By.XPATH, '//textarea[@class="ant-input"]').
         send_keys(f"Ответ на второй вопрос.Отвечал i{i}@gmail.com"))

        nxt.click()

        num = randint(1, 5)

        page.find_element(By.XPATH, f'//div[@aria-posinset="{num}"]').click()

        nxt.click()

        num = randint(1, 10)

        page.find_element(By.XPATH, f'//div[@aria-posinset="{num}"]').click()

        nxt.click()

        action = ActionChains(page)

        point = page.find_element(By.XPATH, '//div[@role="slider"]')

        num = randint(1, 338)

        action.click_and_hold(point).move_by_offset(num, 0).click().perform()

        nxt.click()

        num = randint(1, 5)

        page.find_element(By.XPATH, f'(//input[@type="radio"])[{num}]').click()

        nxt.click()

        num = randint(1, 5)

        num2 = randint(1, 5)

        while num == num2:
            num2 = randint(1, 5)

        page.find_element(By.XPATH, f'(//input[@type="checkbox"])[{num}]').click()

        page.find_element(By.XPATH, f'(//input[@type="checkbox"])[{num2}]').click()

        page.find_element(By.XPATH, "//div[text()='Завершить']").click()

        page.close()