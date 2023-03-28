'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2023-03-25 14:54:25
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2023-03-26 17:50:33
FilePath: \ddlqalearn\test\test_po.py
Description: 

Copyright (c) 2023 by liuhangcheng2002@gmail.com, All Rights Reserved. 
'''

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sele_po.operator import Operator
from selenium.webdriver.common.by import By
from time import sleep
class TestPO(Operator):
    
    def __init__(self):
        super(TestPO, self).__init__(self)


if __name__ == '__main__':
    fsou = TestPO()
    fsou.start()
    fsou.open('chrome')
    fsou.implicitly_wait(10)
    # fsou.get('https://fsoufsou.com/')
    # fsou.get_title()
    # fsou.get_size()
    # fsou.set_size(800, 600)
    # fsou.set_rect(0, 0, 1920, 1080)
    # fsou.max_window()
    # fsou.min_window()
    # fsou.full_screen_window()
    # fsou.get_screen('1.png')
    # fsou.get('https://www.testclass.cn/')
    # fsou.get_title()
    # fsou.page_back()
    # fsou.refresh()
    # fsou.page_forward()
    fsou.get('https://fsoufsou.com/')
    fsou.wait_page_load(5, 0.5)
    search_input = (By.ID, 'search-input')
    search_button = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[3]/div[1]/div[1]')
    page_ym_baike = (By.LINK_TEXT, '魂魄妖梦 - 萌娘百科')
    fsou.find_element(*search_input)
    fsou.send_keys(*search_input, '妖梦')
    fsou.click(*search_button)
    fsou.wait_page_load(5, 0.5)
    handle_search = fsou.get_current_handle()
    fsou.get_screen('2.png')
    fsou.find_element(*page_ym_baike).click()
    handle_all = fsou.get_all_handles()
    fsou.get_screen('3.png')
    fsou.switch_to_window(handle_all[-1])
    fsou.get_title()
    sleep(2)
    fsou.get_screen('4.png')
    fsou.get('https://www.testclass.cn/test_html/iframe/frameset.html')
    fsou.switch_to_iframe('rightframe')
    fsou.get_screen('5.png')
    fsou.find_element(By.ID, 'performance_test').click()
    fsou.switch_to_default_content()
    fsou.get_screen('6.png')
    fsou.get('https://www.baidu.com')
    js_baidu_display_none = "document.getElementsByName('tj_briicon')[0].style.display='none';"
    fsou.execute_script(js_baidu_display_none)
    sleep(1)
    fsou.get_screen('7.png')
    js_baidu_display_block = "document.getElementsByName('tj_briicon')[0].style.display='block';"
    fsou.execute_script(js_baidu_display_block)
    sleep(1)
    fsou.get_screen('8.png')
    sleep(1)
    briicon = fsou.find_element(By.NAME, 'tj_briicon')
    print(briicon.is_displayed)
    briicon.click()
    sleep(3)
    fsou.close()
    fsou.quit()
    fsou.stop_service()