

# Using using Python Array Module


from array import *

val = array('i', [10,20,30,40,50,60])   # i --- Type code i mean i - 2 bit Int, I - 4 bit Int



#Itrate All element of an Array

# 1st Way
for i in val:
    print(i, end=",")

print("\n")

# 2nd Way 
for i in range(len(val)):
    print(val[i], end=" ")
