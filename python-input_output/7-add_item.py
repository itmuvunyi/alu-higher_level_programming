#!/usr/bin/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    """
    Adds all command-line arguments to a Python list and saves them to a file in JSON format.
    
    The list is stored in 'add_item.json'. If the file exists, the arguments are appended to the existing list.
    If the file does not exist, it is created.
    """
    filename = "add_item.json"
    
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []
    
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
