# find the x^n where x and n both are given


def pow(x,n):
    
    if n == 0:
        return 1
    
    else:
        return x * (pow(x, n-1))



arr = [(2,4), (2,3), (3,2), (3,3)]

for i,j in arr:
    print(pow(i,j))

