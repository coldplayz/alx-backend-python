#!/usr/bin/env python3
''' Type-annotated module.
'''
from typing import Union, Mapping, Any, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    ''' Returns a dictionary value, or the default.
    '''
    if key in dct:
        return dct[key]

    return default
