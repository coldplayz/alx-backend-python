#!/usr/bin/env python3
''' Fun with Async IO using asyncio package. '''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Returns average time to run coroutine wait_n.

        Measures the total execution time for wait_n(n, max_delay), and
        returns total_time / n. Your function should return a float.
    '''
    time_b4 = time.time()
    asyncio.run(wait_n(n, max_delay))
    duration = time.time() - time_b4
    return duration / n
