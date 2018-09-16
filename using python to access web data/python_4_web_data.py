# import re
# import np

# dfile = open(r"C:\Users\O-cube\Documents\python work\using python to access web data\regex_sum_83118.txt")

# text = dfile.read()

# sum = 0
# final = []

# for line in text :
#     line = line.strip()

#     y = re.findall("([0-9]+)",line)
#     if len(y)>0:
#         line_val = sum(map(int,y))
#         final.append(line_val)

# print ("Final sum = {0}".format(np.sum(final)))

# import re
# print(sum([int(i) for i in re.findall('[0-9]+',open(r"C:\Users\O-cube\Documents\python work\using python to access web data\regex_sum_83118.txt").read())]))

import re
dfile = open("regex_sum_83118.txt")



number_list = list()

for line in dfile:
    numbers =re.findall("[0-9]+",line)
    number_list = number_list + numbers
    print(number_list)

sum = 0

for i in number_list:
    sum = sum + int(i)

print(sum)



    

    
            

        


    

    
     