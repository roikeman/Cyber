'''
Created on Dec 24, 2013

@author: froike
'''

class CyberEvent:
    def __init__(self,IDS,Time,Msg,Protocol,Dest,Src):
        self.IDS = IDS
        self.Time = Time
        self.Msg = Msg
        self.Protocol = Protocol
        self.Dest = Dest
        self.Src = Src
        

    def IDS(self):
        return self.IDS

    def Time(self):
        return self.Time

    def Msg(self):
        return self.Msg
    
    def Protocol(self):
        return self.Protocol
    
    def Dest(self):
        return self.Dest
    
    def Src(self):
        return self.src
