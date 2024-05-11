#!/usr/bin/env python3


""" Import Modules """


import asyncio
from typing import List
from asyncio import gather


async def task_wait_random(max_delay):
    """Simulate A Random Wait. """
    delay = randint(0, max_delay)
    await asyncio.sleep(delay)

async def task_wait_n(n, max_delay):
    """ Waits for n tasks to complete. """
    tasks = []
    for _ in range(n):
        tasks.append(asyncio.create_task(task_wait_random(max_delay)))
    await asyncio.gather(*tasks)
    """ Return Async Function. """
