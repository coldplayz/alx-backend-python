#!/usr/bin/env python3
''' Fun with Async IO using asyncio package. '''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


# A co-ordinating coroutine
async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' Spawns @wait_random @n times.
    '''
    # print(*[7 for _ in range(n)])
    # return await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    # tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    coroutines = [wait_random(max_delay) for _ in range(n)]  # above also works

    return [await coro for coro in asyncio.as_completed(coroutines)]
