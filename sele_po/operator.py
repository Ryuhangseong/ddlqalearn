
import os
import sys
import socket
import time
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

chromedriver = Service(r'D:\Code\github\ddlqalearn\driver\chromedriver.exe')


class Operator:
    
    def __init__(self, driver: webdriver):
        self.driver = driver
        
    def start(self):
        chromedriver.command_line_args()
        chromedriver.start()
        return print(f'Chromedriver服务已启动')
        
    def open(self, driver: webdriver):
        driver = driver.lower()
        try:
            socket.setdefaulttimeout(50)
            if driver == 'chrome':
                self.driver = webdriver.Chrome(service=chromedriver)
            self.driver.implicitly_wait(10)
            print(u'浏览器启动成功')
        except Exception as e:
            print(f'浏览器启动失败：{e}')
            raise Exception(e)
        return self.driver
    
    def get(self, url):
        self.driver.get(url)
        return print(f'启动网站\"{url}\"成功')
    
    def quit(self):
        self.driver.quit()
        return print(f'已关闭浏览器')
    
    def stop_service(self):
        chromedriver.stop()
        return print(f'Chromedriver服务已停止')
        
    def get_title(self):
        return print(f'当前窗口的标题为：{self.driver.title}')
        
    def get_size(self):
        sizelist = [int(size) for size in re.findall(r'\d+', str(self.driver.get_window_size()))]
        size = str(sizelist).replace('[','').replace(']','')
        return print(f'当前窗口大小为：{size}')
    
    def set_size(self, width, height):
        self.driver.set_window_size(width, height)
        return print(f'当前窗口大小设置为：{width}，{height}')
    
    def set_rect(self, x, y, width, height):
        self.driver.set_window_rect(x, y, width, height)
        return print(f'当前窗口位置大小设置为：{x}，{y}，{width}，{height}')
    
    def max_window(self):
        self.driver.maximize_window()
        return print(f'浏览器最大化成功')
    
    def min_window(self):
        self.driver.minimize_window()
        return print(f'浏览器最小化成功')
    
    def full_screen_window(self):
        self.driver.fullscreen_window()
        return print(f'浏览器全屏化成功')
    
    def page_back(self):
        self.driver.back()
        return print(f'网页已后退')
    
    def page_forward(self):
        self.driver.forward()
        return print(f'网页已前进')
    
    def refresh(self):
        self.driver.refresh()
        return print(f'网页已刷新')
    
    def get_screen(self, filename: str):
        self.driver.save_screenshot(filename)
        return print(f'名为{filename}的截图已保存至/screenshots目录下')