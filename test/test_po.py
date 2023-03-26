'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2023-03-25 14:54:25
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2023-03-26 14:54:10
FilePath: \ddlqalearn\test\test_po.py
Description: 

Copyright (c) 2023 by liuhangcheng2002@gmail.com, All Rights Reserved. 
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sele_po.operator import Operator
from selenium.webdriver.common.by import By
class TestPO(Operator):
    
    def __init__(self):
        super(TestPO, self).__init__(self)


if __name__ == '__main__':
    fsou = TestPO()
    fsou.start()
    fsou.open('chrome')
    fsou.implicitly_wait(10)
    fsou.get('https://fsoufsou.com/')
    fsou.get_title()
    fsou.get_size()
    fsou.set_size(800, 600)
    fsou.set_rect(0, 0, 1920, 1080)
    fsou.max_window()
    fsou.min_window()
    fsou.full_screen_window()
    fsou.get_screen('1.png')
    fsou.get('https://www.testclass.cn/')
    fsou.get_title()
    fsou.page_back()
    fsou.refresh()
    fsou.page_forward()
    fsou.get('https://fsoufsou.com/')
    fsou.wait_page_load(5, 0.5)
    search_input = (By.ID, 'search-input')
    fsou.find_element(*search_input)
    fsou.send_keys(*search_input, '妖梦')
    fsou.get_screen('2.png')
    fsou.close()
    fsou.quit()
    fsou.stop_service()