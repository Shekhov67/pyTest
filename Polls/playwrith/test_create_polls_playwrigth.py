import pytest
from random import randint
from playwright.sync_api import sync_playwright

url = "https://staging.connectable.site/"
passw = "111111"  # импортируй из test_module при необходимости


def login(page):
    page.goto(url)
    page.fill('input[placeholder="Workspace"]', 'pytest')
    page.fill('input[placeholder="E-mail"]', 't2@gmail.com')
    page.fill('input[placeholder="Password"]', passw)
    page.click('text=Log in')


def create_poll(page, poll_type_index: int, name: str, description: str):
    login(page)

    # Пропуск блока настроения
    try:
        page.wait_for_selector('//div[@class="page-block mood-block col"]', timeout=3000)
        num = randint(1, 10)
        page.click(f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]')
    except:
        print("Муд блок не появился")

    page.click("text=Опросы")
    page.wait_for_selector("text=Добавить опрос")
    page.click("text=Добавить опрос")

    # Тип опроса (1 - открытый, 2 - закрытый, 3 - анонимный)
    page.locator(f"(//input[@type='radio'])[{poll_type_index}]").click()

    page.locator("(//input)[1]").fill(name)
    page.locator("textarea").fill(description)

    # Добавление вопросов
    def add_question(q_text, q_type=None, range_text=None, options_count=0):
        page.click("//div[@class='abs']")  # Кнопка +
        page.locator('//input[@placeholder="Например, знаете ли вы, чего от вас ожидает работодатель?"]').nth(-1).fill(q_text)
        if q_type:
            arrow = page.locator("(//span[@class='ant-select-arrow'])").nth(-1)
            arrow.click()
            page.locator(f"//li[text()='{q_type}']").nth(-1).click()
            if range_text:
                page.locator(f"(//span[text()='{range_text}'])").nth(-1).click()
        for _ in range(options_count):
            page.locator('(//*[@class="ant-btn ant-btn-link"])').nth(-1).click()

    add_question("Вопрос первый")
    add_question("Вопрос второй", "Развернутый ответ текстом")
    add_question("Вопрос третий", "Выбор числа в диапазоне", "от 1 до 5")
    add_question("Вопрос четвертый", "Выбор числа в диапазоне", "от 1 до 10")
    add_question("Вопрос пятый", "Выбор числа в диапазоне", "от 1 до 100")
    add_question("Вопрос шестой", "Один вариант из списка", options_count=5)
    add_question("Вопрос седьмой", "Несколько вариантов из списка", options_count=5)

    # Сделать последний вопрос обязательным
    page.locator("(//button[@role='switch'])").nth(-1).click()

    # Сохранить опрос
    save_btn = page.locator("//div[text()='Сохранить']")
    save_btn.scroll_into_view_if_needed()
    save_btn.click()

    page.wait_for_timeout(2000)
    page.close()


@pytest.mark.parametrize("poll_type,name,description", [
    (1, "Открытый опрос", "Описание открытого опроса"),
    (2, "Закрытый опрос", "Описание закрытого опроса"),
    (3, "Анонимный опрос", "Описание анонимного опроса"),
])
def test_create_polls(poll_type, name, description):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        create_poll(page, poll_type, name, description)
        browser.close()