#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def abss(*a):
    if a:
        summ = 0
        flag_zero = False
        
        for arg in a:
            if arg == 0:
                flag_zero = True
            elif flag_zero:
                summ += abs(arg) 
                
        return summ    

    else:
        return None


if __name__ == "__main__":
    p = list(int(i) for i in input("Введите значения: ").split())
    result = abss(*p)
    print(result)

