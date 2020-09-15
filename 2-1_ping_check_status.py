import os
hostname = "192.168.1.50" #example
response = os.system("ping -n 5 " + hostname)

#and then check the response...
if response == 0:
    print (hostname, 'is up!')
else:
    print (hostname, 'is down!')