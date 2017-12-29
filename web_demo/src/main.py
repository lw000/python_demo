'''
Created on 2017年12月29日

@author: Administrator
'''

from bs4 import BeautifulSoup
from selenium import webdriver
import time


if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get('http://vip.jd.com/home.html')
    browser.find_element_by_link_text('账户登陆'.encode()).click()
    browser.find_element_by_id('loginname').send_keys('你的用户名'.encode())
    browser.find_element_by_id('nloginpwd').send_keys('密码'.encode())
    browser.find_element_by_xpath('//*[@id="loginsubmit"]').click()
    time.sleep(1)
    try:
        browser.find_element_by_class_name('sign-in').click()
        print('签到成功')
    except:
        print('不能重复签到，签到失败')