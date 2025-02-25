#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        # Try printing the value as an integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # If an error occurs, print it to stderr
        import sys
        print(f"Exception: {e}", file=sys.stderr)
        return False
