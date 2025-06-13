import pytest
from random import randint
from playwright.sync_api import sync_playwright

url = "https://staging.connectable.site/"
num_polls = 25  # количество пользователей

def completing_poll(page, type_poll, index):
    page.goto(url)
    page.wait_for_selector('input[placeholder="Workspace"]', timeout=10000)
    page.screenshot(path=f"screenshots/{index}_1_login_page.png")

    page.fill('input[placeholder="Workspace"]', 'pytest')
    page.fill('input[placeholder="E-mail"]', f'i{index}@gmail.com')
    page.fill('input[placeholder="Password"]', '111111')
    page.click('text=Log in')

    print(f"[{index}] Выполнен логин")
    page.wait_for_timeout(2000)
    page.screenshot(path=f"screenshots/{index}_2_after_login.png")

    try:
        page.wait_for_selector('//div[@class="page-block mood-block col"]', timeout=5000)
        num = randint(1, 10)
        page.click(f'(//div[@class="rate-cell text-16 semibold f-centered pointer"])[{num}]')
        print(f"[{index}] Оценка настроения: {num}")
    except:
        print(f"[{index}] Муд блок не появился")

    try:
        page.wait_for_selector('text=Опросы', timeout=5000)
        page.click('text=Опросы')
        print(f"[{index}] Переход в раздел Опросы")
    except Exception as e:
        print(f"[{index}] Ошибка при переходе в Опросы: {e}")
        page.screenshot(path=f"screenshots/{index}_error_oprosy.png")
        return

    page.wait_for_timeout(2000)
    page.screenshot(path=f"screenshots/{index}_3_polls_list.png")

    try:
        page.wait_for_selector('//input[@placeholder="Искать"]', timeout=5000)
        page.fill('//input[@placeholder="Искать"]', type_poll)
        print(f"[{index}] Поиск по названию опроса: {type_poll}")

        page.wait_for_selector('(//a[@class=""])[1]', timeout=5000)
        page.click('(//a[@class=""])[1]')
        print(f"[{index}] Клик по карточке опроса")
    except Exception as e:
        print(f"[{index}] Опрос не найден: {e}")
        page.screenshot(path=f"screenshots/{index}_error_search_poll.png")
        return

    try:
        page.wait_for_selector('//div[text()="Пройти опрос"]', timeout=5000)
        page.click('//div[text()="Пройти опрос"]')
        print(f"[{index}] Начало прохождения опроса")
    except:
        print(f"[{index}] Пользователь i{index}@gmail.com уже проходил опрос или кнопка не найдена")
        page.screenshot(path=f"screenshots/{index}_poll_already_done.png")
        return

    page.screenshot(path=f"screenshots/{index}_4_poll_started.png")

    # Вопросы
    page.fill('//input[@type="text"]', f"Ответ на 1 вопрос. Пользователь i{index}@gmail.com")
    page.click('//div[text()="Следующий вопрос"]')

    page.fill('//textarea', f"Ответ на 2 вопрос. Пользователь i{index}@gmail.com")
    page.click('//div[text()="Следующий вопрос"]')

    page.click(f'//div[@aria-posinset="{randint(1, 5)}"]')
    page.click('//div[text()="Следующий вопрос"]')

    page.click(f'//div[@aria-posinset="{randint(1, 10)}"]')
    page.click('//div[text()="Следующий вопрос"]')

    # Слайдер
    slider = page.locator('//div[@role="slider"]')
    slider.hover()
    bbox = slider.bounding_box()
    if bbox:
        page.mouse.move(bbox['x'], bbox['y'])
        page.mouse.down()
        page.mouse.move(bbox['x'] + randint(50, 300), bbox['y'], steps=5)
        page.mouse.up()
        print(f"[{index}] Слайдер пройден")
    page.click('//div[text()="Следующий вопрос"]')

    page.click(f'(//input[@type="radio"])[{randint(1, 5)}]')
    page.click('//div[text()="Следующий вопрос"]')

    nums = set()
    while len(nums) < 2:
        nums.add(randint(1, 5))
    for n in nums:
        page.click(f'(//div[@class="radius p4 bg-light-blue pointer hov-blue"])[{n}]')
    page.click('//div[text()="Завершить"]')

    print(f"[{index}] Опрос успешно завершён")
    page.screenshot(path=f"screenshots/{index}_5_poll_finished.png")


@pytest.mark.parametrize("type_poll", ["Открытый", "Закрытый", "Анонимный"])
def test_polls(type_poll):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        import os
        os.makedirs("screenshots", exist_ok=True)

        for i in range(1, num_polls + 1):
            context = browser.new_context()
            page = context.new_page()
            completing_poll(page, type_poll, i)
            context.close()

        browser.close()