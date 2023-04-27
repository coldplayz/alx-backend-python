#!/usr/bin/env python3
''' Type-annotated module.
'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Returns a tuple based on the arguments. '''
    return (k, (v ** 2))
