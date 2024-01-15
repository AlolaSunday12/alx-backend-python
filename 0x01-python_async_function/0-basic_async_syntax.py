#!/usr/bin/env python3
"""
Module with an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10)
    named wait_random that waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.

    Parameters:
    - max_delay (int): Maximum delay for the random sleep.

    Returns:
    - float: Random delay between 0 and max_delay.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
