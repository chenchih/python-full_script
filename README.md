# python-full_script
## Update

# File Description 

+ Part1: SNMP

| File Name      | Description   |  Type  |  Other File  |
| --------   | -----:  | :----:  | :----:  |
|  1-1.1_snmp_walk_fw_input_IP.py    |check FW Version by SNMP user input IP  | SNMP |NA     |
| 1-1.2_snmp_walk_fw_list_IP.py       |Check FW Version assign IP in list | SNMP |NA     |
| 1-2.1_snmp_fw_immagge_replace_normal.py |Upgrade FW  user enter IP and check FW | SNMP |NA     |
| 1-2.2_snmp_fw_immagge_replace_normal_function.py| Upgrade FW  user enter IP and check FW-use function| SNMP |NA     |
| 1-2.3_snmp_fw_image_reg_expression.py  |Upgrade FW  user enter IP and check FW- used regular expression| SNMP |NA     |


+ Part2: Ping

| File Name      | Description   |  Type  | Other File  |
| --------   | -----:  | :----:  |:----:  |
|  2-1_ping_check_status.py    | ping ip address  | SNMP |NA     |
|  2-2_ping_with_output.py       |  ping ip address and export log.tmp, and check result   | ping |NA     |

+ Part3: Stability
 
| File Name      | Description   |  Type  | Other File  |
| --------   | -----:  | :----:  |:----:  |
| 3-1.1_stabilty-snmp_reset_loop.py |reset DUT by SNMP and used ping to check online |SNMP/PING | NA     |
| 3-1.2_stability_walk_snmp_reboot_with_pingV2.py |reset DUT by SNMP and used ping to check online V2 adding date |SNMP/PING | NA     | 
| 3-2_stability_walk_snmp_every_mintue_stability.py | walk MIB every minute |SNMP | NA     |

+ Part4: CMTS setting (Telnet)
 
| File Name      | Description   |  Type  | Other File  |
| --------   | -----:  | :----:  |:----:  |
|4-1.1_telnet_cbr8_ipv4.py|check your DUT IPV4 from CMTS using telnet |telnet|NA     |
|4-1.2_telnet_cbr8_ipv6.py|check your DUT IPV6 from CMTS using telnet|telnet|NA     |
|4-2.1_telnet_CMTS_IPv4_python3.py|User Enter XXXXXXXXXXXX MAC address, and check your DUT IPV4 from CMTS using telnet-python3|telnet|NA     |
|4-2.2_telnet_CMTS_IPv4_python2.py |User Enter XXXXXXXXXXXX MAC address, and check your DUT IPV4 from CMTS using telnet-Python2|telnet|NA     |
|4-2.3_telnet_CMTS_IPv4_python3-MAC-convert.py|User Enter any format MAC address, and check your DUT IPV4 from CMTS using telnet-Python2|telnet|NA     |
|4-3.1_telnet_CMTS_IPv6_python3.py|User Enter XXXXXXXXXXXX MAC address, and check your DUT IPV6 from CMTS using telnet-python3|telnet|NA     |
|4-3.2_telnet_CMTS_IPv6_python2.py|User Enter XXXXXXXXXXXX MAC address, and check your DUT IPV6 from CMTS using telnet-python2|telnet|NA     |

+ Part6-7: Other
 
| File Name      | Description   |  Type  | Other File  |
| --------   | -----:  | :----:  |:----:  |
|5-1_mac_cmts_text_file.py|||
|5-2_macconvert_V2.py|||
|5-3_CMTS_SCM_format.py | changed MAC to CMTS format  | read file |mac_cmts.txt     |NA|
|6-1.1read_and_write_file_for_DNS_List.py|read text file and add A into the file|read file|data.txt|
|6-1.2read_and_write_file_for_DNS_List_random_A_AAAA.py|read text file and random add  A or AAAA into the file|read file/random A or AAAA type|data.txt|
