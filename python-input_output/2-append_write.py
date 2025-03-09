#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 encoded text file and returns the number of characters added.
    
    Args:
        filename (str): The name of the file to append to. Default is an empty string.
        text (str): The text to append to the file. Default is an empty string.
    
    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
