#!/usr/bin/python3
"""works only if name is set to main"""
if __name__ == "__main__":

    from add_0 import add
    a = 1
    b = 2

"""use print .format style"""
print("{} + {} = {}".format(a, b, add(a, b)))
