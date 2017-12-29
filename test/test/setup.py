'''
Created on 2017年12月26日

@author: Administrator
'''

from distutils.core import setup, Extension
import numpy

#get numpy dir
npinclude = numpy.get_include()

module = Extension('cCalc', sources=['python_ext.cpp'],
        include_dirs=[npinclude],
        library_dirs=[],
        libraries=[]
        )
setup(name= 'cCalc',
    version= '1.0',
    ext_modules = [module])

if __name__ == '__main__':
    pass