#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except IndexError:
        pass
    print()
    return count


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
