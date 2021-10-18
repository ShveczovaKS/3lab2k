#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    t = 0
    m = 1
    for el in A:
        if(el > 8 and el < 18 and (el % 10) == 0):
            t+=1
            m*=el
    print(t)
    print(m)