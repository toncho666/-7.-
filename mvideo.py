from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time



driver1 = webdriver.Chrome() # создаем экземпляр класса
driver1.get('https://www.mvideo.ru/')

assert 'интернет-магазин' in driver1.title # проверка "а там ли мы оказались"

time.sleep(15)
links = []

# формируем список ссылок на товары
for step in range(1,6):
    try:
        button = driver1.find_element_by_xpath('(//div[@class="accessories-carousel-wrapper"])[2]/a[@class="next-btn sel-hits-button-next"]')
        #button = elem.find_element_by_class_name('next-btn sel-hits-button-next')
        button.click()
        time.sleep(3)
    except Exception as e:
        print(e)
        break

link = driver1.find_elements_by_xpath('(//div[@class="caroufredsel_wrapper"])[3]//li[@class="gallery-list-item"]')
for lnk in link:
    x = lnk.find_element_by_class_name('sel-product-tile-title').get_attribute('href')
    links.append((x))

list = []
dict = {}


for hit_link in links:
    driver1.get(hit_link)
    time.sleep(3)
    link_hit_good = hit_link
    name = driver1.find_element_by_class_name('o-pdp-topic__title').text
    # цену сложно собрать, т.к. два контейнера с ценой, оба называются одинаково (зависит от поля трейдин)
    #price = driver1.find_element_by_xpath('//div[@class="c-zoom__price-info"]//div[@class="c-pdp-price__current sel-product-tile-price"]/text')

    dict['link'] = link_hit_good
    dict['name'] = name
    #dict['price'] = price

    list.append(dict)

print(list)
