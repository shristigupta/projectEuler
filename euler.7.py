# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:51:37 2018

@author: shristi

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math as mt
def prime_10001():
    n=3
    c=2
    while(c!=10001):
        
        n=n+2
        if(is_prime(n)):
            c=c+1
            print(c,n)
        
    if(c==10001):
        return (n)
        
def is_prime(n):
    c=0    
    for i in range(3,int(mt.sqrt(n)+1)):
        if (n%i==0):
            c=c+1
            
    if(c==0):
        return True 
    else:
        return False
    
n=prime_10001();
print(n)
    
    
    
        