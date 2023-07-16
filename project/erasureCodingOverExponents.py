from sage.all import *
import numpy as np
import sympy as sp
import random


def mypow(x,y):
    res = 1
 
    while (y > 0):
        if (y & 1):
            res = res * x;
 
        
        y = y >> 1
        x = x * x

    return res


def encode(k,n,v,mi):

    lambda_val=2048
    p= next_prime(mypow(2,lambda_val))

    G2=Integers(p)  #this was supposed to be G2 from Gen algorithm


    G= np.zeros((k,n),dtype=int)
    G=G.tolist()

    for j in range(v):
        for i in range(k):
            G[i][random.randint(0,n-1)]=random.getrandbits(lambda_val)
    
    print('OK1')

    wi=[] #encoded message will be stored here

    for i in range(n):
        pdt=1
        for j in range(k):
            pdt*=power_mod(mi[j],G[j][i],p)
        wi.append(pdt)

    

    return G,wi,p

def decode(p,k,n,v,wi,G):
    K=np.zeros((k,k),dtype=int)
    K=K.tolist()
    for i in range(k):
        for j in range(k):
            K[i][j]=G[i][j]
    
    K=matrix(K)
    K_inv=K.inverse()
    K_inv=list(K_inv)

    print('OK3')
    print(wi)
    print(K_inv)

    mi=[]

    for i in range(k):
        pdt=1
        for j in range(k):
            pdt*=power_mod(wi[j],K_inv[j][i],p)
        mi.append(pdt)

    return mi


#taking key servers =3, storage servers=8, (c=1.51, a=1.43) v=blnk=8 (b=7.2)
k=3
n=8
v=8
mi=[11,14,7]  # message values [change later according to will]

G,wi,p=encode(k,n,v,mi)

print('OK2')

retrieved_message=decode(p,k,n,v,wi,G)

print(retrieved_message)

