def write_file(filename="", text=""):
    """Writes text to filename
    Args:
        filename (str): filename/filepath
        text (str): text to write
    """
    count = 0 
    if type(filename) is str and type(text) is str:
        with open(filename, 'w') as fyle:
            count = fyle.write(text)
    return count
