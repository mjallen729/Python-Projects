from selenium import webdriver
import time

url = 'https://app.ens.domains/search/'
avail_xpath = '//*[@id="root"]/div/main/a/div[1]/div'

ops = webdriver.ChromeOptions()  # declare options object for driver
ops.add_argument('headless')  # force chrome window not to open when running

driver = webdriver.Chrome(
    '/Users/Matthew/Documents/workspace/PyStuff/ETH Domain Scan/chromedriver',
    options= ops)

words = open('1000MostCommonWords.txt', 'r')  # list of names to scan

available = set()

start = time.time()
for word in words:
    ws = word.rstrip('\n')

    if len(ws) > 2:
        driver.get(url + ws)
    
    else:
        continue
    
    time.sleep(2)

    try:
        if driver.find_element_by_xpath(avail_xpath).text == 'Available':
            available.add(ws)
    
    except:
        continue

print(available)
print('Took: ' + str(round(time.time() - start, 10)))