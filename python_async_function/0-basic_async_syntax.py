#!/usr/bin/env python3


""" Imported Modules """


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Find The Delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
    """ Return Delay """
