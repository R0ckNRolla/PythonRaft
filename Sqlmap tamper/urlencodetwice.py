#!/usr/bin/env python
#url二次编码注入漏洞利用
import re
from urllib import quote
from lib.core.data import kb
from lib.core.enums import PRIORITY
#quote 方法对 传入的payload进行url编码
__priority__ = PRIORITY.NORMAL

def dependencies():
    pass
def tamper(payload, **kwargs):
    nedencode = payload
    nedencode = quote(quote(nedencode)) #对payload进行二次编码   
    return nedencode