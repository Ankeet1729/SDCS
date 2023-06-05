from sage.all import *
import random

k=int(input("Enter k: "))

list=prime_range(10**(k-1),10**k)
length=len(list)
n1=random.randint(0,length)
n2=random.randint(0,length)
while(n1==n2):
    n2=random.randint(0,length)

p=list[n1]
q=list[n2]

var('a,b',domain='integer')
eq=a*p+b*q==1
sol=solve(eq,a,b)
a=sol[0].substitute(t_0=0)
b=sol[1].substitute(t_0=0)
print(tuple([p,q,a,b]))