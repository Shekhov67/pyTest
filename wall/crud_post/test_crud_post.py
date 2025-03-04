import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from random import randint
from TestSuites.smoke.test_module import url


@pytest.fixture()
def workspace():
    client = 'pytest'
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
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(url)
    return driver

def test_crudPostsNewsline(page, workspace, userLog, password):
    #createText - переменная для ввода текста в создаваеммом посте
    createText = 'AutoPyTest2'

    updateText = 'updateTextPyTest'

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

            page.find_element(By.XPATH,
                              f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]').click()
    except:
        print('Муд блок не появился')

    page.find_element(By.XPATH, "//*[contains(text(), 'Стена')]").click()

    page.find_element(By.XPATH, "//div[text()='Лента событий']").click()

    try:
        #posts = '//div[@class="btn f-centered pointer open-action-button icon text-center small"]'

        posts = page.find_elements(By.XPATH, '//div[@class="btn f-centered pointer open-action-button icon text-center small"]')

        count_posts = len(posts)

        print(count_posts)

        for i in range(1, count_posts+1):

            page.find_element(By.XPATH, '//div[@class="btn f-centered pointer open-action-button icon text-center small"]').click()
            page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[5]').click()
            print('Удаление постов')

            time.sleep(3)

    except:
        print('Нет постов')

    (page.find_element(
        By.XPATH, "//textarea[@placeholder ='Напишите текст сообщения. Используйте @, чтобы кого-то упомянуть']").
     click())

    (page.find_element(
        By.XPATH, "//textarea[@placeholder ='Напишите текст сообщения. Используйте @, чтобы кого-то упомянуть']").
     send_keys(createText))

    page.find_element(By.XPATH, "//div[text()='Опубликовать']").click()

    page.refresh()

    page.find_element(By.XPATH, '//div[@class="btn f-centered pointer open-action-button icon text-center small"]').click()

    page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[3]').click()

    #gettext = page.find_element(By.XPATH, f"//div[text()='{createText}']").text

    #assert gettext == createText, "Текст поста на стене != текст открытого поста"

    time.sleep(5)

    page.find_element(By.XPATH, '//div[@class="btn f-centered pointer open-action-button icon text-center small"]').click()

    page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[4]').click()

    page.find_element(By.CSS_SELECTOR, ".input-wrapper").click()

    page.find_element(By.XPATH, "(//textarea)[2]").clear()

    page.find_element(By.XPATH, "(//textarea)[2]").send_keys(updateText)

    page.find_element(By.XPATH, '//div[@class="btn f-centered pointer primary text-center"]').click()

    time.sleep(3)

    gettext2 = page.find_element(By.XPATH, f"//div[text()='{updateText}']").text

    assert gettext2 == updateText, "Обновленный текст не совпадает"

    page.find_element(By.XPATH, "//div[text()='Назад в ленту']").click()

    gettext3 = page.find_element(By.XPATH, f"//div[text()='{updateText}']").text

    assert gettext3 == updateText, "Проверка обновленного поста на стене"

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    icon_delete = page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[5]')

    icon_delete.click()

    page.close()

    page.quit()

def test_crudPostsNewsCompany(page, workspace, userLog, password):
    #createText - переменная для ввода текста в создаваеммом посте
    createText = 'AutoPyTest2NewsCompany'

    updateText = 'updateTextPyTestNewsCompany'

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

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Новости компании']")))

    page.find_element(By.XPATH, "//div[text()='Новости компании']").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-checkbox'])[2]")))

    page.find_element(By.XPATH, "(//span[@class='ant-checkbox'])[2]").click()

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

    page.find_element(By.XPATH, "//div[text()='Назад на стену компании']").click()

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

    assert alertDeletedPost == "Пост удален", " Проверка алерта удаления поста "

def test_crudPostGratitudeNewsLine(page, workspace, userLog, password):
    # createText - переменная для ввода текста в создаваеммом посте
    createText = 'AutoPyTest2postGratitudeNewsLine'

    updateText = 'updateTextPyTestpostGratitudeNewsLine'

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

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Лента событий']")))

    page.find_element(By.XPATH, "//div[text()='Лента событий']").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-checkbox'])[1]")))

    page.find_element(By.XPATH, "(//span[@class='ant-checkbox'])[1]").click()

    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//textarea[@placeholder='Упомяните того, кого ходите отблагодарить']")))

    (page.find_element(By.XPATH, "//textarea[@placeholder='Упомяните того, кого ходите отблагодарить']").
     send_keys('@Анд'))

    #wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-mentions-measure']")))

    page.find_element(
        By.XPATH, "//div[@class='ant-mentions-dropdown  ant-mentions-dropdown-placement-bottomRight']/ul/li").click()

    (page.find_element(By.XPATH, "//textarea[@placeholder ='Упомяните того, кого ходите отблагодарить']").
     send_keys(createText))

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Опубликовать']")))

    page.find_element(By.XPATH, "//div[text()='Опубликовать']").click()

    page.refresh()

    sleep(5)

    user = page.find_element(By.XPATH, '//a[@class="mention-link"]').text

    print(user)

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    page.find_element(By.XPATH, "//*[contains(@d,'13.707Z')]").click()

    sleep(5)

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[1]").click()

    page.find_element(By.XPATH, "//*[contains(@d,'8.31003Z')]").click()

    page.find_element(By.CSS_SELECTOR, ".input-wrapper").click()

    page.find_element(By.XPATH, "(//textarea)[2]").clear()

    page.find_element(By.XPATH, "(//textarea)[2]").send_keys(f'{user}{updateText}')

    page.find_element(By.XPATH, '//div[@class="btn f-centered pointer primary text-center"]').click()

    sleep(5)

    page.find_element(By.XPATH, "//div[text()='Назад в ленту']").click()

    sleep(5)

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    icon_delete = page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[5]')

    icon_delete.click()

    wait.until(EC.element_to_be_clickable
               ((By.XPATH, '//div[@class="ant-notification-notice-message"]')))

    alertDeletedPost = page.find_element(By.XPATH, '//div[text()="Пост удален"]').text

    print(alertDeletedPost)

    assert alertDeletedPost == "Пост удален", " Проверка алерта удаления поста "

