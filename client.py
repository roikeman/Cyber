#!/usr/bin/env python
# client.py

import config as cfg
import sys
import csv
import select
import socket
from threading import Thread
from time import sleep
from termcolor import colored
from CyberManager import CyberManager
from CyberListenerSnort import CyberListenerSnort


########CONFIGURATION FILES####################################
Rep_File = 'RepFile.csv'
def_config_file = '/home/froike/config.conf'
def_function_file = '/home/froike/function.py'
##########GLOBAL VARIABLES#####################################
msg_info = ''
Rep_Dic = ''
server_socket = ''
############LOADING DEPENDENCIES###############################
def loadfiles():
        global Rep_Dic,master,SnortLis
        reader = csv.reader(open(Rep_File, 'r'))
        Rep_Dic = dict((rows[0],rows[1]) for rows in reader)
        print ("Loading msg manager...\n")
        master = CyberManager(def_config_file, def_function_file)
        SnortLis = CyberListenerSnort('/var/log/snort/alert.csv',master)
        SnortLis.start()
        print("Loaded successfully!\n")
########FUNCTIONS##############################################
def TpCalcAvgRep(obj):
    global server_socket
    print(colored("TCAR Request, for object: " + obj, 'red'))
    try:
        reply = "<TCARA> " + obj + " " + Rep_Dic[obj] + "\n"
    except:
        reply = "<TCARA> NoRep\n"
    server_socket.sendall(reply.encode())
###############MSG HANDLER#####################################
def endline():
    print(' >', flush = True)

def msg_handler(msg):
    global msg_info
    line = msg.split()
    if line[0] == cfg.QUIT_STRING.encode():
        sys.stdout.write(msg.decode() + "\n")
        sys.exit(2)
    elif line[0] == cfg.TpCalcAvgRepReq.encode():
        if len(line) >= 2:
            TpCalcAvgRep(line[1].decode())
    else:
        sys.stdout.write(msg.decode())
        if 'Auth' in msg.decode():
            msg_info = 'Auth: '
        else:
            msg_info = ''
        endline()
###########################MAIN###################################################
def main():
    global server_socket
    global msg_info
    loadfiles()
    if len(sys.argv) < 2:
        print("Protocol: Python3 client.py [hostname]", file = sys.stderr)
        sys.exit(1)
    else:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.connect((sys.argv[1], cfg.PORT))

    sockets_list = [sys.stdin, server_socket]
    while True:
        read_sockets, write_sockets, error_sockets = select.select(sockets_list, [], [])
        for s in read_sockets:
            if s is server_socket: # incoming message 
                msg = s.recv(cfg.READ_BUFFER)
                if not msg:
                    print("Disconnected.")
                    sys.exit(2)
                else:
                    msg_handler(msg)
            else:
                msg = msg_info + sys.stdin.readline()
                server_socket.sendall(msg.encode())
#########################################################
        
if __name__ == "__main__":
    main()
