#coding:UTF-8
#author:1x2Bytes
#zero-security(O-sec)
import socket
import argparse
import sys
def banner():
    print'''
 ____            _   ____                  
|  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  
| |_) / _ \| '__| __\___ \ / __/ _` | '_ \ 
|  __/ (_) | |  | |_ ___) | (_| (_| | | | |
|_|   \___/|_|   \__|____/ \___\__,_|_| |_|
@1x2Bytes  zero-security(O-sec)  
    '''
def portscan(hosts,port):
    if "http://" in hosts:
        site = hosts.split("http://")[1]
        host = socket.gethostbyname(site)
        if "/" in site:
            sites = site.replace('/','')
            host = socket.gethostbyname(sites)
    elif "https://" in hosts:
        site = hosts.split("https://")[1]
        host = socket.gethostbyname(site)
        if "/" in site:
            sites = site.replace('/','')
            host = socket.gethostbyname(sites)
    else:
        host = socket.gethostbyname(hosts)
    default_port = range(1,65535)
    if not port:
        for ports in default_port:
            try:

                s=socket.socket()
                s.settimeout(0.1)
                s.connect((host,ports))
                msg = "[IP] %s [PORT] %s Open" % (host,ports)
                print msg
            except:
                pass
    else:
        try:

            s=socket.socket()
            s.settimeout(0.1)
            s.connect((host,port))
            msg = "[IP] %s [PORT] %s Open" % (host,port)
            print msg
        except:
            pass

def main():
     parse = argparse.ArgumentParser(description="A easy PortScan Script ")
     parse.add_argument('--host', '-a', type=str, help='IP address or url no cdn')
     parse.add_argument('--port','-p',type=int,help='One Port to scan open')
     args = parse.parse_args()
     if not args.host:
         parse.print_help()
         sys.exit(0)
     ip = args.host
     port = args.port
     banner()
     portscan(ip,port)
if __name__ == '__main__':
    main()



