#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class.

    Args:
    obj (any): The object to check
    a_clas (type): The class to match the type of obj to.
    Returns:
    if obj is exactly an instance of a_clas - True.
    Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
