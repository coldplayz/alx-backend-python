#!/usr/bin/env python3
''' Type-annotated module.
'''
from typing import List, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Returns a function that multiplies a float by a multiplier. '''
    def f2(multiplier2: float) -> float:
        ''' Returns a multiplied float. '''
        return multiplier * multiplier2

    return f2
