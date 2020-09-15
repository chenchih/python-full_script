def MACADD():
    h = input("please enter your MAC : ")
    mac_list=list(h)
    print
    if(mac_list[2]==":"):
    #print(":")
        h=h.replace(":",'')
        #print("Remove :"+ h)
        h ='.'.join(h[i:i+4] for i in range(0,12,4))
        return h

    elif (mac_list[3].isdigit()):
        h=h.replace(".",'')
        h ='.'.join(h[i:i+4] for i in range(0,12,4))
        return h
        #print("a digit")
       #h=h.replace(":",'')
        #h = ':'.join(h[i:i+2] for i in range(0,12,2))
        
       
        #print ('MAC format:'+':'.join(h[i:i+2] for i in range(0,12,2)))
    
        
        #print ('CMTS mac format:'+'.'.join(h[i:i+4] for i in range(0,12,4)))
    else:
        
        h=h.replace(".",'')
        #print("Remove :"+ h)
        h ='.'.join(h[i:i+4] for i in range(0,12,4))
        return h 
    return h 