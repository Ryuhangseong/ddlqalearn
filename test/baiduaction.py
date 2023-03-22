'''
Author: ryuhangseong liuhangcheng2002@gmail.com
Date: 2023-03-22 16:31:04
LastEditors: ryuhangseong liuhangcheng2002@gmail.com
LastEditTime: 2023-03-22 17:51:23
FilePath: \ddlqalearn\test\baiduaction.py
Description: 

Copyright (c) 2023 by liuhangcheng2002@gmail.com, All Rights Reserved. 
'''

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sele_po.elementoperator import ElementOperator

class Action(ElementOperator):
    
    def __init__(self):
        super(Action, self).__init__(self)

if __name__ == '__main__':
    action = Action()
    action.test()
    print('Test clear')
    print('That\'s all')