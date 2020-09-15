import os
import time
import datetime
count=0
cycle=5
currentDT = datetime.datetime.now()
os.system("cls")
hostname_IP = input("enter your ip address(host):")
cycle = input("please enter your cycle:(default is 10000): ")

cycle= int(cycle)
print ("#################start################")
for i in range (cycle):
    print ("==========Current date and time:",currentDT.strftime("%a, %b %d, %Y %H:%M:%S"),"===========")
    response = os.system("ping -n 5 " + hostname_IP+ "| FIND "+'"TTL="')
    #print (currentDT.strftime("%a, %b %d, %Y, %H:%M:%S"))
    
    time.sleep( 3 )
    if response == 0:
   
        count =count+1
        response1 = os.system("snmpset -v 2c -c private " + hostname_IP+  " 1.3.6.1.2.1.69.1.1.3.0 i 1")
        print ("!!!!waiting for 300second!!!!")
        time.sleep(300)
        print ("==============================")
        print ("###result:PASS###",count)
    else:
        print ("result:FAIL")
        break


print ("#################end################")
os.system("pause")
#time.sleep( 5 )
#response = os.system("snmpwalk -cpublic -v 2c 192.168.41.15 1.3.6.1.2.1.69.1.4.5.0 ")
#response = os.system("ping -n 5 " + hostname)