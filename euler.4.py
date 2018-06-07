# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

def largest_pallindrome():
    max=0
    for i in range(100,1000):
        for j in range(i+1,1000):
            n = i*j
            if(is_pallindrome(n)):
                if(n>max):
                    max=n
    return max

def is_pallindrome(n):
    r=0
    o=n
    while(n!=0):
        r=int(r*10+n%10)
        """print(r)"""
        n=int(n/10)
        """print(n)"""
    
    if(r==o):
        print(r)
        return True
    else:
        return False
    
"""print(is_pallindrome(123321))"""
    
max=largest_pallindrome();
print(max)
