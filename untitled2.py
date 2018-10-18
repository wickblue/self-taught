#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:25:34 2018

@author: philllippierce
"""

def staircase(n):
    for i in range(n):
        print('{:>{}}'.format('#'*(i+1), n))
staircase(6)