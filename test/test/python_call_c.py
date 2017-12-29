'''
Created on 2017年12月26日

@author: Administrator
'''

import ctypes
import os
import sys
import cProfile

sys.path.append(r"./python_ext.pyd")
sys.path.append(r"./calc.pyd")

import python_ext
import calc

# cdecl调用
#     cdecl_dll_call = ctypes.CDLL(dllPath) 
cdecl_dll_call = ctypes.cdll.LoadLibrary('./python_export_func.dll')

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def main():
#     CUR_PATH = os.path.dirname(__file__)
#     dllPath = os.path.join(CUR_PATH, 'python_export_func.dll')

    rect = calc.Rect(10, 20)
    print('calc.Area: ', calc.Area(rect))
    print('calc.Perimeter: ', calc.Perimeter(rect))
    print('calc.set_w_old: ', calc.set_w(rect, 60))
    print('calc.set_h_old: ', calc.set_h(rect, 60))
    print('calc.get_w: ', calc.get_w(rect))
    print('calc.get_h: ', calc.get_h(rect))
    print('calc.Area: ', calc.Area(rect))
    print('calc.Perimeter: ', calc.Perimeter(rect))

    math = calc.Math()
    print('calc.len: ', calc.len(math, '111111111'))
    print('calc.add: ', calc.add(math, 1, 2))
    print('calc.sub: ', calc.sub(math, 1, 2))
    print('calc.mul: ', calc.mul(math, 1, 2))
    
    print('python_ext.len: ', python_ext.len('111111111'))
    print('python_ext.add: ', python_ext.add(1,2))
    print('python_ext.sub: ', python_ext.sub(1,2))
    print('python_ext.mul: ', python_ext.mul(1,2))
    
    print('cdecl_dll_call.add: ', cdecl_dll_call.add(1,2))
    print('cdecl_dll_call.sub: ', cdecl_dll_call.sub(1,2))
    print('cdecl_dll_call.mul: ', cdecl_dll_call.mul(1,2))
    
if __name__ == '__main__':
    main()
    
#     print(cProfile.run('python_ext.len(\'111111111\')'))
#     print(cProfile.run('python_ext.add(1,2)'))
#     print(cProfile.run('python_ext.sub(1,2)'))
#     print(cProfile.run('python_ext.mul(1,2)'))
#     cProfile.run("main()")
#     cProfile.run("main1()")
