#!/bin/python3
from sshport_scan_module import check_ip_alive
import sys
#ip = '192.168.1.1'
def test():
    #ipduan = 1
    f = open("ip.txt",'rb')
    list1 = f.read().decode("utf-8")
    #print (list1)
    ipsplit = list1.split("\n")
    for ip in ipsplit:
        #ip = "223.197.223."+str(ipduan)
        if check_ip_alive(ip) == 1:
            print ('[+]'+ip)
            f = open ('newip.txt','a')
            f.write(ip+"\n")
            f.close()
            #ipduan = ipduan + 1
        else:
            print('[-]' + ip)
            #ipduan = ipduan + 1
            continue
        #ipduan = ipduan + 1
if __name__ == '__main__':
    test()


