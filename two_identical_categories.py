from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import Counter
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=options, executable_path="./chromedriver")
driver.get("http://qa-assignment.oblakogroup.ru/board/:id_nikita_burtsev")
driver.find_element_by_xpath('//*[@id="add_new_todo"]/img').click()
driver.find_element_by_xpath('//*[@id="select2-select_category-container"]').click()
drop_down = driver.find_element_by_xpath('//*[@id="select2-select_category-results"]')
categorys = drop_down.find_elements_by_tag_name("li")
for category in categorys:
    if category.text == 'Создать новый список':
        category.click()
name = driver.find_element_by_xpath('//*[@id="project_title"]')
name.click()
name.send_keys('дедушка')
driver.find_element_by_xpath('//*[@id="submit_add_todo"]').click()
driver.find_element_by_xpath('//*[@id="add_new_todo"]/img').click()
driver.find_element_by_xpath('//*[@id="select2-select_category-container"]').click()
drop_down = driver.find_element_by_xpath('//*[@id="select2-select_category-results"]')
categorys = drop_down.find_elements_by_tag_name("li")
for category in categorys:
    if category.text == 'Создать новый список':
        category.click()
name1 = driver.find_element_by_xpath('//*[@id="project_title"]')
name1.click()
name1.send_keys('дедушка')
driver.find_element_by_xpath('//*[@id="submit_add_todo"]').click()
all_to_dos = driver.find_element_by_xpath('//*[@id="main_content_container"]/div[2]')
found_to_dos = all_to_dos.find_elements_by_tag_name('h2')
c = Counter(found_to_dos)
print(c)
#for i in found_to_dos:
#    if found_to_dos == found_to_dos:
#        print('test is fouled')


