#!/usr/bin/env python3
''' Fun with async generators and comprehensions.
'''
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Generates an async list comprehension using an async generator.
    '''
    return [n async for n in async_generator()]
