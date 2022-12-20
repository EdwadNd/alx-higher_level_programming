#!/usr/bin/python3


def safe_print_division(a, b):
    """
    divides two integers and prints the resultult
    catches divide by zero exception
    """
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result