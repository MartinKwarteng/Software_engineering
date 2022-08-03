def add(a, b):
    # Add inputted numbers 
    sum = a + b
    return sum


def subtract (x, y):
    # Subtracts inputted numbers 
    result = x - y
    return result


def multiply(a, b):
    # Mulitlpy inputted numbers 
    product = a * b
    return product


def division(x, y):
    # Divides inputted numbers 
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x / y

