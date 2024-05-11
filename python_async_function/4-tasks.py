#!/usr/bin/env python3


""" Import Modules """


import asyncio
from typing import List

task_wait_random = __import__('3-task_wait_random').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls task_wait_random n times with the specified max_delay and returns a list of the results.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list containing the results of calling task_wait_random.
    """
    results = []

    for _ in range(n):
        results.append(await task_wait_random(max_delay))

    return results

if __name__ == "__main__":
    asyncio.run(task_wait_n)
  """ Return Async Function """"
