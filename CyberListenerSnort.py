'''
Created on Dec 24, 2013

@author: froike
'''

from CyberListener import CyberListener
import linecache
import time
from CyberEvent import CyberEvent

class CyberListenerSnort(CyberListener):
    '''
    classdocs
    '''
    def runit(self):
        i=1
        while (1):
            line = linecache.getline(self.def_log_file,i)
            if (len(line)>1):
                line = line.split(',')
                self.sendEvenToMaster( CyberEvent("Snort", line[0], line[4], line[5], line[7], line[6]))
                i=i+1
                
            else:    
                time.sleep(2)
                linecache.checkcache(self.def_log_file)