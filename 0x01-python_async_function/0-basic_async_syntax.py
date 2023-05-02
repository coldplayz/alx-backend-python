#!/usr/bin/env python3
''' Fun with Async IO using asyncio package. '''
import asyncio
import random


# A coroutine
async def wait_random(max_delay: int = 10) -> float:
    ''' Waits for a random amount of time amd returns it.
    '''
    duration = random.uniform(0, max_delay)
    await asyncio.sleep(duration)
    return duration
