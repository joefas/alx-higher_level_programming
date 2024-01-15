#!/usr/bin/python3
"""Defines a base geomtery class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implememted")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
            name(str): The name of the parameter.
            value(int): The parameter to validate.
        Raises:
            TypeError: If value is not integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
