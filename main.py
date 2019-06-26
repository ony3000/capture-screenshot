import os
import csv
import time
from selenium import webdriver

now = time.strftime('%Y%m%d_%H%M%S')
directory_name = f'screenshots_{now}'

if not os.path.exists(directory_name):
    os.makedirs(directory_name)

driver = webdriver.Firefox()
driver.maximize_window()

with open('./capture_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        name = row[0]
        url = row[1]
        driver.get(url)
        time.sleep(1)
        el = driver.find_element_by_tag_name('html')
        el.screenshot(f'{directory_name}/{name}.png')

driver.close()
