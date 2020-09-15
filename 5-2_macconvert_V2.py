import os

h = input("please enter your MAC : ")

#This support both python2 and python3
#s=""
#h="00233a990c21"
#
mac_list=list(h)
if(mac_list[2]==":"):
    #print(":")
    h=h.replace(":",'')
    print("Remove :"+ h)

elif (mac_list[2].isdigit()):
    print("a digit")
    ':'.join(h[i:i+2] for i in range(0,12,2))
    print ('MAC format:'+':'.join(h[i:i+2] for i in range(0,12,2)))
    
    ':'.join(h[i:i+2] for i in range(0,12,2))
    print ('CMTS mac format:'+'.'.join(h[i:i+4] for i in range(0,12,4)))
else:
    print("XXX")




os.system("pause")
