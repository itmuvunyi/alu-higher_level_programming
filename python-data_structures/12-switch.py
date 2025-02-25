#!/usr/bin/python3

def switch_values(a, b):
    # Switch the values of a and b
    a, b = b, a
    return a, b

a = 5
b = 10
print(switch_values(a, b))
