#!/usr/bin/python3

def read_file(filename=""):
    """Reads a file
    Args:
        filename (str): filename/filepath
    """
    if type(filename) is str:
        with open(filename, 'r', encoding="UTF-8") as fyle:
            print(fyle.read(), end='')