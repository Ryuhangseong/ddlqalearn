
import os
import sys
import socket
import time
import re
import shutil
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
        return print(u'Chromedriver服务已启动')
        
    def open(self, driver: webdriver):
        driver = driver.lower()
        try:
            socket.setdefaulttimeout(50)
            if driver == 'chrome':
                self.driver = webdriver.Chrome(service=chromedriver)
            print(u'浏览器启动成功')
        except Exception as e:
            print(f'浏览器启动失败：{e}')
            raise Exception(e)
        return self.driver
    
    def implicitly_wait(self, num: int):
        self.driver.implicitly_wait(num)
        return print(f'隐式等待时间设置为：{num}秒')
        
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
        if os.path.exists(f'{os.getcwd()}/screenshot/{filename}'):
            os.remove(f'{os.getcwd()}/screenshot/{filename}')
            print(f'已删除同名的{filename}文件')
        shutil.move(f'{filename}', f'{os.getcwd()}/screenshot/{filename}')
        return print(f'名为{filename}的截图已保存至screenshot目录下')
    
    def wait_page_load(self, timeout: int, time: int):
        try:
            WebDriverWait(self.driver, timeout, time).until(lambda d: d.execute_script("return document.readyState"))
        except Exception as e:
            raise Exception(e)
        
    def wait_element_visible(self, timeout: int, time: int, locator):
        ele = WebDriverWait(self.driver, timeout, time).until(EC.visibility_of_element_located(locator))
        return ele
    
    def close(self):
        try:
            self.driver.close()
            return print(u'网页已关闭')
        except Exception as e:
            raise Exception(e)
        
    def find_element(self, by, locate):
        web_ele = self.driver.find_element(by, locate)
        return web_ele
    
    def send_keys(self, by, locate, string: str):
        self.find_element(by, locate).send_keys(string)
        return print(f'已输入：{string}')
    
    def click(self, by, locate):
        self.find_element(by, locate).click()
    
    def get_current_handle(self):
        print(u'已获取当前标签页的句柄')
        return self.driver.current_window_handle
        
    def get_all_handles(self):
        print(u'已获取全部标签页的句柄')
        return self.driver.window_handles
        
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)
        return print(u'已切换到所要求的页面')
    
    def switch_to_iframe(self, iframe: str):
        self.driver.switch_to.frame(iframe)
        return print(u'已切换到所要求的表单')
    
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        return print(u'已回到最外层页面')
    
    def print_text(self, by, locate):
        return print(f'{self.find_element(by, locate).text}')
    
    def execute_script(self, js: str):
        try:
            self.driver.execute_script(js)
        except Exception as e:
            raise Exception(e)
        
    