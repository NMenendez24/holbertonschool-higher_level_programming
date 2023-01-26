#!/usr/bin/python3
def safe_print_division(a, b):
    if b == 0:
        result = None
    try:
        result = a / b
        print("Inside result: {:.2}".format(result))
        return result
    except:
        print("Inside result: {}".format(result))
        return None
    finally:
        pass
