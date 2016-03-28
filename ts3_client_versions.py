#!/usr/bin/python

import re
import time
import sys
import socket
from time import gmtime, strftime

query_user = 'username'
query_user_password = 'password'

host= 'localhost'
port= '10011'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5.0)
sock.connect((host,int(port)))
sock.recv(1024)
login="login %s %s\n" % (query_user, query_user_password)
sock.send(login)
sock.recv(1024)
sock.send('serverlist\n\n')
serverlist= sock.recv(1024)
sock.send('use 1\n\n')
sock.recv(1024)
sock.send('clientupdate client_nickname=Retry\\sTS3.fi\n\n')
sock.recv(1024)
sock.send('clientlist\n\n')
print "[+] Getting client list..."
time.sleep(2)
clients= sock.recv(40960000)
print "[+] List length: %s" % len(clients)
clientlist=clients.split('|')
print "[+] Number of clients: %s" % len(clientlist)
for client in clientlist:
  client=dict(re.findall(r'(\S+)=(".*?"|\S+)', client))
  sock.send('clientinfo clid='+client['clid']+'\n\n')
  time.sleep(0.5)
  clinfo= sock.recv(4096000)
  clinfo=dict(re.findall(r'(\S+)=(".*?"|\S+)', clinfo))
  if 'client_version' in clinfo:
    version=clinfo['client_version'].replace('\s', " ").split(" ")[0]
  else:
    version = "No\\sVersion\\sFound"
  data=[client['client_nickname'].replace('\\s', " "),version,]
  timestamp= strftime("%d-%m-%Y %H:%M:%S", gmtime())
  print (timestamp+" TS3 [+] Client info: {: <40} {: <20}".format(*data))
  if version != "3.0.18.2":
    if version != "ServerQuery":
      #Target client
      sock.send('sendtextmessage targetmode=1 target='+client['clid']+' msg='+msg+'\n\n')
      sock.recv(1024)
sock.send('quit\n\n')
sock.recv(1024)
print "Done"
