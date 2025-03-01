#!/usr/bin/python3


"""This module defines a Square class with a private size attribute, area method, and my_print method."""


class Square:
    """Class that defines a square by its size."""
    
    def __init__(self, size=0):
        """Initializes the square with a size."""
        self.size = size  # Using the setter to set the initial size
    
    @property
    def size(self):
        """Getter for size."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value  # Private attribute
    
    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
    
    def my_print(self):
        """Prints the square using the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
