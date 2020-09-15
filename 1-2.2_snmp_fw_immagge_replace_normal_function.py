import os
def function_upgrade():
    hostname = input("enter your ip address(host):")
    #hostname="172.16.15.10"
    ######################Check FW############################################
    print ("#################start################")

    direct_output = os.popen("snmpwalk -cpublic -v 2c " + hostname+  " 1.3.6.1.2.1.69.1.3.5").read()
    #direct_output = os.popen('snmpwalk -cpublic -v 2c 172.16.26.96 1.3.6.1.2.1.69.1.3.5 ').read()
    test123=direct_output.replace('SNMPv2-SMI::mib-2.69.1.3.5.0 = STRING: ','')
    ###########Replace method  to replace ' and "" ###########################################
    
    test123=test123.replace('"','')
    test123=test123.replace('\n','')

    #print (test123)
    #########Regular expression method to replace ' and "" ####################################
    
    #r = re.search(r':\s(.*)', direct_output).group(1)
    #r = re.sub(r'\'|\"', '', r)
    ###############################################################


    ########################################################################################
    fw_name="GA-EN2251-P15-7.2.1.5G1-BAN-000.sbn"
    tftp_IP="192.168.3.12"
    ########################################################################################

    if test123 == fw_name: #"7.1.8.26-PC15-CTR"
        print("Same FW, this is LatestFW-Current FW:"+direct_output)

    else: 
        
        response = os.system("snmpset  -v 2c -c private " + hostname+  " 1.3.6.1.2.1.69.1.3.1.0 a " + tftp_IP)
        response = os.system("snmpset  -v 2c -c private " + hostname+  " 1.3.6.1.2.1.69.1.3.2.0 s " + fw_name)
        response = os.system("snmpset  -v 2c -c private " + hostname+  " 1.3.6.1.2.1.69.1.3.3.0 i 1")
        
        #response = os.system("snmpget -c public -v 2c " + hostname+  " 1.3.6.1.2.1.69.1.3.4.0 ")
        OperStatus = os.popen("snmpwalk -cpublic -v 2c " + hostname+  " 1.3.6.1.2.1.69.1.3.4").read()
        
        print(OperStatus[:-1])
        if OperStatus[-2] == "4":
            print("OperStatus: Fail")
        elif OperStatus[-2] == "1":
            print("OperStatus: In-Progress")
        else:
            print("OperStatus: Other reason")
    print ("#################END################")


while True:

    function_upgrade()
