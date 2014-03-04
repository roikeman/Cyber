'''
Created on Dec 24, 2013

@author: froike
'''
from CyberManager import CyberManager
from CyberListenerSnort import CyberListenerSnort



def_config_file = '/home/froike/config.conf'
def_function_file = '/home/froike/function.py'
"""
try:
    code = open(def_function_file).read()
    exec (code)
except Exception:
    print ("Error in loading function file!")
    exit
   """ 


if __name__ == '__main__':

    print ("start...")
    master = CyberManager(def_config_file, def_function_file)
    SnortLis = CyberListenerSnort('/var/log/snort/alert.csv',master)
    SnortLis.start()
    print("end...")
