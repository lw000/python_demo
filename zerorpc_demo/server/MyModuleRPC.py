'''
Created on 2018年1月9日

@author: Administrator
'''

import zerorpc

class MyModuleRPC(object):

    @zerorpc.stream
    def streaming_range(self, fr, to, setp):
        return range(fr, to, setp)
    
    def bad(self):
        raise Exception('pppppppppppppp')