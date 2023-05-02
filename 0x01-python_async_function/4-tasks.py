#!/usr/bin/env python3
''' Fun with Async IO using asyncio package. '''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


# A co-ordinating coroutine
async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' Spawns @task_wait_random @n times.
    '''
    # tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # above also works

    return [await coroutine for coroutine in asyncio.as_completed(tasks)]
