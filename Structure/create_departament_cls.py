import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from TestSuites.smoke.test_module import url

workspace = "pytest"
userLog = "t2@gmail.com"
#url = 'https://staging.connectable.site/'
#url = 'https://connectable.site/'
#url = 'https://intranetable.team/'
class TestCreateDepartament:
    def __init__(self, type_dep, name_dep):
        self.type = type_dep
        self.name = name_dep

    def create_dep(self):

        #global url

        global workspace

        global userLog

        # Создаём объект настроек Chrome
        chrome_options = Options()

        # Добавляем параметры:
        chrome_options.add_argument("--start-maximized")  # Открыть на весь экран
        chrome_options.add_argument("--disable-notifications")  # Отключить уведомления
        chrome_options.add_argument("--incognito")  # Режим инкогнито
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Скрыть статус автоматизации

        # Инициализируем драйвер с настройками
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        driver.implicitly_wait(50)
        driver.maximize_window()

        page = driver

        wait = WebDriverWait(page, 5)

        page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys(f'{workspace}')

        page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'{userLog}')

        page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(f'111111')

        page.find_element(By.XPATH, '//div[text()="Log in"]').click()

        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="page-block mood-block col"]')))

            moodBlock = page.find_element(By.XPATH, '//div[@class="page-block mood-block col"]')

            print(moodBlock)

            if moodBlock:
                num = randint(1, 1)

                print(f'Рандомное число для оценки настроения {num}')

                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '(//div[@class="rate-cell text-16 semibold f-centered pointer"])[10]')))

                (page.find_element(By.XPATH, f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]').
                 click())
        except:
            print('Муд блок не появился')

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Структура')]")))

        page.find_element(By.XPATH, "//*[contains(text(), 'Структура')]").click()

        time.sleep(2)

        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Административная"]')))

        page.find_element(By.XPATH, '//div[text()="Административная"]').click()

        wait.until(EC.presence_of_all_elements_located((By.XPATH, f'(//div[@class="dropdown-item"])[{self.type}]')))

        page.find_element(By.XPATH, f'(//div[@class="dropdown-item"])[{self.type}]').click()

        for i in range(150):

            try:
                count_dep = '//div[@class="new-dept btn f-centered pointer text-center secondary icon"]'

                num = page.find_elements(By.XPATH, count_dep)

                #print(str(len(num)) + ' количество департаментов в разделе')

                if len(num) == 0:
                    select_num_dep = randint(1, len(num) + 1)
                elif len(num) == 2:
                    select_num_dep = randint(1, len(num) - 1)
                else:
                    select_num_dep = randint(1, len(num))

                print(select_num_dep)

                create_dep = f'(//div[@class="new-dept btn f-centered pointer text-center secondary icon"])[{select_num_dep}]'

                wait.until(EC.presence_of_element_located((By.XPATH, create_dep)))

                time.sleep(2)

                wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card-structure col p0"]')))

                page.find_element(By.XPATH, create_dep).click()

                wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ant-modal-content"]')))

                wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="ant-modal-content"]')))

                wait.until(EC.presence_of_element_located((By.XPATH, '//input')))

                wait.until(EC.element_to_be_clickable((By.XPATH, '//input')))

                page.find_element(By.XPATH, '//input').send_keys(f'{self.name} {i}')

                wait.until(EC.presence_of_element_located((By.XPATH, '//textarea')))

                wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea')))

                page.find_element(By.XPATH, '//textarea').send_keys(f'Это проектный отдел {i} созданный с помощью автотестов')

                wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Сохранить']")))

                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Сохранить']")))

                page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

            except:
                print('Возникла ошибка при создании отдела')


adm = TestCreateDepartament('3', 'Административный отдел')
adm.create_dep()

#funct = TestCreateDepartament('4', 'Функциональный отдел')
#funct.create_dep()

project = TestCreateDepartament('5', 'Проектный отдел')
project.create_dep()
