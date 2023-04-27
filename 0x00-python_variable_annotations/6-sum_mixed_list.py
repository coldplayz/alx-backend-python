#!/usr/bin/env python3
''' Type-annotated module.
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    ''' Returns the sum of a list. '''
    return sum(mxd_list)
