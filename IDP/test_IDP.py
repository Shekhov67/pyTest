import re
import random
from playwright.sync_api import Page, expect
from TestSuites.smoke.test_module import url

def test_IDP(page: Page):
    page.goto(url)

    page.get_by_role("textbox", name="E-mail").click()
    page.get_by_role("textbox", name="E-mail").fill("t2@gmail.com")
    page.get_by_test_id("login-password").click()
    page.get_by_test_id("login-password").fill("111111")
    page.get_by_role("textbox", name="Workspace").click()
    page.get_by_role("textbox", name="Workspace").fill("pytest")
    page.get_by_text("Log in").click()

    page.get_by_text("Планы развития").click()

    try:
        page.wait_for_selector('//div[@class="page-block mood-block col"]', timeout=5000)
        num = random.randint(1, 10)
        page.click(f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]')
        print(f"Оценка настроения: {num}")
    except:
        print("Муд блок не появился")

    page.wait_for_selector("//div[text()='Добавить']")
    page.locator("//div[text()='Добавить']").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("АвтотестИПР")
    page.locator("div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
    page.get_by_role("option", name="Давыд Лапин Специалист по стрижке овец").locator("div").first.click()
    page.locator("div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
    page.get_by_role("textbox").nth(1).fill("лео")
    page.get_by_role("textbox").nth(1).press("Enter")
    page.get_by_text("Сохранить").click()
    page.get_by_role("link", name="АвтотестИПР").click()

    page.locator("//div[text()='Добавить']").click()
    page.get_by_text("Сохранить").click()
    page.get_by_text("Редактировать").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("АвтотестИПР!!!")
    page.get_by_text("Сохранить").click()

    page.get_by_role("tab", name="Заметки").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("Тест")
    page.get_by_text("Отправить").click()

    page.get_by_role("tab", name="Журнал изменений").click()
    page.get_by_text("Данные изменены").click()
    page.get_by_text("Изменено поле \"Название\"").click()
    page.get_by_text("Создание ИПР").click()
    page.get_by_text("Добавлена задача").click()
    page.get_by_text("Добавлен комментарий").click()

    page.get_by_role("tabpanel").get_by_text("Новый шаг ИПР").click()
    page.get_by_role("tabpanel").get_by_text("Тест").click()

    page.get_by_text("Исполнитель").click()
    page.get_by_text("Наблюдатель").click()
    page.locator("div").filter(has_text=re.compile(r"^Дата создания$")).click()

    page.get_by_role("tab", name="Задачи").click()
    page.get_by_text("Завершить").click()
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_text("Завершено").click()

    assert page.wait_for_selector("//div[text()='Все задачи завершены']", timeout=5000), \
        'Отсутствует подтверждение завершения ИПР (все задачи завершены)'

    page.get_by_text("Все задачи завершены Завершить весь ИПР? Подтвердить").click()
    page.get_by_text("Подтвердить").click()
    page.get_by_role("tab", name="Журнал изменений").click()
    page.get_by_text("Задача была завершена").click()
    page.get_by_text("План развития завершен").click()

    page.get_by_text("Удалить").click()
    page.get_by_role("button", name="Подтвердить").click()
    assert page.get_by_text("No data"), 'Таблица ИПР не пустая, ИПР не удален'