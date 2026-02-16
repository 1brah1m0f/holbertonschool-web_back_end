#!/usr/bin/env python3
wait_random = __import__('1-concurrent_coroutines').wait_random
import asyncio

async def wait_n(n: int, max_delay: int):
    