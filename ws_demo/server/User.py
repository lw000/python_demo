# -*- coding: UTF-8 -*-

'''
Created on 2017年12月22日

@author: Administrator
'''

class User(object):
    '''
    classdocs
    '''
    users = {}
    
    def __init__(self, arguments):
        '''
        Constructor
        '''
        super(User, self).__init__()
        
        if isinstance(arguments, dict) : 
            self.__name = arguments['name'][0].decode()
            self.__upsd = arguments['upsd'][0].decode()
            self.__rid = arguments['rid'][0].decode()
            self.__uid = arguments['uid'][0].decode()
            self.__extra = arguments['extra'][0].decode()
        else:
            RuntimeError('arguments error.')
        
    def __del__(self):
        pass
        
    @property
    def name(self):
        return self.__name
    
    @name.setter 
    def name(self, v):
        self.__name = v
    
    @property
    def upsd(self):
        return self.__upsd
    
    @upsd.setter 
    def upsd(self, upsd):
        self.__upsd = upsd
        
    @property
    def rid(self):
        return self.__rid
    
    @rid.setter 
    def rid(self, rid):
        self.__rid = rid
        
    @property
    def uid(self):
        return self.__uid
    
    @uid.setter 
    def uid(self, uid):
        self.__uid = uid
        
    @property
    def extra(self):
        return self.__extra
    
    @extra.setter 
    def extra(self, extra):
        self.__extra = extra
        
    def register(self):
        self.users[self.uid] = self

    def unregister(self):
        self.users.remove(self.uid)
        
def main():
    d = {'name':[b'name'],'upsd':[b'upsd'],'rid':[b'rid'],'uid':[b'uid'],'extra':[b'extra']}
#     d['name'] = [b'name']
#     d['upsd'] = [b'upsd']
#     d['rid'] = [b'rid']
#     d['uid'] = [b'uid']
#     d['extra'] = [b'extra']
    print(d['name'][0])
    user = User(d)#,['upsd'],['rid'],['uid'],['extra']
    print(user.name)
    print(user.upsd)
    print(user.rid)
    print(user.uid)
    print(user.extra)

if __name__ == '__main__':
    main()