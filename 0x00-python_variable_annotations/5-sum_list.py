#!/usr/bin/env python3
''' Type-annotated module.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' Returns the sum of floats in a list. '''
    return sum(input_list)
