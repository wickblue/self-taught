#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:49:00 2018

@author: philllippierce
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def split(n, i, bill, b):
    bill.remove(bill[i])
    total = 0
    for item in bill:
        total += item
    fair = total / 2
    if fair != b:
        return int((b - fair))
    else:
        return 'Bon Appetit'


n, i = input().strip().split(' ')
n, i = [int(n), int(i)]
bill = list(map(int, input().strip().split(' ')))
b = int(input().strip())

result = split(n, i, bill, b)
print(result)

