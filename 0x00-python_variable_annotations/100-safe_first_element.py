#!/usr/bin/env python3
''' Type-annotated module.
'''
from typing import Union, Sequence, Any


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Returns the first item of lst or none if lst is empty.
    '''
    if lst:
        return lst[0]

    return None
