import os
hostnames = ['172.16.15.29', '172.16.15.31',]



for hostname in hostnames:
    #check CM's FW 
    response = os.system("snmpwalk -cpublic -v 2c "+ hostname+" "+"1.3.6.1.2.1.69.1.4.5")
    #0 is response, 1 is not response
    print(type(hostnames))
    
    #if response == 1:
    #    break
  
        
