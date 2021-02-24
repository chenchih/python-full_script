import random
number_list = ["A", "AAAA"]
with open('data.txt') as f,open('data_out_rand.txt', 'w') as f_out:
    for line in f:
        line = line.strip()
        #f.write()
        #f_out.write(line + " " + "A" + "\n"+ "\n")
        f_out.write(line + " " + random.choice(number_list) + "\n"+ "\n")

        

