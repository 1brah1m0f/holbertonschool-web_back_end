#!/usr/bin/env python3
"""Docstring for python_async_comprehension.0-async_generator"""
import asyncio
import random

async def async_generator() -> Generator[float, None, None]:
    """Docstring for async_generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
