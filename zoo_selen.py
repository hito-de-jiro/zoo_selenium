import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

HOST = 'https://www.zooplus.de'

URL = f'https://www.zooplus.de/tierarzt/results?animal_99=true'


def get_html(url=URL):
    """Starts the browser, receives and returns raw data"""
    # Creating a list to collect raw data
    all_data = []
    num_page = 2
    i = 1
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    while i < num_page + 1:
        browser.get(url + '&page=' + str(i))
        try:
            WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
                (By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div/div/button[2]"))).click()
        except Exception:
            continue

        elems = browser.find_elements(By.CLASS_NAME, 'result-intro ')
        #  get value from list of elems
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
            except Exception:
                get_data.append(empty_string)

            try:
                working_time = elem.find_element(By.CLASS_NAME, 'daily-hours__range')
                get_data.append(working_time.text)
            except Exception:
                get_data.append(empty_string)

            try:
                working_time_note = elem.find_element(By.CLASS_NAME, 'daily-hours__note').text
                get_data.append(working_time_note)
            except Exception:
                get_data.append(empty_string)

            address_text = elem.find_element(By.CLASS_NAME, 'result-intro__address').text
            address = address_text.replace('\n', '')
            get_data.append(address)
            print(get_data)
            # record list 'get_data' in dict 'all_data'
            all_data.append(get_data)

        i += 1

    print('Done!')

    # time.sleep(2)
    browser.close()
    browser.quit()
    return all_data


def save_csv(data):
    """create and record CSV-file"""
    csv_file = open('output_data.csv', 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)
    csv_file.close()


def main(url=URL):
    get_html(url)
    # data = get_html(url)
    # save_csv(data)


if __name__ == '__main__':
    main()
