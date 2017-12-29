# -*- coding: UTF-8 -*-

'''
Created on 2017年12月22日

@author: Administrator
'''

class Sessions(object):
    ''' 处理类 '''
    
    session_register = []

    def register(self, sender):
        self.session_register.append(sender)
        sender.write_message('connected.')

    def unregister(self, sender):
        self.session_register.remove(sender)
  

def main():
    pass

if __name__ == '__main__':
    main()