#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年12月14日

@author: Administrator
'''

import pymysql
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d]',
                    datefmt='%a, %d %b %Y %H:%M:%S')  # ,filename='mysql_demo.log'


def main():
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='localhost', user='lw', passwd='qazxsw123',
                               db='app_project', port=3306, charset='utf8')
#         cur = conn.cursor()  # 获取一个游标
        cur = conn.cursor(pymysql.cursors.DictCursor)  # 获取一个游标
#         cur.execute('select * from user where name=%s', ('李伟',))
        cur.execute('select * from user')
        data = cur.fetchall()
        for d in data:
#             logging.debug('id:%d,name:%s,sex:%d,position:%d,wages:%.2f,average_wages:%.2f,department:%d ' % (
#                 d[0], d[1], d[2], d[3], d[4], d[5], d[6]))
            logging.debug('id:%d,name:%s,sex:%d,position:%d,wages:%.2f,average_wages:%.2f,department:%d ' % (
                            d['id'],d['name'], d['sex'], d['position'], d['wages'], d['average_wages'], d['department']))
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
    except Exception:
        print('查询失败')


if __name__ == '__main__':
    main()
