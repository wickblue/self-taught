#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:30:46 2018

@author: philllippierce
"""

#!/bin/python3
arr = []
for i in range(1,7):
    for x in range(1,7):
        arr.append(x+i)
ans = []
for i in arr:
    if i < 10:
        ans.append(i)
y = len(ans)
z = y/36
print(z)
