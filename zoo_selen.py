import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

HOST = 'https://www.zooplus.de'
url = 'https://www.zooplus.de/tierarzt/results?animal_99=true&page=1'


def get_html(url=url):
    # start browser without options
    browser = webdriver.Chrome()
    # make dictionary  for list get_data
    all_data = []
    try:
        browser.get(url)
        # Operation with cookies
        WebDriverWait(browser, 20).until(
            ec.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div/div/button[2]"))).click()
        time.sleep(1)
        WebDriverWait(browser, 20).until(
            ec.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[1]/div/div/main/div/div[3]/div[1]/section/div[1]/fieldset/div/div[1]/div[1]/label/input"))).click()
        time.sleep(1)
        # get element with all data
        elems = browser.find_elements(By.CLASS_NAME, 'result-intro ')

        # get value from list of elems
        for elem in elems:
            # make empty list and record data elements
            get_data = []
            empty_string = ''
            title = elem.find_element(By.CLASS_NAME, 'result-intro__title')
            get_data.append(title.text)
            rating = elem.find_element(By.CLASS_NAME, 'result-intro__rating__note')
            get_data.append(rating.text)
            try:
                description = elem.find_element(By.CLASS_NAME, 'result-intro__subtitle')
                get_data.append(description.text)
            except IndexError:
                get_data.append(empty_string)

            try:
                working_time = elem.find_element(By.CLASS_NAME, 'daily-hours__range')
                get_data.append(working_time.text)
            except IndexError:
                get_data.append(empty_string)

            try:
                working_time_note = elem.find_element(By.CLASS_NAME, 'daily-hours__note').text
                get_data.append(working_time_note)
            except IndexError:
                get_data.append(empty_string)

            address_text = elem.find_element(By.CLASS_NAME, 'result-intro__address').text
            address = address_text.replace('\n', '')
            get_data.append(address)
            print(get_data)
            # record list 'get_data' in dict 'all_data'
            all_data.append(get_data)

    except Exception as ex:
        print(ex)
    finally:
        print('Done!')
        time.sleep(10)
        browser.close()
        browser.quit()

    return all_data


def save_csv(data):
    """create and record CSV-file"""
    csv_file = open('output_data.csv', 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)
    csv_file.close()


def main():
    data = get_html(url)
    save_csv(data)


if __name__ == '__main__':
    main()

