def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    if operation == 'add':
        if make_int:
            return f"{message} {int(add(a, b))}"
        else:
            return f"{message} {add(a, b)}"

    elif operation == 'subtract':
        if make_int:
            return f"{message} {int(sub(a, b))}"
        else:
            return f"{message} {sub(a, b)}"

    elif operation == 'multiply':
        if make_int:
            return f"{message} {int(multi(a, b))}"
        else:
            return f"{message} {multi(a, b)}"
            
    elif operation == 'divide':
        if make_int:
            return f"{message} {int(div(a, b))}"
        else:
            return f"{message} {div(a, b)}"
    else:
        return None

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

print(calculate('add', 2.5, 4))
print(calculate('subtract', 4, 1.5, make_int=True))
print(calculate('multiply', 1.5, 2))
print(calculate('divide', 10, 4, message='I got'))
print(calculate('foo', 2, 3))