#!/usr/bin/env python3
''' Fun with Async IO using asyncio package. '''
import asyncio
# from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' Returns an asyncio.Task object using @max_delay.
    '''
    coroutine = wait_random(max_delay)  # collect a coro
    task = asyncio.create_task(coroutine)  # wrap a coro in a Task
    return task
