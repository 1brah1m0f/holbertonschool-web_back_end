#!/usr/bin/env python3
"""Measure runtime of async_comprehension."""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 times in parallel and measure runtime."""

    start = time.perf_counter()

    tasks = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*tasks)

    end = time.perf_counter()

    return end - start
