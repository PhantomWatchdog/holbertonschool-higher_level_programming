#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e))
        return False
