import pytest
from playwright.sync_api import Page, expect, sync_playwright

@pytest.mark.smoke
def test_create_client_user_and_mailing(page: Page):

    # Логин
    page.goto("https://staging.connectable.site/login")
    page.get_by_role("textbox", name="E-mail").fill("w.project.portal3@gmail.com")
    page.get_by_test_id("login-password").fill("111")
    page.get_by_text("Log in").click()
    expect(page.get_by_text("New client")).to_be_visible()

    # Создание клиента
    page.get_by_text("New client").click()
    page.get_by_role("textbox", name="Enter full name", exact=True).fill("autotesting")
    page.get_by_role("textbox", name="Enter short id").fill("auto")
    page.get_by_role("combobox").locator("div").click()
    page.get_by_role("option", name="Русский").click()
    page.get_by_text("Save").click()
    expect(page.get_by_text("Клиент записан")).to_be_visible()
    page.get_by_role("button", name="OK").click()

    # Выбор клиента
    page.get_by_role("table").locator("div").filter(has_text="autotesting auto").first.click()
    page.get_by_role("cell", name="autotesting auto").locator("svg").click()

    # Переход в администрирование
    page.get_by_text("Администрирование").click()
    page.get_by_text("Новый сотрудник").click()

    # Создание сотрудника
    page.get_by_role("textbox", name="Введите имя сотрудника").fill("admin")
    page.get_by_role("textbox", name="Введите фамилию сотрудника").fill("admin")
    page.get_by_role("textbox", name="Подтверждение пароля").fill("111111")
    page.get_by_role("textbox", name="Пароль").fill("111111")
    page.get_by_role("textbox", name="Введите e-mail").fill("t2@gmail.com")
    page.get_by_role("textbox", name="Должность").fill("Admin")
    page.get_by_text("Создать").click()

    # Назначение прав
    page.get_by_role("tab", name="Права и роли").click()
    page.get_by_role("row", name="admin admin Администратор:").get_by_role("switch").click()
    page.get_by_role("button", name="Да").click()

    # Создание рассылки
    page.get_by_text("Админ-панель").click()
    page.get_by_text("Управление клиентами").click()
    page.get_by_text("autotesting").click()
    page.get_by_text("Рассылки").click()
    page.get_by_role("button", name="Добавить рассылку").click()
    page.get_by_label("Редактирование рассылки").get_by_role("combobox").locator("div").click()
    page.get_by_role("option", name="Автоначисления за срок работы").click()
    page.get_by_role("dialog", name="Редактирование рассылки").get_by_role("switch").click()
    page.get_by_role("checkbox", name="По дням").check()
    page.get_by_role("textbox", name="Select time").click()
    page.get_by_role("button", name="09").first.click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("button", name="OK").click()
    page.get_by_label("Изменение данных клиента").get_by_text("Сохранить").click()
    expect(page.get_by_text("Клиент записан")).to_be_visible()
    page.get_by_role("button", name="OK").click()

    # Удаление клиента
    page.get_by_text("autotesting").click()
    page.get_by_text("Удалить").click()
    page.get_by_role("checkbox", name="Подтвердить полное удаление данных клиента").check()
    page.get_by_label("Полное удаление клиента").get_by_text("Сохранить").click()
    page.get_by_text("ОК", exact=True).click()
    page.get_by_role("button", name="OK").click()

    # Выход
    page.get_by_text("Админ Админович").click()
    page.get_by_text("Выйти").click()

