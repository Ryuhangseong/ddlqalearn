'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2023-03-24 17:58:33
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2023-03-24 21:53:22
FilePath: \ddlqalearn\test\test_baidu.py
Description: 

Copyright (c) 2023 by liuhangcheng2002@gmail.com, All Rights Reserved. 
'''

import os
import sys
from time import sleep
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = Service(r"D:\Code\github\ddlqalearn\driver\chromedriver.exe")

class TestBaidu(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=chromedriver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        pass
    
    def tearDown(self):
        self.driver.quit()
        pass
    
    def test_baidu(self):
        self.driver.get("https://fsoufsou.com/")
        self.driver.find_element(By.ID, 'search-input').clear()
        self.driver.find_element(By.ID, 'search-input').send_keys('妖梦')
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[1]').click()
        sleep(2)
        
    def test_wait(self):
        self.driver.get("https://fsoufsou.com/")
        sleep(3)
        print("Hello sleep(3)")
        self.driver.find_element(By.ID, 'search-input').clear()
        self.driver.find_element(By.ID, 'search-input').send_keys('妖梦')
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[1]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/a').click()
        sleep(2)
        WebDriverWait(self.driver, 0.5).until(EC.title_contains(u'妖梦'))
        print(u'网页标题含有：“妖梦”')
        sleep(2)
        
if __name__ == '__main__':
    unittest.main()