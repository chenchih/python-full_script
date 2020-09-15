import os
import time
count=0
cycleno = 1000
hostname = input("enter your ip address(host):")
cycleno = input("please enter cycle[default 1000]: ")
print ("==================start==============")
for i in range (cycleno):
    response_mib = os.system("snmpwalk -cpublic -v 2c 192.168.41.15 1.3.6.1.2.1.69.1.4.5.0 ")
    time.sleep( 5 )
    if response_mib == 0:
       
     
        count =count+1
        print ("===============")
        print ("###result:PASS###",count)
        time.sleep( 5 )
        
    else:
        print ("result:FAIL")
        break


print ("==================end==============")


os.system("pause")
#time.sleep( 5 )
#response = os.system("snmpwalk -cpublic -v 2c 192.168.41.15 1.3.6.1.2.1.69.1.4.5.0 ")
#response = os.system("ping -n 5 " + hostname)