#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:13:07 2018

@author: philllippierce
"""

def gradingStudents(grades):
    for i in range(4):
        if grades[i] > 37:
            if (grades[i] % 5) > 2:
                grades[i] = ((grades[i] // 5) + 1) * 5
                
    return grades

grades = [73, 67, 38, 33]
print(gradingStudents(grades))