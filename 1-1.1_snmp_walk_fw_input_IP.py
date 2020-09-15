import os

while True:  # Loop continuously
    hostname = input("enter your ip address(host):")   # Get the input
    #print("hellp",hostname)
    
    #fw check 
    response = os.system("snmpwalk -cpublic -v 2c "+ hostname+" "+"1.3.6.1.2.1.69.1.3.5")
    # reboot cm  docsDevResetNows    
    '''
    response=os.system("snmpset  -v 2c -c private " + hostname +" "+"1.3.6.1.2.1.69.1.1.3.0 i 1")
    if hostname == "":       # If it is a blank line...
        print("=============end=============")
        break           # ...break the loop
    '''
    #cfg check
    #response = os.system("snmpwalk -cpublic -v 2c "+ hostname+" "+"1.3.6.1.2.1.69.1.4.5")
        
