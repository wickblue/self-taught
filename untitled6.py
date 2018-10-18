#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:33:46 2018

@author: philllippierce
"""

#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    larry = 0
    rob = 0
    for i in apples:
        if s <= (a + i) <= t:
            larry += 1
    for i in oranges:
        if s <= (b + i) <= t:
            rob += 1
    print(larry, rob, sep=' ')

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
