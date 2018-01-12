'''
Created on 2018年1月9日

@author: Administrator
'''
from CalcModuleRPC import CalcModuleRPC
from MyModuleRPC import MyModuleRPC

class CommonModuleServer(CalcModuleRPC, MyModuleRPC):
    def hello(self, name):
        return 'Hello, %s' % name