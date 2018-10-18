#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:08:40 2018

@author: philllippierce
"""

#!/bin/python3

import sys

def hackerlandRadioTransmitters(x, k):
    ans = 0
    i = 0
    while i < x[-1]:
        xLoc = x[i] + k
        while xLoc > x[i]:
            i += 1
        i -= 1
        yLoc = x[i] + k
        while yLoc > x[i]:
            i += 1
        ans += 1
        print(ans)
    return ans
      
        
        
            
    
                
    
                
        

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(x, k)
    print(result)
