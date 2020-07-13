import time
from selenium import webdriver
import requests
from slugify import slugify
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import json


def builder(name, item_id, shop_id):
    name = slugify(name).lower()
    url = "https://shopee.co.id/"+name+"-i."+str(shop_id)+"."+str(item_id)
    urls.append(url)

def search_result(prev):
  headers = {
      'authority': 'shopee.co.id',
      'x-shopee-language': 'id',
      'x-requested-with': 'XMLHttpRequest',
      'if-none-match-': '55b03-3af6e068e58fc66314dfb4654f7b19d6',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61',
      'x-api-source': 'pc',
      'accept': '*/*',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://shopee.co.id/search?keyword=ikan',
      'accept-language': 'en-US,en;q=0.9',
      'if-none-match': '17fadebc3da4efe08ee66fcac6692a12',
  }

  params = (
      ('by', 'relevancy'),
      ('keyword', 'ikan'),
      ('limit', '50'),
      ('newest', prev),
      ('order', 'desc'),
      ('page_type', 'search'),
      ('version', '2'),
  )

  response = requests.get('https://shopee.co.id/api/v2/search_items/', headers=headers, params=params)

  json_data = response.json()

  for item in json_data['items']:
    builder(item['name'],item['itemid'],item['shopid'])

driver = webdriver.Chrome('./chromedriver.exe')
urls = []
products = []

prev = 0
for i in range(99):
    search_result(prev)
    prev+=50

for url in urls:
    driver.get(url)
    time.sleep(7)

    # Fixed 
    try:
        title = driver.find_elements_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span')
        price = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div')
        deskripsi = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span')
        category = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div/a[2]')
        subcategory = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div/a[3]')
        seller = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]')

    except NoSuchElementException: 
        df = pd.DataFrame(products, index=[0])
        df.to_excel("output.xlsx") 

    product = {
        'url' : url,
        'title' : title[0].text,
        'price' : price.text,
        'desc' : deskripsi.text,
        'category' : category.text,
        'subcategory' : subcategory.text,
        'seller' : seller.text
    }
    # Buggy, still have a bug
    try:
        terjual = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div[3]/div[1]')
    except NoSuchElementException:
        terjual = '-'
        product['sold'] = terjual

    try:
        star = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]')
    except NoSuchElementException:
        star = '-'
        product['star'] = star

    try:
        subsubcategory = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div/a[4]')
    except NoSuchElementException:
        subsubcategory = '-'
        product['subsubcategory'] = subsubcategory
    
    try:
        city = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[6]/div')
    except NoSuchElementException:
        city = '-'
        product['city'] = city

    if(subsubcategory != '-'):
        product['subsubcategory'] = subsubcategory.text
    if(city != '-'):
        product['city'] = city.text
    if(terjual != '-'):
        product['sold'] = terjual.text
    if(star != '-'):
        product['star'] = star.text

    products.append(product)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

df = pd.DataFrame(products, index=[0])
df.to_excel("output.xlsx") 

print(df)