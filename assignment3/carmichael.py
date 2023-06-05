from sage.all import *

n=int(input("Enter upto which number to be checked: "))

carmichaels=[]

for i in range(2,n+1):
    
    if(is_prime(i)):
        continue
    
    if(not is_squarefree(i)):
        continue
    
    factors=divisors(i)
    prime_factors=[]

    for f in factors:
        if(is_prime(f)):
            prime_factors.append(f)

    flag=True
    
    for p in prime_factors:
        if((i-1)%(p-1)!=0):
            flag=False
    
    if(flag):
        carmichaels.append(i)

print(carmichaels)

