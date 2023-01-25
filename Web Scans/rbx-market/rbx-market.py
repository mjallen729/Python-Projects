from selenium import webdriver
from datetime import datetime as dt
from selenium.webdriver.common.by import By

_url = 'https://www.rolimons.com/leaderboard/'
xpath_flexbox = '/html/body/div[3]/div[2]/div[5]'

# Flexbox xpath: //*[@id="page_content_body"]/div[5]/div[1]
# RAP flexpath: /html/body/div[3]/div[2]/div[5]/div[1]/a/div[3]/div[3]/div[2]/span

ops = webdriver.ChromeOptions()
ops.add_argument('headless')
driver = webdriver.Chrome('chromedriver.exe', options= ops)

def compute(page_num):
	driver.get(_url + str(page_num))

	global avg
	avg = 0
	n = 0
	while True:
		try:
			rap = driver.find_element(By.XPATH, xpath_flexbox + f'/div[{n+1}]' +
				f'/a/div[3]/div[3]/div[2]/span').text

			rap = rap[3:].replace(',', '')
			rap = int(rap)

			add_data(rap)

			avg = (avg * n + rap) / (n + 1)
			n += 1

		except Exception as e:
			break

data = list()
def add_data(rap):
	data.add(rap)

# Uses top 250 richest players RAP to compute market average
for i in range(1, 5):
	compute(i)

with open('avg-log.txt', 'a') as log:
	log.write(
		f'{str(dt.now().strftime("%Y-%m-%d %H:%M:%S"))}\t{round(avg / 10000, 2)}\n')

import pandas as pd

df = pd.DataFrame(data)
df.to_csv('rap-data.csv')