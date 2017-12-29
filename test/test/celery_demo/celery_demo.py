'''
Created on 2017年12月25日

@author: Administrator
'''
    
from tasks import sendmail
from tasks import add

if __name__ == '__main__':
    add.delay(4, 4)
#     sendmail.delay(dict(to='celery@python.org'))