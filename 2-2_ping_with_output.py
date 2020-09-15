import os
import time
count=0

#hostname = raw_input("enter your ip address(host): ")
hostname = input("enter your ip address(host):")
print ("#################start################")

for i in range (2):
    #ping ip address 
    #response = os.system("ping -n 5 " + hostname + " | FIND " + '"TTL=" > tmp.log')
    response = os.system("ping " + hostname + "> tmp.log")	
    open('tmp.log', 'r').read()


	# reset modem by snmp 
    count = 0
    strCount = str(count)
    time.sleep( 1 )
    if response == 0:
   
        count = count + 1
        strCount = str(count)

        print ("###result:PASS###",count)
        print ("==============================")

        fd = open("tmp.log",'a+')
        fd.write("###result:PASS###")
        fd.write(strCount)
        fd.close()
    else:
        print ("result:FAIL")

        fd = open("tmp.log",'a+')
        fd.write("###result:FAIL###")
        fd.write(strCount)
        fd.close()
     
    break


print ("#################end################")
os.system("pause")
#time.sleep( 5 )
#response = os.system("snmpwalk -cpublic -v 2c 192.168.41.15 1.3.6.1.2.1.69.1.4.5.0 ")
#response = os.system("ping -n 5 " + hostname)