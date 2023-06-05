from sage.all import *

def sum_divisors(n):
    x=divisors(n)
    s=sum(x)-n
    return s


count=0
num=0
while True:
    num+=1
    if sum_divisors(num) == num:
        continue
    if num<sum_divisors(num) and sum_divisors(sum_divisors(num))==num:
        print(num,sum_divisors(num))
        count+=1
    if count == 10:
        break
    