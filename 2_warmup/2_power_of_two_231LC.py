# Power of two - 231 Leet Code
# https://leetcode.com/problems/power-of-two/submissions/2017157427/


def power_of_two(num):

    one_count = 0

    while num !=0:
        last_bit = num & 1    # AND bit wise operation 2^2 = 4 = 100
        
        if last_bit == 1:                     # Pattern is all two powers no. have exactly 1 bit
            one_count += 1
            
        num  = num >> 1   # shift right bit wise operations

    if one_count == 1:
        return True
    else:
        return False
    
arr = [1, 3, 4, 16, 8, 100, 23]

for i in arr:
    result = power_of_two(i)
    print(result)