from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

n = 5 # количество писем, которые хотим "собрать"
login = ''
password = ''

driver = webdriver.Chrome() # создаем экземпляр класса
driver.get('https://mail.ru')

assert 'Mail.ru:' in driver.title # проверка "а там ли мы оказались"

# вводим логин и переходим к вводу пароля
elem = driver.find_element_by_id('mailbox:login') # активируем поле "логин"
elem.send_keys(login) # вводим в поле "логин"
time.sleep(1)
elem.send_keys(Keys.ENTER)

# вводим пароль и заходим в почтовый ящик
time.sleep(1)
elem = driver.find_element_by_id('mailbox:password') # активируем поле "ввести пароль"
time.sleep(1)
elem.send_keys(password) # вводим в поле "пароль"
time.sleep(1)
elem.send_keys(Keys.ENTER)

# сканируем письма
# ждем загрузки страницы с письмами
time.sleep(5)

assert 'Входящие' in driver.title # проверка "а там ли мы оказались"

# открываем первое письмо
button = driver.find_element_by_class_name('llc__content')
button.click()

list = []
dict = {}
for i in range(1,n):
    time.sleep(3) # время для подгрузки содержимого письма

    letter = driver.find_element_by_class_name('application')
    sender = letter.find_element_by_class_name('letter__contact-item').text
    date_of_send = letter.find_element_by_class_name('letter__date').text
    subject = letter.find_element_by_class_name('thread__subject').text
    text = letter.find_element_by_class_name('letter-body').text

    dict['sender'] = sender
    dict['date_of_send'] = date_of_send
    dict['subject'] = subject
    dict['text'] = text

    list.append(dict)

    button_next = driver.find_element_by_class_name('portal-menu-element portal-menu-element_next portal-menu-element_expanded portal-menu-element_not-touch')
    button_next.click()
    time.sleep(5)






'''
# теперь нужно попасть в профиль
profile = driver.find_element_by_class_name('avatar') # получаем нужный класс
driver.get(profile.get_attribute('href'))  # выполняем get запрос по ссылке из класса
assert 'Профиль | GeekBrains' in driver.title # проверка "а там ли мы оказались"

# теперь нужно попасть в редактирование профиля
edit_profile = driver.find_element_by_class_name('text-sm')
driver.get(edit_profile.get_attribute('href'))  # выполняем get запрос по ссылке из класса
assert 'Настройки профиля' in driver.title # проверка "а там ли мы оказались"

# теперь нужно изменить дату рождения
date = driver.find_element_by_name('user[birth_date(3i)]') # получаем доступ к нужному полю
#options = date.find_elements_by_tag_name('options') # получаем доступ ко всем тегам "options" внутри класса

select = Select(driver.find_element_by_name('user[birth_date(3i)]')) # создаем экземпляр класса
select.select_by_value('13') # выбираем нужную дату

# теперь нужно сохранить данные
date.submit() #подтверждаем изменение формы
driver.back() #возвращаемся на страницу назад
drive.forward() #переходим на страницу вперед

'''
#driver.quit()