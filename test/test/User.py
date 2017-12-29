# -*- coding: UTF-8 -*-

'''
Created on 2017年 12月14日

@author: Administrator
'''
import sys

sys.path.append('./chat')
import chat_pb2

class People(object):
    '''
    classdocs
    '''
    __create_count = 0
    
    def __init__(self, name, v):
        self.__create_count += 1
        self.__name = name
        self.__age = v
#         print(self)
#         print(self.__class__)
#         print(self.__dict__)

    @property
    def name(self):
        return self.__name
    
    @name.setter 
    def name(self, v):
        self.__name = v
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('age must be an integer!')
        if age < 0 or age > 100:
            raise ValueError('age must between 0 ~ 100!')
        self.__age = age
    
    @property
    def sex(self):
        return self.__sex
        
    @sex.setter
    def sex(self, v):
        self.__sex = v
 
    @classmethod
    def print_count(cls):
        print('staticmethod print_count', cls.__create_count)

def pb_test():
    per = chat_pb2.Person()
    per.name = '1111'
    per.age = 20
    print(per)
    
if __name__ == '__main__':
    
    pb_test()
    
    p1 = People('liwei', 20)
    print(p1.name)
    print(p1.age)
    p1.age = 30
    print(p1.age)
    p2 = People('liwei', 20)
    print(People.print_count())
    