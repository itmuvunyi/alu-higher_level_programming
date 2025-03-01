#!/usr/bin/python3


"""This module defines a Square class with a private size attribute and an area method."""


class Square:
    """Class that defines a square by its size."""
    
    def __init__(self, size=0):
        """Initializes the square with a size."""
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size  # Private attribute
    
    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
