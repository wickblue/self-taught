#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:34:41 2018

@author: philllippierce
"""

#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    minimum = sum(arr)
    maximum = 0
    for i in arr:
        if (sum(arr) - i) > maximum:
            maximum = sum(arr) - i
        if (sum(arr) - i) < minimum:
            minimum = sum(arr) - i
    print(minimum, maximum, sep=' ')

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)