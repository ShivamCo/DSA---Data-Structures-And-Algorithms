## Find if a number is Prime number or not

def is_prime(num):

    n = num // 2

    for i in range(2,n+1):
        
        div = num % i

        if div == 0:
            return(f"{num} is not a Prime Number")
        
    return(f"{num} is a Prime Number")


    
    

arr = [2,3,4,5,6,7,13, 17, 19, 23, 27, 29, 31, 50]

for i in arr:
    print(is_prime(i))