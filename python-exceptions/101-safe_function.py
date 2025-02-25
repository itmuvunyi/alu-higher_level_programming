#!/usr/bin/python3


def safe_function(fct, *args):
    try:
        # Attempt to call the function with the provided arguments
        return fct(*args)
    except Exception as e:
        # If an error occurs, print the exception to stderr
        import sys
        print(f"Exception: {e}", file=sys.stderr)
        return None
