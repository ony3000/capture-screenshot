import os
import csv
import time
from selenium import webdriver

now = time.strftime('%Y%m%d_%H%M%S')
directory_name = f'screenshots_{now}'

if not os.path.exists(directory_name):
    os.makedirs(directory_name)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--start-maximized')
options.add_argument('--test-type')
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

with open('./capture_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        name = row[0]
        url = row[1]
        driver.get(url)
        driver.save_screenshot(f'{directory_name}/{name}.png')

driver.close()
