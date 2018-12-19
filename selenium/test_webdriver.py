# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("http://1.1.1.1/login.html")
browser.find_element_by_name('uid').send_keys("temp")
browser.find_element_by_name('pwd').send_keys("temptemp")
browser.find_element_by_name('Login').click()