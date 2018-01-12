'''
Created on 2018年1月10日

@author: Administrator
'''

import sys
sys.path.append('./common')

class ChatRoom(object):
    '''
    classdocs
    '''
    
    online_sessions = {}
    offline_sessions = {}
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def register(self, session):
        rid = session.user.rid
        if self.online_sessions.get(rid) == None:
            self.online_sessions[rid] = list([])
        
        self.online_sessions[rid].append(session)
        
        return True

    def unregister(self, session):
        rid = session.user.rid
        if self.online_sessions.get(rid) == None:
            return
        
        users = self.online_sessions[rid]
        users.remove(session)
          
    def broadcastMessage(self, msg):
        for _, l in self.online_sessions.items():
            for s in l:
                s.write_message(msg)
            
    def broadcastMessageFilter(self, msg, func):
        for _, l in self.online_sessions.items():
            for s in l:
                if func(s):
                    s.write_message(msg)
                                   
    def sendMessageToRoom(self, msg, rid):
        if self.online_sessions.get(rid) == None:
            return
        sessions = self.online_sessions[rid]
        for s in sessions:
            if s.user.rid == rid:
                s.write_message(msg)
                
    def sendMessageToUid(self, msg, rid, uid):
        if self.online_sessions.get(rid) == None:
            return
        sessions = self.online_sessions[rid]
        for s in sessions:
            if s.user.uid == uid:
                s.write_message(msg)
                
                
                
                
                
                
                