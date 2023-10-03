import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = f'https://www.zooplus.de/tierarzt/results?animal_99=true'

num_page = 1
browser = webdriver.Firefox()
browser.implicitly_wait(10)

try:
    browser.get(URL + '&page=' + str(num_page))
    elem = browser.switch_to.active_element.find_element(By.XPATH,
                                                         "/html/body/div[2]/div[3]/div/div/div[2]/div/div/button[2]")
    if elem:
        elem.click()

    print('Click!')
except Exception as exc:
    print(exc)
finally:
    time.sleep(10)
    browser.close()
    browser.quit()
