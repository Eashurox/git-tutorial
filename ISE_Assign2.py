from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

usr ='cs19s501@iittp.ac.in'
pwd='r@doswiss004'

options = Options()
driver = webdriver.Chrome(r"/usr/local/bin/chromedriver",chrome_options=options)
driver.get('https://github.com/login')

username_box= driver.find_element_by_id('login_field')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)

login_box = driver.find_elements_by_class_name('btn-block')
login_box[0].click()

search = driver.find_element_by_name("q")
search.send_keys('text editor')
search.send_keys(Keys.ENTER)
f2 = open(os.path.join(r'/home/eashu/git practice/reponame.text'),"w")

for i in range(1,11):
    name = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(i)+"]/div[2]/div[1]/a")
    f2.write(name.text)
    f2.write("\n")
    
f2.close()
