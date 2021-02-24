with open('data.txt') as f,open('data_out.txt', 'w') as f_out:
    for line in f:
        line = line.strip()
        #f.write()
        f_out.write(line + " " + "A" + "\n"+ "\n")
        

