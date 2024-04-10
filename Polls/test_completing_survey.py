from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def polls():
    poll = ("M14.1399 10.5934C13.7158 11.5964 13.0525 "
            "12.4802 12.2079 13.1676C11.3633 13.855 10.3631 "
            "14.325 9.2949 14.5366C8.22668 14.7481 7.12289 14.6948 "
            "6.08004 14.3813C5.03719 14.0677 4.08703 13.5034 3.31262 "
            "12.7378C2.53822 11.9722 1.96315 11.0286 1.6377 9.98935C1.31225 8.95015 "
            "1.24632 7.84704 1.44568 6.77647C1.64503 5.70591 2.10361 4.70047 2.78131 3.84807C3.45901"
            " 2.99567 4.3352 2.32226 5.33328 1.88672")
    return poll

@pytest.fixture()
def workspace():
    client = 'pytest'
    return client
@pytest.fixture()
def userLog():
    user = 'py1@gmail.com'
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
    driver.get("https://staging.connectable.site/")
    return driver

def test_completing_poll_open(page, workspace, userLog, password, polls):

    wait = WebDriverWait(page, 5)

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys(f'{workspace}')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'{userLog}')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(f'{password}')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    try:
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

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@clip-path="url(#clip0_2208_4701)"]')))

    ##page.find_element(By.XPATH, '//*[@clip-path="url(#clip0_2208_4701)"]').click()

    page.find_element(By.XPATH, '//*[@id="menu-container"]/div[12]/div[1]').click()

    page.find_element(By.XPATH, "//input[@placeholder='Искать']").send_keys('открытый')

    page.find_element(By.XPATH, "(//a[@class=''])[1]").click()

    try:

        page.find_element(By.XPATH, "//div[text()='Пройти опрос']").click()

    except:
        print(f"Пользователь {userLog} проходил опрос")
        end_test(page)

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

def test_completing_poll_close(page, workspace, userLog, password, polls):

    wait = WebDriverWait(page, 5)

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys(f'{workspace}')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'{userLog}')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(f'{password}')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    try:
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

    wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@d="{polls}"]')))

    page.find_element(By.XPATH, '//*[@id="menu-container"]/div[12]/div[1]').click()

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

def test_completing_poll_anonim(page, workspace, userLog, password, polls):

    wait = WebDriverWait(page, 5)

    page.find_element(By.XPATH, '//input[@placeholder="Workspace"]').send_keys(f'{workspace}')

    page.find_element(By.XPATH, '//input[@placeholder="E-mail"]').send_keys(f'{userLog}')

    page.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(f'{password}')

    page.find_element(By.XPATH, '//div[text()="Log in"]').click()

    try:
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

    wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@d="{polls}"]')))

    page.find_element(By.XPATH, '//*[@id="menu-container"]/div[12]/div[1]').click()

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