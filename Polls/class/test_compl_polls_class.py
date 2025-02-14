from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from selenium.webdriver.common.action_chains import ActionChains
from TestSuites.test_module import url
from TestSuites.test_module import num_polls

#url = 'https://staging.connectable.site/'
#url = 'https://connectable.site/'
#url = 'https://intranetable.team/'
'''num_polls - количество циклов прохождений опроса'''
#num_polls = 23

class Polls:
    def __init__(self, type_polls):
        self.type = type_polls

    def test_completing_poll(self):

        #global num_polls

        for i in range(1, num_polls):

            #global url
            driver = webdriver.Chrome()
            driver.implicitly_wait(5)
            driver.maximize_window()
            driver.get(url)
            #driver.get("https://staging.connectable.site/")

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

            page.find_element(By.XPATH, "//input[@placeholder='Искать']").send_keys(self.type)

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

            (page.find_element(By.XPATH, '//textarea').
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


test_open = Polls('открытый')
test_open.test_completing_poll()

test_close = Polls('закрытый')
test_close.test_completing_poll()

test_anon = Polls('анонимный')
test_anon.test_completing_poll()