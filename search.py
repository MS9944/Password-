#!/bin/python3
import requests
import re
def get_html(url):
    html_get = requests.get(url)
    #print (html_get.text)
    return html_get.text
def main1():
    print ("[*]正在请求......")
    gethtml = get_html("https://tool.nbqykj.cn/network/scan/ssh")
    iplist = re.findall('(?<=\/network\/ip\?q=)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',gethtml)
    f = open ("ip.txt",'wb')
    for i in iplist:
        f.write(str(i).encode("utf-8")+"\n".encode('utf-8'))
    #print (iplist)
    f.close()
main1()
print ("[+]数据写入成功,保存为ip.txt")
