import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from method_scan_ru_text import scan_ru_text

@pytest.fixture()
def workspace():
    client = 'testing1'
    return client
@pytest.fixture()
def userLog():
    user = 't2@gmail.com'
    return user
@pytest.fixture()
def password():
    passw = '111111'
    return passw

@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    #driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://intranetable.team/")
    return driver

def test_text(page, workspace, userLog, password):
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

            (page.find_element(By.XPATH, f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]').
             click())
    except:
        print('Муд блок не появился')

    print('РАЗДЕЛ АДМИНИСТРИРОВАНИЕ /////////////////////////////////////////////////////')

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Administration')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Administration')]").click()

    #Поиск русских слов на странице
    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Company data')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Company data')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Rights and roles')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Rights and roles')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Mood statistic')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Mood statistic')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Other settings')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Other settings')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Notifications')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Notifications')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Notification settings')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Notification settings')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Notification templates')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Notification templates')]").click()

    scan_ru_text(page, wait)

    print('СОЗДАНИЕ НОВОГО ПОЛЬЗОВАТЕЛЯ //////////////////////////////////////////////')

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='New employee']")))

    page.find_element(By.XPATH, "//div[text()='New employee']").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='About']")))

    page.find_element(By.XPATH, "//div[text()='About']").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Social networks']")))

    page.find_element(By.XPATH, "//div[text()='Social networks']").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Personnel documents']")))

    page.find_element(By.XPATH, "//div[text()='Personnel documents']").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Files for HR']")))

    page.find_element(By.XPATH, "//div[text()='Files for HR']").click()

    scan_ru_text(page, wait)

    print('РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЯ //////////////////////////////////////////////')

    page.find_element(By.XPATH, '//button[@class="ant-btn"]').click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'All employees')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'All employees')]").click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//i[@aria-label="icon: edit"]')))

    time.sleep(2)

    action = ActionChains(page)

    edit = page.find_element(By.XPATH, '//i[@aria-label="icon: edit"]')

    action.click_and_hold(edit).move_by_offset(5, 0).click().perform()

    scan_ru_text(page, wait)

    page.find_element(By.XPATH, "//div[text()='Social networks']").click()

    scan_ru_text(page, wait)

    page.find_element(By.XPATH, "(//div[text()='Notifications'])[2]").click()

    scan_ru_text(page, wait)

    page.find_element(By.XPATH, "//div[text()='Personnel info']").click()

    scan_ru_text(page, wait)

    page.find_element(By.XPATH, "//div[text()='HR files']").click()

    scan_ru_text(page, wait)

    page.find_element(By.XPATH, "//div[text()='Cancel']").click()

    scan_ru_text(page, wait)

    print('РАЗДЕЛ АДАПТАЦИЯ //////////////////////////////////////////////')

    page.find_element(By.XPATH, "//*[contains(text(), 'Adaptation')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center"])[3]')))

    page.find_element(By.XPATH, '(//div[@class="btn f-centered pointer secondary icon text-center"])[3]').click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Scenario')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Scenario')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Participants')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Participants')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Polls')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Polls')]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="text-mid-grey"]')))

    page.find_element(By.XPATH, '//*[@class="text-mid-grey"]').click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, '(//*[@class="btn f-centered pointer primary full text-center"])[1]')))

    page.find_element(By.XPATH, '(//*[@class="btn f-centered pointer primary full text-center"])[1]').click()

    scan_ru_text(page, wait)

    print('РАЗДЕЛ ОПРОСЫ //////////////////////////////////////////////')

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Table')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Table')]").click()

    scan_ru_text(page, wait)

    print('РАЗДЕЛ МАГАЗИН //////////////////////////////////////////////')

    page.find_element(By.XPATH, "//*[contains(text(), 'Shop')]").click()

    scan_ru_text(page, wait)

    page.find_element(By.XPATH, "(//*[contains(text(), 'Add')])[2]").click()

    scan_ru_text(page, wait)

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Achievement')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Achievement')]").click()

    scan_ru_text(page, wait)

    page.quit()






