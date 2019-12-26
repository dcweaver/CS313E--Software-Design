#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:31:40 2019

@author: ChaseWeaver
"""

#Three Laws of Recursion
# 1. A recursive algorithm must call itself. That's what makes it recursive.

# 2. A recursive algorithm must have a *base case*. This means there is a value for the function that is easy
#    to calculate




def iFactorial(num):
    
    fact = 1 
    
    for i in range(num):
        fact *= i + 1 
        
    return fact

##############################################################################

def rFactorial(num):
    
    if num == 1:
        return (1)
    else:
        return(num * rFactorial(num - 1))



def main():
    
    print(iFactorial(5))
    print(iFactorial(3))
    
main()