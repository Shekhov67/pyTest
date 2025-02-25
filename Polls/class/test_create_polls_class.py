from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from TestSuites.smoke.test_module import url
#url = 'https://staging.connectable.site/'
#url = 'https://connectable.site/'
#url = 'https://intranetable.team/'

class TestCreatePolls:

    def __init__(self, type_polls, name_polls, polls_description):

        self.type = type_polls
        self.name = name_polls
        self.description = polls_description

    def test_create_polls(self):

        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(url)
        page = driver

        wait = WebDriverWait(page, 5)

        page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys('pytest')

        page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys('t2@gmail.com')

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

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Добавить опрос']")))

        page.find_element(By.XPATH, "//div[text()='Добавить опрос']").click()

        page.find_element(By.XPATH, f"(//input[@type='radio'])[{self.type}]").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='w-100 col f-grow-1 relative p4']")))

        page.find_element(By.XPATH, "(//input)[1]").clear()

        page.find_element(By.XPATH, "(//input)[1]").send_keys(f'{self.name}')

        page.find_element(By.XPATH, "//textarea").clear()

        page.find_element(By.XPATH, "//textarea").send_keys(f'{self.description}')
        ##Кнопка добавления вопроса
        plus = page.find_element(By.XPATH, "//div[@class='abs']")

        plus.click()

        (page.find_element(By.XPATH,
                           '//input[@class="ant-input empty-input"]').send_keys('Вопрос первый'))

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        plus.click()

        (page.find_element(By.XPATH,
                           '//input[@class="ant-input empty-input"]').send_keys('Вопрос второй'))

        page.find_element(By.XPATH, "(//span[@class='ant-select-arrow'])[2]").click()

        page.find_element(By.XPATH, "//li[text()='Развернутый ответ текстом']").click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)
        ##Вопросы с диапазонами чисел
        plus.click()

        (page.find_element(By.XPATH,
                           '//input[@class="ant-input empty-input"]').send_keys('Вопрос третий'))

        page.find_element(By.XPATH, "(//span[@class='ant-select-arrow'])[3]").click()

        page.find_element(By.XPATH, "(//li[text()='Выбор числа в диапазоне'])[2]").click()

        page.find_element(By.XPATH, "(//span[text()='от 1 до 5'])[1]").click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        plus.click()

        (page.find_element(By.XPATH,
                           '//input[@class="ant-input empty-input"]').send_keys('Вопрос четвертый'))

        page.find_element(By.XPATH, "(//span[@class='ant-select-arrow'])[4]").click()

        page.find_element(By.XPATH, "(//li[text()='Выбор числа в диапазоне'])[3]").click()

        page.find_element(By.XPATH, "(//span[text()='от 1 до 10'])[2]").click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        plus.click()

        (page.find_element(By.XPATH,
                           '//input[@class="ant-input empty-input"]').send_keys('Вопрос пятый'))

        page.find_element(By.XPATH, "(//span[@class='ant-select-arrow'])[5]").click()

        page.find_element(By.XPATH, "(//li[text()='Выбор числа в диапазоне'])[4]").click()

        page.find_element(By.XPATH, "(//span[text()='от 1 до 100'])[3]").click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        plus.click()

        (page.find_element(By.XPATH,
                           '//input[@class="ant-input empty-input"]').send_keys('Вопрос шестой'))

        page.find_element(By.XPATH, "(//span[@class='ant-select-arrow'])[6]").click()

        page.find_element(By.XPATH, "(//li[text()='Один вариант из списка'])[5]").click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '//*[@class="ant-btn ant-btn-link"]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '//*[@class="ant-btn ant-btn-link"]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '//*[@class="ant-btn ant-btn-link"]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '//*[@class="ant-btn ant-btn-link"]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '//*[@class="ant-btn ant-btn-link"]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        plus.click()

        (page.find_element(By.XPATH,
                           '//input[@class="ant-input empty-input"]').send_keys('Вопрос седьмой'))

        page.find_element(By.XPATH, "(//span[@class='ant-select-arrow'])[7]").click()

        page.find_element(By.XPATH, "(//li[text()='Несколько вариантов из списка'])[6]").click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '(//*[@class="ant-btn ant-btn-link"])[2]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '(//*[@class="ant-btn ant-btn-link"])[2]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '(//*[@class="ant-btn ant-btn-link"])[2]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '(//*[@class="ant-btn ant-btn-link"])[2]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, '(//*[@class="ant-btn ant-btn-link"])[2]').click()

        page.execute_script("arguments[0].scrollIntoView(true);", plus)

        page.find_element(By.XPATH, "(//button[@role='switch'])[7]").click()

        btn_save = page.find_element(By.XPATH, "//div[text()='Сохранить']")

        page.execute_script("arguments[0].scrollIntoView(true);", btn_save)

        btn_save.click()

        page.close()

    #def test_delete_poll(self):





open_polls = TestCreatePolls('1', 'Открытый опрос', 'Это описание открытого опроса на питонском автотесте')
open_polls.test_create_polls()

close_polls = TestCreatePolls('2', 'Закрытый опрос', 'Это описание закрытого опроса на питонском автотесте')
close_polls.test_create_polls()

anonim_polls = TestCreatePolls('3', 'Анонимный опрос', 'Это описание анонимного опроса на питонском автотесте')
anonim_polls.test_create_polls()