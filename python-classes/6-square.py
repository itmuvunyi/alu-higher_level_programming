#!/usr/bin/python3


"""This module defines a Square class with private size and position attributes, area method, and my_print method."""


class Square:
    """Class that defines a square by its size and position."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position."""
        self.size = size  # Using the setter for size
        self.position = position  # Using the setter for position
    
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
    
    @property
    def position(self):
        """Getter for position."""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Setter for position."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        if not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value  # Private attribute
    
    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
    
    def my_print(self):
        """Prints the square using the character # considering position."""
        if self.__size == 0:
            print()
        else:
            # Print vertical space for position[1]
            for _ in range(self.__position[1]):
                print()
            
            # Print the square
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
