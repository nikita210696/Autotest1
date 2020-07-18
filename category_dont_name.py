from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
input_todo_name = driver.find_element_by_xpath('//*[@id="project_title"]')
input_todo_name.click()
input_todo_name.send_keys('')
driver.find_element_by_xpath('//*[@id="submit_add_todo"]').click()
all_to_dos = driver.find_element_by_xpath('//*[@id="main_content_container"]/div[2]')
found_to_dos = all_to_dos.find_elements_by_tag_name('h2')
for i in found_to_dos:
    print(i.text)
    assert len(i.text) != 0
