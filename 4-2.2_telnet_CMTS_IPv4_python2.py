# -*- coding: utf-8 -*-
import telnetlib
import subprocess
import time
import re

def Telnet_Check_reachability(ip):
    ping_count=3
    process = subprocess.Popen(['ping', ip, '-n', str(ping_count)],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
                      
    process.wait()
    stdout = process.stdout.read()
    #print stdout
    if "TTL=" in stdout:
        #print "Server reachable"
        successful = 1
    else:
        #print "Server unreachable"
        successful = 0
    return successful

def Login_Telnet(HOST,username,password):
    try:
        tn=""
        reachability=Telnet_Check_reachability(HOST)
        if (reachability==1):
            tn = telnetlib.Telnet(HOST,23)
            tn.read_until("Username:")
            tn.write(username + "\n")
            if password:
                tn.read_until("Password:")
                tn.write(password + "\n")
            time.sleep(3)
            return tn
    except IOError:
        print "Telnet " + HOST + " failed. Please check the server connection"

def telnet_To_CMTS(Client_IP, Client_Name, Client_Pwd, MAC):
    tn =Login_Telnet(Client_IP, Client_Name, Client_Pwd)
    if "telnetlib" in str(tn):
        time.sleep(1)
        value = tn.read_until("Router#")
        command = "scm " + MAC + " \n"
        tn.write(command)
        value = tn.read_until("Router#")
        #print value
        tn.close()
        time.sleep(1)

        info = "172"

        matchObj = re.match(r'.*'+ info + '(.*)C0',value, re.M|re.DOTALL)
        if matchObj:
            Ipv4_address = info + matchObj.group(1)
            Ipv4 = Ipv4_address.replace(" ", "")
            return Ipv4

        else:
           print "No match!!"    
    else:
        print "Telnet failed"


ip ="192.168.1.252"
username = "guest"
password = "guest"
mac = "840b.7cac.85e4"
new_IPv4 = telnet_To_CMTS(ip, username, password, mac)
print new_IPv4

