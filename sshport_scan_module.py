from scapy.all import *
import socket


def check_ip_alive(ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(3)
    if s.connect_ex((ip,22))==0:
        return 1
    else:
        return 0
