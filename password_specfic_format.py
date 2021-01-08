"""
This is a script to convert MAC Address format
CGNV5_TFC format: #BBAADD@CCFFEE 
"""

def split_mac(x):
     mac_Add=x.split(":")
     return mac_Add
#CGNV5 TFC MODEL
def TFC_MAC(MAC):
    #mac_Add=MAC.split(":")
    mac_Add=split_mac(MAC)
    str=""
    mac_Add_1= mac_Add[1],mac_Add[0],mac_Add[3]
    mac_Add_2=mac_Add[2],mac_Add[5],mac_Add[4]
    convert_strlist=str.join(mac_Add_1)
    TFC_F=convert_strlist
    convert_strlist=str.join(mac_Add_2)
    TFC_B=convert_strlist

    MAC_TFC= "#",TFC_F,"@",TFC_B,"*"
    #str =  ''.join(tup) 
    #MAC= ''.join(MAC_TFC) 
    TFC_MAC_ADDR = convertTuple(MAC_TFC) 
    return TFC_MAC_ADDR


def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

def split_convert(MAC):
    MAC_ADD=MAC.split(':')
    str=""
    return str.join(MAC_ADD)

mac_Add= input("please enter your mac address: ").upper()
print ("MAC Address:    ", split_convert(mac_Add))
print ("TFC MAC Address:", TFC_MAC(mac_Add))


