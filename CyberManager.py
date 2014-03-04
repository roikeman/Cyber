'''
Created on Dec 24, 2013

@author: froike
'''
import linecache
from function import *

class CyberManager:
    
    
    
    def __init__(self,Def_config_file, Def_function_file):
        self.Def_config_file = Def_config_file
        self.Def_function_file = Def_function_file
        self.RuleSetContains = dict()
        self.RuleSetEquals = dict()
        self.init_config()
        """
        try:
            code = open(Def_function_file).read()
            exec code  
        except Exception:
                print ("Error in loading function file!")
                exit
        """
        
    def NewEvent(self, CEvent):
        print (CEvent.Msg)
        if CEvent.Msg in self.RuleSetEquals:  #feature: test which rules get executed
            try:
                exec (self.RuleSetEquals[CEvent.Msg])
            except Exception:
                print ("Error in loading function!")
                pass
            
        for (k,v) in self.RuleSetContains.items():
            if k in CEvent.Msg:
                try:
                    exec (v)
                except Exception:
                    print ("Error in loading function!")
                    pass
            
    
    def init_config0(self,config_file):
        i=1
        while (1):
            line = linecache.getline(config_file,i)
            if (len(line)>1):
                line = line.strip()
                line = line.split(',')
                if line[1] == 'equals':
                    self.RuleSetEquals[line[0]] = line[2]
                else:
                    if line[1] == "contains" :
                        self.RuleSetContains[line[0]] = line[2]
                        #RuleSetContains.append(line)
                i=i+1
            else:
                break
        print(self.RuleSetEquals)

    def init_config(self):
        self.init_config0(self.Def_config_file)    