def test_crudPostGratitudeNewsCompany(page, workspace, userLog, password):
    # createText - переменная для ввода текста в создаваеммом посте

    createText = 'AutoPyTest2postGratitudeNewsLine'

    updateText = 'updateTextPyTestpostGratitudeNewsLine'

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

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Новости компании']")))

    page.find_element(By.XPATH, "//div[text()='Новости компании']").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-checkbox'])[1]")))

    page.find_element(By.XPATH, "(//span[@class='ant-checkbox'])[1]").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ant-checkbox'])[1]")))

    page.find_element(By.XPATH, "(//span[@class='ant-checkbox'])[1]").click()

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder ='Упомяните того, кого ходите отблагодарить']")))

    (page.find_element(By.XPATH, "//textarea[@placeholder ='Упомяните того, кого ходите отблагодарить']").
     send_keys('@Анд'))

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-mentions-measure']")))

    page.find_element(
        By.XPATH, "//div[@class='ant-mentions-dropdown  ant-mentions-dropdown-placement-bottomRight']/ul/li").click()

    (page.find_element(By.XPATH, "//textarea[@placeholder ='Упомяните того, кого ходите отблагодарить']").
     send_keys(createText))

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Опубликовать']")))

    page.find_element(By.XPATH, "//div[text()='Опубликовать']").click()

    # wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='post-wrapper col py6 px4 gap4 greeting']")))
    #
    # wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='post-wrapper-content']/div/a)[1]")))

    user = page.find_element(By.XPATH, '//a[@class="mention-link"]').text
    #
    # postNameUser = page.find_element(By.XPATH, "//div[@class='post-wrapper-content']").text
    #
    # postGratitudeUser = f"{user} {createText}"
    #
    # wait.until(EC.presence_of_element_located((By.XPATH, f"(//a[text()='{user}'])[1]")))
    #
    # assert postNameUser == postGratitudeUser, "Текст в посте благодраности не совпадет"
    #
    wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'small')])[1]")))

    wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'small')])[2]")))

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@d,'13.707Z')]")))

    page.find_element(By.XPATH, "//*[contains(@d,'13.707Z')]").click()

    # wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='post-wrapper col py6 px4 gap4 greeting']")))
    #
    # wait.until(EC.presence_of_element_located((By.XPATH, f"(//a[text()='{user}'])[1]")))
    #
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='post-wrapper-content']")))
    #
    # gettext = page.find_element(By.XPATH, "//div[@class='post-wrapper-content']").text
    #
    # assert gettext == postGratitudeUser, "Текст поста на стене != текст открытого поста"

    sleep(5)

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

    page.find_element(By.XPATH, "(//textarea)[2]").send_keys(f'{user}{updateText}')

    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="btn f-centered pointer primary text-center"]')))

    page.find_element(By.XPATH, '//div[@class="btn f-centered pointer primary text-center"]').click()

    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{updateText}']")))

    # gettext2 = page.find_element(By.XPATH, f"//div[@class='post-wrapper-content']").text
    #
    # wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='post-wrapper-content']")))
    #
    # postGratitudeUser2 = f'{user}{updateText}'
    #
    # assert gettext2 == postGratitudeUser2, "Обновленный текст не совпадает"

    page.find_element(By.XPATH, "//div[text()='Назад на стену компании']").click()

    # gettext3 = page.find_element(By.XPATH, "(//div[@class='post-wrapper-content'])[1]").text
    #
    # assert gettext3 == postGratitudeUser2, "Проверка обновленного поста на стене"

    page.find_element(By.XPATH, "(//div[contains(@class,'small')])[2]").click()

    icon_delete = page.find_element(By.XPATH, '(//div[@class="dropdown-item"])[5]')

    wait.until(EC.presence_of_element_located((By.XPATH, "(//*[contains(@d, '8.1046')])[1]")))

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(@d, '8.1046')])[1]")))

    icon_delete.click()

    wait.until(EC.element_to_be_clickable
               ((By.XPATH, '//div[@class="ant-notification-notice-message"]')))

    alertDeletedPost = page.find_element(By.XPATH, '//div[text()="Пост удален"]').text

    print(alertDeletedPost)

    assert alertDeletedPost == "Пост удален", " Проверка алерта удаления поста "