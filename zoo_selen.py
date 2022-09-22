import pprint

import requests
import time
import csv


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

HOST = 'https://www.zooplus.de'
URL = 'https://www.zooplus.de/tierarzt/results'


def get_html(url=URL):

    # options = webdriver.ChromeOptions()
    # ua = UserAgent()
    # options.add_argument(ua.google)
    # options.add_argument("--disable-notifications")
    #options.add_argument('headless')  # запуск браузера у фоні
    # browser = webdriver.Chrome(chrome_options=options)

    # start browser without options
    browser = webdriver.Chrome()

    headers = {

        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjExNzM1NTksImlh',
        'cache-control': 'no-cache',
        'referer': 'https://www.zooplus.de/tierarzt/results?animal_99=true',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-api-authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjExNzM1NTksImlhdCI6MTY2MTE3MjY1OX0.ZFUNRoBLXah_riMwrnxCsq9wjNTouEyMS_P8msgrzAA',
    }

    try:
        browser.get(url)
        # Operation with cookies
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div/div/button[2]"))).click()
        time.sleep(5)
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/main/div/div[3]/div[1]/section/div[1]/fieldset/div/div[1]/div[1]/label/input"))).click()
        time.sleep(5)

        elems = browser.find_elements(By.CLASS_NAME, 'result-intro ')
        get_data = []
        for elem in elems:
            try:
                title = elem.find_element(By.CLASS_NAME, 'result-intro__title')
                print(title.text)
                rating = elem.find_element(By.CLASS_NAME, 'result-intro__rating__note')
                print(rating.text)
                description = elem.find_element(By.CLASS_NAME, 'result-intro__subtitle')
                print(description.text)

                working_time = elem.find_element(By.CLASS_NAME, 'daily-hours__range')
                print(working_time.text)
                working_time_note = elem.find_element(By.CLASS_NAME, 'daily-hours')
                print(working_time_note.text)
                address = elem.find_element(By.CLASS_NAME, 'result-intro__address')
                print(address.text)
            except Exception:
                continue


            # output_file = open('output_data.csv', 'w', newline='')
            # output_writer = csv.writer(output_file)
            # output_writer.writerow(elem_text)
            # output_file.close()

        #print(get_data)

    except Exception as ex:
        print(ex)
    finally:
        print('Done!')
        browser.implicitly_wait(30)
        browser.close()
        browser.quit()


def main(url):
    get_html(url)


if __name__ == '__main__':
    main(URL)
