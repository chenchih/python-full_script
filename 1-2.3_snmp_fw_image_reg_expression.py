import os, re

direct_output = os.popen('snmpwalk -cpublic -v 2c 172.16.26.96 1.3.6.1.2.1.69.1.3.5 ').read()
#########Regular expression ####################################
#/s=>space
r = re.search(r':\s(.*)', direct_output).group(1)
r = re.sub(r'\'|\"', '', r)

#################DEBUG USED############################
#print(test1234 == r)
# print("r:",r)
# print("r1:",r1)
#############################################

if r1 == "7.1.8.26-PC15-CTR":
    print("same")
else: 
    print("end")
