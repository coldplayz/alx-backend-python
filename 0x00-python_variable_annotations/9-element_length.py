#!/usr/bin/env python3
''' Type-annotated module.
'''
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Returns a list of tuples. '''
    return [(i, len(i)) for i in lst]
