#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file and returns the number of characters written.
    
    Args:
        filename (str): The name of the file to write to. Default is an empty string.
        text (str): The text to write into the file. Default is an empty string.
    
    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
