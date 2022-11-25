def add_integer(a, b=98):
    if (type(a) is int or type(a) is float):
        if (type(a) is float):
            a = round(a)
    else:
        raise TypeError("a must be an integer")

    if (type(b) is int or type(b) is float):
        if (type(b) is float):
            b = round(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
