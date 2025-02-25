#!/usr/bin/python3

def switch_values(a, b):
    a, b = b, a
    return a, b

a = 100
b = 3
print(switch_values(a, b))

