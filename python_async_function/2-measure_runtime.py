#!/usr/bin/env python3


""" Import Modules """

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Find The Function that measures the total execution time """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return total_time / n
    """ Return The Total Execution Time """
  