#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """initializes a new square.

        Args:
            size (init): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets/sets the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
