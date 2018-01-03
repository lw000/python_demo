#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年 12月14日

@author: Administrator
'''

import os
import hashlib
import atexit
import time
import profile
import json
import base64
import uuid
from collections import Counter
import cProfile
# from config import Config

from algorithms.sorting import bubble_sort
from algorithms.sorting import quick_sort 

try:
    import cPickle as pickle
except ImportError:
    import pickle


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def list_test():
    s = [11, 33, 22, 55, 44]
    for v in s:
        print(v)
    a = 1
    b = 3
    print(s[a:b])
    print(s.sort())
    print(str(s))
    
    print('bubble_sort: ', bubble_sort.sort(s))
    print('quick_sort: ', quick_sort.sort(s))
    
    xx = [x * x for x in range(10)]
    print(xx)


def dict_test():
    dic = {"name": "liwei", "age": 7}
    print(dic["name"])
    print(dic.get("age"))

    print(json.dumps(dic))

    print(str(dic))
    print(len(dic))

    for k in dic.keys():
        print(k)


def exit_fun(a1, a2):
    print("over: " + a1 + a2)


def test_write():
    f = open("./x.back", mode='wb')
    d = dict(a=1, b=2)
    pickle.dump(d, f)
    f.close()


def test_read():
    f = open("./x.back", mode='rb')
    d = pickle.load(f)
    f.close()
    print("d >>>>>>>>", d)
    return 1, 2, 3


def set_test():
    ssss = set([])

    for i in range(10):
        ssss.add(i)
    for i in range(10):
        ssss.add(i)
    print("ssss: ", ssss)


def createGenerator():
    v = range(10)
    for i in v:
        yield i * i

    
def main():
    atexit.register(exit_fun, a1="111", a2="222")
        
    mygenerator = createGenerator()
    
    for i in mygenerator:
        print(i)
    
    
    lxx = '%s, %d' % ('11111111', 200)
    print(lxx.encode())
    
#     print(os.environ)
#     print(os.getenv("ERLANG_HOME"))

    print(add(10, 20))

    cProfile.run("set_test()")
#     cProfile.run("list_test()")
#     profile.run("dict_test()")
#     profile.run("test_write()")
#     profile.run("test_read()")

    dict_test()
    list_test()
    set_test()
    test_write()
    vvv = test_read()
    print('vvv: ', vvv)

    def f(x, y, z): return x + y + z

    print("f:", f(1, 3, 4))

    t = time.time()
    for i in range(10000):
        v = "111111111".join("222222222222222222222").join(str(i))
    print("t: ", time.time() - t)

    t1 = time.time()
    for i in range(10000):
        v = "111111111" + "222222222222222222222" + str(i)
    print("t1: ", time.time() - t1)

#     raise "11111111111111"

    print("李伟")
    print(hashlib.md5("1111111111".encode()).hexdigest())

#     v = base64.b64encode("11111111111")
#     print(v)

#     print(list(range(100)))

    print(uuid.uuid1())

    c = Counter()
    for v in 'sdfdsfsfhfghertewgtgdfsdfsafwaerehrthhdfgsdfsetsdfdsfsfhfghertewgtgdfsdfsafwaerehrthhdfgsdfset':
        c[v] = c[v] + 1
    print("c: ", c, c['f'])


if __name__ == "__main__":
#     f = open('cfg.cfg', 'r')
#     cfg = Config(f)
#     for m in cfg.messages:
#         s = '%s, %s' % (m.message, m.name)
#         print >> m.stream, s
#         
#     f.close()
    
    main()
