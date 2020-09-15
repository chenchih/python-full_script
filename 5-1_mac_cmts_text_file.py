count =0
with open('mac_cmts.txt') as f:
    #for line in f:
    for line_index,line in enumerate(f):    
        line = line.strip()
        #line = line[:-1] + str(int(line[-1:]) + 1)
        #f_out.write('{}\n'.format(line))
        
        #print (count)
        
        print (line_index + 1,'\t','mac format: scm '+'.'.join(line[i:i+4] for i in range(0,12,4))+ " phy0")