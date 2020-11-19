
dumb_global_variable = 19


def dumb_function():
    global dumb_global_variable

    dumb_global_variable = 10


def add(a: float, b: float, *c, force_int=False, **extras) -> list:
    '''
        Description
            Adds number together
        params
            a: int or float
            b: int or float
            c: and other ints or floats
            force_int: bool - Will force all parameters to be ints

    '''
    if force_int:
        a = int(a)
        b = int(b)
        c = [int(n) for n in c]

    total = a + b
    for number in c:
        total += number

    for key, value in extras.items():
        print(key, value)

    return total


# x = add(10.5, 11.2,  go="yes", stop="ok", whatever="sure")
# print(x)

y = add(10, 10)
print(y)


if y >= 20:
    correct = True
else:
    correct = False

print(correct)
