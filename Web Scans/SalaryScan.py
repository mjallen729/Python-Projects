# https://www.levels.fyi/companies/google/salaries/software-engineer
# https://www.levels.fyi/companies/google/salaries/data-scientist
import requests
from selenium import webdriver
import time

ops = webdriver.ChromeOptions()
ops.add_argument('headless')

driver = webdriver.Chrome(
    'G:\workspace\Python\Web Scans\chromedriver.exe', options= ops)


companies = ['apple', 'google', 'amazon', 'facebook', 'netflix', 'uber',
    'doordash', 'lyft', 'microsoft']

swe_url = lambda a: 'https://www.levels.fyi/companies/' + a + '/salaries/software-engineer'
ds_url = lambda a: 'https://www.levels.fyi/companies/' + a + '/salaries/ds'

element = '/html/body/div[1]/div[2]/div/div[3]/div[2]/table/tbody/tr[1]/td[2]/h6'  # class (h6)

avg = 0
num = 0

for com in companies:
    swe = swe_url(com)

    driver.get(swe)

    time.sleep(2)

    try:
        salary = driver.find_element_by_xpath(element).text
        salary = [c for c in salary if c.isnumeric()].join()

        avg *= num
        avg += salary
        num += 1
        avg /= num

    except:
        print('Something went wrong during SWE access: ', com)
        continue

print('Software Engineer: ', avg * 100000)
avg = 0
num = 0

for com in companies:
    ds = ds_url(com)

    driver.get(ds)

    time.sleep(2)

    try:
        salary = driver.find_element_by_xpath(element).text
        salary = [c for c in salary if c.isnumeric()].join()

        avg *= num
        avg += salary
        num += 1
        avg /= num

    except:
        print('Something went wrong during DA access: ', com)
        continue

print('Data Scientist: ', avg * 100000)