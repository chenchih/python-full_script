import getpass
import re
import telnetlib
HOST = "192.168.1.252"
#user = input("Enter your remote account: ")
#password = getpass.getpass()
user='guest'
password='guest'
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")

value = tn.read_until(b"Router#")
tn.write(b"scm 840B.7C0B.E474 ipv6 \n")
value = tn.read_until(b"Router#")
#######################################################
value=value.decode('utf8')
info = "2001"
matchObj = re.match(r'.*'+ info + '(.*)\n',value, re.M|re.DOTALL)
#matchObj=matchObj.decode('big5')

       
if matchObj:
    Ipv6_address = info + matchObj.group(1)
    Ipv6 = Ipv6_address.replace("\n", "")
    print(Ipv6)
    #return Ipv6

else:
    print ("No match!!")  
  

####################################################
        
tn.write(b"exit\n")
#print(tn.read_all().decode('ascii'))
