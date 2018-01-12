# -*- coding: UTF-8 -*-

'''
Created on 2017年 12月14日

@author: Administrator
'''
import sys
import uuid
sys.path.append('./')
sys.path.append('./chat')

from chat_pb2 import Person

class People(object):
    '''
    classdocs
    '''
    create_count = 0
    
    def __init__(self, name, v):
        self.create_count += 1
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
        if not isinstance(v, int):
            raise ValueError('sex must be an integer!')
        if v < 0 or v > 2:
            raise ValueError('sex must between 0 ~ 2!')
        self.__sex = v
 
    @classmethod
    def print_count(cls):
        print('staticmethod print_count', cls.create_count)
        
    def __str__(self, *args, **kwargs):
        return 'name:%s,age:%d' % (self.name, self.age)
if __name__ == '__main__':
    print(uuid.uuid1())
    print(uuid.uuid4())
    
    per = Person()
    per.name = '1111'
    per.age = 20
    print(per)
    
    p1 = People('liwei', 20)
    p2 = People('heshanshan', 20)
    print(p1.name)
    print(p1.age)
    print(p2.name)
    print(p2.age)
    
    print(People.print_count())
    