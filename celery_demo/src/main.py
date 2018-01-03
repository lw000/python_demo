'''
Created on 2018年1月3日

@author: Administrator
'''

import sys

sys.path.append('./')

from tasks import add  

if __name__ == '__main__':
    r = add.delay(2, 2)
    print(r.ready())
    print(r.result)
