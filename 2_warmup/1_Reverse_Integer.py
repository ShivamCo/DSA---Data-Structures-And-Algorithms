
## https://leetcode.com/problems/reverse-integer/
## Reverse an integer


def reverse_integer(num):

    negative = False
    result = 0

    if num < 0:
        negative = True
        num *= -1


    while num != 0:
        last_digit = num % 10
        result += last_digit
        
        num = num // 10
        result *= 10

    result = result//10


    if negative:
        return -(result)

    else:
        return result





print(reverse_integer(120))
