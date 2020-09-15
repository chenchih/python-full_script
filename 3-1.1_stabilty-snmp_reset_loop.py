import os
import time

count=0
cycleno = 1000
hostname = input("enter your ip address(host):")
cycleno = input("please enter cycle[default 1000]: ")

print ("#################start################")
for i in range (2):
    #ping ip address 
    response = os.system("ping -n 5 " + hostname + " | FIND " + '"TTL="')
    #test  = "snmpset -v 2c -c private " + hostname+  " 1.3.6.1.2.1.69.1.1.3.0 i 1"
    response1 = os.system("snmpset -v 2c -c private " + hostname+  " 1.3.6.1.2.1.69.1.1.3.0 i 1")

						  


	# reset modem by snmp 
  
    
    time.sleep( 300 )
    if response == 0:
        if response1 == 0:
            count =count+1
			
            print ("###result:PASS###",count)
            print ("==============================")
        else:
            print ("###result:SNMP FAIL###",count)
            print ("==============================")
		
    else:
        print ("result:Ping FAIL")
        break


print ("#################end################")
os.system("pause")
#time.sleep( 5 )
#response = os.system("snmpwalk -cpublic -v 2c 192.168.41.15 1.3.6.1.2.1.69.1.4.5.0 ")
#response = os.system("ping -n 5 " + hostname)