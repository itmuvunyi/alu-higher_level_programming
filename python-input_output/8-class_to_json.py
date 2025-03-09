#!/usr/bin/python3

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures for JSON serialization of an object.
    
    Args:
        obj: An instance of a class.
    
    Returns:
        dict: A dictionary representation of the object with serializable attributes.
    """
    return obj.__dict__
