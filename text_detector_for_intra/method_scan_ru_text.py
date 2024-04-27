import time

from langdetect import detect, DetectorFactory
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def scan_ru_text(page, wait):

    time.sleep(1)

    wait.until(EC.presence_of_element_located((By.XPATH, "//html")))

    text_detection = page.find_element(By.XPATH, "//html").text

    #Переменная для хранения слов которые отображаются на странице
    list_text = text_detection.split()
    #Цикл для поиска русских слов на странице
    for i in range(len(list_text)):

        string_list = list_text[i]

        new_string_list = re.sub(r'[^А-Яа-я]', '', string_list)

        if new_string_list == '':

            continue

        else:

            detect_language = detect(new_string_list.lower())

            if detect_language == 'ru' or detect_language == 'bg':

                print(f'Текст на русском языке: {new_string_list}')

                print(detect_language)

