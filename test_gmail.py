

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

usrName = 'jeevithadc14@gmail.com'
pssWrd = "password2941"

#river.maximize_window()

driver.get("https://www.linkedin.com")
#actions = ActionChains(driver)

driver.find_element_by_xpath('//*[@id="login-email"]').send_keys(usrName)
# driver.send_keys(usrName)
driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(pssWrd)
#driver.send_keys(pssWrd)
driver.find_element_by_id('login-submit').click()

driver.find_element_by_id("notifications-tab-icon").click()

time.sleep(5)
driver.find_element_by_id("mynetwork-tab-icon").click()
time.sleep(5)
driver.find_element_by_css_selector("#nav-settings__dropdown-trigger").click()
driver.implicitly_wait(5)
driver.find_element_by_class_name("block ember-view").click()

