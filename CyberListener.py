'''
Created on Dec 24, 2013

@author: froike
'''

import threading
from CyberEvent import CyberEvent
import abc


class CyberListener(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self,def_log_file,CyberMngrObject):
        self.def_log_file = def_log_file
        self.CyberMngrObject = CyberMngrObject
        

    def start(self):
        print("....................start")
        self.x = threading.Thread(target=self.runit)
        print("....................")
        self.x.start()
        print ("....end")
        
        
    @abc.abstractmethod
    def runit(self):
        pass
        
    
    def sendEvenToMaster(self,CyberEv):
        self.CyberMngrObject.NewEvent(CyberEv)
        
        

