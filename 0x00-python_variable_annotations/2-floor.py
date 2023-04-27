#!/usr/bin/env python3
''' Type-annotated module.
'''


def floor(n: float) -> int:
    ''' Returns the floor of n. '''
    # Convert float @n to string
    f_str = str(n)

    # Extract the integer part
    i_str = f_str.split('.', maxsplit=1)[0]

    # Convert to int
    i = int(i_str)

    return i
