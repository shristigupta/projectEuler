# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 12:40:53 2018
@author: shristi

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

m_3 = int(999/3)
print("Divisible by 3 and below 1000",m_3)

m_5 = int(999/5)
print("Divisible by 5 and below 1000",m_5)

m_5_3 = int(999/15) 
print("Divisible by 3 and 5 and below 1000",m_5_3)

t = m_3 +m_5 - m_5_3
print("Divisible by 3 or 5 ",int(t))

i=3
m_3=0
while (i<=999):
    m_3=m_3+i
    i = i + 3
    
i=5
m_5=0
while (i<=999):
    m_5=m_5+i
    i = i + 5
    
i=15
m_15=0
while (i<=999):
    m_15=m_15+i
    i = i + 15
    
print("Total of "+str(t)+" multiples is: "+str(int(m_3+m_5-m_15)))
    
    
    
    