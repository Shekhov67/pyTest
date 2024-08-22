from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def workspace():
    client = 'pytest'
    return client
@pytest.fixture()
def userLog():
    user = 'i2@gmail.com'
    return user
@pytest.fixture()
def password():
    passw = '111111'
    return passw

@pytest.fixture()
def page():
    ''' Переход на страницу портала '''
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    #driver.get("https://connectable.site/")
    driver.get("https://staging.connectable.site/")
    return driver

def test_completing_poll_open(page, workspace, userLog, password):

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

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Опросы')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Опросы')]").click()

    page.find_element(By.XPATH, "//input[@placeholder='Искать']").send_keys('открытый')

    page.find_element(By.XPATH, "(//a[@class=''])[1]").click()

    try:

        page.find_element(By.XPATH, "//div[text()='Пройти опрос']").click()

    except:
        print(f"Пользователь {userLog} проходил опрос")
        page.close()

    ##Кнопка следующий вопрос

    nxt = page.find_element(By.XPATH, "//div[text()='Следующий вопрос']")

    (page.find_element(By.XPATH, "//input[@type='text']").
     send_keys(f"Ответ на первый вопрос. Отвечал {userLog}"))

    nxt.click()

    (page.find_element(By.XPATH, '//textarea[@class="ant-input"]').
     send_keys(f"Ответ на второй вопрос.Отвечал {userLog}"))

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

def test_completing_poll_close(page, workspace, userLog, password):

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

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Опросы')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Опросы')]").click()

    page.find_element(By.XPATH, "//input[@placeholder='Искать']").send_keys('закрытый')

    page.find_element(By.XPATH, "(//a[@class=''])[1]").click()

    try:

        page.find_element(By.XPATH, "//div[text()='Пройти опрос']").click()

    except:
        print(f"Пользователь {userLog} проходил опрос")
        page.close()
    ##Кнопка следующий вопрос

    nxt = page.find_element(By.XPATH, "//div[text()='Следующий вопрос']")

    (page.find_element(By.XPATH, "//input[@type='text']").
     send_keys(f"Ответ на первый вопрос. Отвечал {userLog}"))

    nxt.click()

    (page.find_element(By.XPATH, '//textarea[@class="ant-input"]').
     send_keys(f"Ответ на второй вопрос.Отвечал {userLog}"))

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

def test_completing_poll_anonim(page, workspace, userLog, password):

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

    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Опросы')]")))

    page.find_element(By.XPATH, "//*[contains(text(), 'Опросы')]").click()

    page.find_element(By.XPATH, "//input[@placeholder='Искать']").send_keys('анонимный')

    page.find_element(By.XPATH, "(//a[@class=''])[1]").click()

    try:

        page.find_element(By.XPATH, "//div[text()='Пройти опрос']").click()

    except:
        print(f"Пользователь {userLog} проходил опрос")
        page.close()

    ##Кнопка следующий вопрос

    nxt = page.find_element(By.XPATH, "//div[text()='Следующий вопрос']")

    (page.find_element(By.XPATH, "//input[@type='text']").
     send_keys(f"Ответ на первый вопрос. Отвечал {userLog}"))

    nxt.click()

    (page.find_element(By.XPATH, '//textarea[@class="ant-input"]').
     send_keys(f"Ответ на второй вопрос.Отвечал {userLog}"))

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