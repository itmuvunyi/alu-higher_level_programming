#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements
    a1, a2 = (tuple_a + (0, 0))[:2]  # Fill with 0 if tuple_a is smaller than 2 elements
    b1, b2 = (tuple_b + (0, 0))[:2]  # Fill with 0 if tuple_b is smaller than 2 elements
    
    return (a1 + b1, a2 + b2)

