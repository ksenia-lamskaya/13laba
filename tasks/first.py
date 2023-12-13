#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def average(*a):
    if a:
        n = len(a)
        y = 1
        for i in a:
            y *= i
        
        g = math.pow(y, 1/n)
        return g

    else:
        return None


if __name__ == "__main__":
    arg = list(int(i) for i in input("Введите значения: ").split())
    result = average(*arg)
    print(result)

