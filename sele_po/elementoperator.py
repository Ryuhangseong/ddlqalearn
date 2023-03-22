'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2023-03-22 16:33:33
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2023-03-22 17:34:18
FilePath: \ddlqalearn\sele_po\elementoperator.py
Description: 

Copyright (c) 2023 by liuhangcheng2002@gmail.com, All Rights Reserved. 
'''

import os
import sys
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


chromedriver = str(os.getcwd().replace("\\test", "") + "\\driver\\chromedriver.exe")
os.environ["webdriver.chrome.driver"] = chromedriver

class ElementOperator:
    
    def __init__(self, driver):
        self.driver = driver
    
    def test(self):
        if chromedriver:
            print(chromedriver)