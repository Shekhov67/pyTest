import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint

class TestAdaptation():
    def __init__(self, type_role):
        self.client = 'pytest'
        self.user = 't2@gmail.com'
        self.passw = '111111'
        self.role = type_role
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()
        self.driver.get("https://staging.connectable.site/")
        # self.driver.get("https://connectable.site/")

    def test_create(self):

        page = self.driver

        wait = WebDriverWait(page, 5)

        page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys(self.client)

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

        page.find_element(By.XPATH, "//*[contains(text(), 'Адаптация')]").click()

        btn_create = page.find_element(By.XPATH, "//div[text()='Добавить трек']")

        if btn_create.is_displayed():

            btn_create.click()

            page.find_element(By.XPATH, "//input").send_keys('Тестовая питон-адаптация')

            page.find_element(By.XPATH, "//textarea").send_keys('Описание тестовой питон-адаптации')

            page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        else:
            print('Кнопка Добавить трек отсутствует, пользователь не админ')

        #notification_create_adaptation = page.find_element(By.XPATH, "//div[text()='Новый трек успешно создан']")

        #wait.until(EC.visibility_of(notification_create_adaptation))

        ##assert notification_create_adaptation.is_displayed()

        page.find_element(By.XPATH, "(//div[@class='btn f-centered pointer secondary icon text-center'])[1]").click()

        window_setting_adaptation = page.find_element(By.XPATH, "//div[text()='Настройки модуля адаптации (онбординга)']")

        wait.until(EC.visibility_of(window_setting_adaptation))

        assert window_setting_adaptation.is_displayed()

        page.find_element(By.XPATH, "(//div[text() = 'Выберите сотрудников'])[1]").click()

        user_checkbox_1 = page.find_element(By.XPATH, '(//input[@type = "checkbox"])[1]')

        user_checkbox_1.click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        page.find_element(By.XPATH, '//button[@class="ant-modal-close"]').click()

        page.find_element(By.XPATH, "(//div[@class='btn f-centered pointer secondary icon text-center'])[1]").click()

        page.find_element(By.XPATH, "//div[text()='HR-специалисты']").click()

        page.find_element(By.XPATH, "(//div[text() = 'Выберите сотрудников'])[2]").click()

        user_checkbox_2 = page.find_element(By.XPATH, '(//input[@type = "checkbox"])[2]')

        user_checkbox_2.click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        page.find_element(By.XPATH, '//button[@class="ant-modal-close"]').click()

        page.find_element(By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center"])[3]').click()

        page.find_element(By.XPATH, "(//div[text()='Выберите из списка'])[1]").click()

        page.find_element(By.XPATH, '//li[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]').click()

        page.find_element(By.XPATH, "(//div[text()='Выберите из списка'])[2]").click()

        page.find_element(By.XPATH, '//li[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]').click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        page.quit()
    def create_steps(self):

        page = self.driver

        wait = WebDriverWait(page, 10)

        page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys(self.client)

        page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys('t2@gmail.com')

        page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('111111')

        page.find_element(By.XPATH, '//div[text()="Log in"]').click()

        page.find_element(By.XPATH, "//*[contains(text(), 'Адаптация')]").click()

        page.find_element(By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center"])[3]').click()

        page.find_element(By.XPATH, "//div[text()='Сценарий']").click()

        time.sleep(10)

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()
        ######Создание этапов и шагов сценария новичка
        page.find_element(By.XPATH, "//div[text()='Добавить этап']").click()

        page.find_element(By.XPATH, '//input[@placeholder="Введите название этапа сценария"]').send_keys(f'Первый этап {self.role}')

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        page.find_element(By.XPATH, "//div[text()='Добавить этап']").click()

        page.find_element(By.XPATH, '//input[@placeholder="Введите название этапа сценария"]').send_keys(f'Второй этап {self.role}')

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        page.find_element(By.XPATH, "//div[text()='Добавить этап']").click()

        page.find_element(By.XPATH, '//input[@placeholder="Введите название этапа сценария"]').send_keys(f'Третий этап {self.role}')

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()
        ##ШАГИ
        page.find_element(By.XPATH, "(//div[text()='Добавить шаг'])[1]").click()

        page.find_element(By.XPATH, '//input[@placeholder="Новый шаг"]').send_keys(f'Первый шаг {self.role}(увед. вкл.)')

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        page.find_element(By.XPATH, "(//div[text()='Добавить шаг'])[1]").click()

        page.find_element(By.XPATH, '//input[@placeholder="Новый шаг"]').send_keys(f'Первый шаг {self.role}(увед. выкл.)')

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.find_element(By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center small"])[2]').click()

        page.find_element(By.XPATH, '//input[@type="checkbox"]').click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        page.find_element(By.XPATH, "(//div[text()='Добавить шаг'])[2]").click()

        page.find_element(By.XPATH, '//input[@placeholder="Новый шаг"]').send_keys(f'Второй шаг {self.role}(увед. вкл.)')

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()
        # Выставить срок задачи на 1 день
        page.find_element(By.XPATH, f"//div[text()='Второй шаг {self.role}(увед. вкл.)']").click()

        page.find_element(By.XPATH, '(//div[@class="one-line text-link pointer"])[3]').click()

        wait.until(EC.invisibility_of_element((By.XPATH, "//span[text()='Шаг добавлен успешно']")))

        page.find_element(By.XPATH, "//div[text()='Изменить']").click()

        page.find_element(By.XPATH, "//div[text()='Сроки']").click()

        page.find_element(By.XPATH, '//span[@class="ant-input-number-handler ant-input-number-handler-down "]').click()

        page.find_element(By.XPATH, '//span[@class="ant-input-number-handler ant-input-number-handler-down "]').click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()
        ###
        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        page.find_element(By.XPATH, "(//div[text()='Добавить шаг'])[3]").click()

        page.find_element(By.XPATH, '//input[@placeholder="Новый шаг"]').send_keys(f'Третий шаг {self.role}(увед. вкл.)')

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        page.find_element(By.XPATH, "(//div[text()='Добавить шаг'])[3]").click()

        page.find_element(By.XPATH, '//input[@placeholder="Новый шаг"]').send_keys(f'Третий шаг {self.role}(увед. выкл.)')

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        page.find_element(By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center small"])[5]').click()

        page.find_element(By.XPATH, '//input[@type="checkbox"]').click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        # Выставить срок задачи на 1 день

        page.find_element(By.XPATH, '(//div[@class="one-line text-link pointer"])[5]').click()

        wait.until(EC.invisibility_of_element((By.XPATH, "//span[text()='Шаг добавлен успешно']")))

        page.find_element(By.XPATH, "//div[text()='Изменить']").click()

        page.find_element(By.XPATH, "//div[text()='Сроки']").click()

        page.find_element(By.XPATH, '//span[@class="ant-input-number-handler ant-input-number-handler-down "]').click()

        page.find_element(By.XPATH, '//span[@class="ant-input-number-handler ant-input-number-handler-down "]').click()
        ##save
        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer primary full text-center"]').click()

        page.find_element(By.XPATH, '//button[@class="ant-modal-close"]').click()

        ###.
        ###Добавление награды(монеты и ачивка)
        edit_1 = page.find_element(By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center small"])[1]')

        edit_1.click()

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[3]').click()  ##нажать на награду в выпадающем меню

        page.find_element(By.XPATH, '//input[@class="ant-input-number-input"]').send_keys('100')

        page.find_element(By.XPATH, '(//div[@class="ant-select-selection__rendered"])[2]').click()

        page.find_element(By.XPATH, '//li[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]').click()

        page.find_element(By.XPATH, "(//div[text()='Сохранить'])[2]").click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        ###Добавление награды(монеты)
        edit_2 = page.find_element(By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center small"])[2]')

        edit_2.click()

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[3]').click()  ##нажать на награду в выпадающем меню

        page.find_element(By.XPATH, '//input[@class="ant-input-number-input"]').send_keys('100')

        page.find_element(By.XPATH, "(//div[text()='Сохранить'])[2]").click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

        ###Добавление награды(ачивки)
        edit_3 = page.find_element(By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center small"])[3]')

        edit_3.click()

        page.find_element(By.XPATH, '//div[@class="btn f-centered pointer secondary icon text-center"]').click()

        page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[3]').click()  ##нажать на награду в выпадающем меню

        page.find_element(By.XPATH, '(//div[@class="ant-select-selection__rendered"])[2]').click()

        page.find_element(By.XPATH, '//li[@class="ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active"]').click()

        page.find_element(By.XPATH, "(//div[text()='Сохранить'])[2]").click()

        page.find_element(By.XPATH, "//div[text()='Сохранить']").click()

        page.refresh()

        page.find_element(By.XPATH, f"//div[text()='{self.role}']").click()

stepsNewUser = TestAdaptation('Новичок')
stepsNewUser.test_create()
stepsNewUser = TestAdaptation('Новичок')
stepsNewUser.create_steps()

stepsMenthorUser = TestAdaptation('Наставник')
stepsMenthorUser.create_steps()

stepsBossUser = TestAdaptation('Руководитель')
stepsBossUser.create_steps()