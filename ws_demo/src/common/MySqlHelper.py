'''
Created on 2018年1月3日

@author: Administrator
'''

import pymysql

# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库

class MysqlHelper(object):
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='lw', passwd='qazxsw123',
                               db='app_project', port=3306, charset='utf8')
        
    def getConn(self):
        return self.conn