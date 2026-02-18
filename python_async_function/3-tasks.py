#!/usr/bin/env python3
"""Docstring for python_async_function.3-tasks"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

def task_wait_rando(max_delay: int) -> asyncio.Task:
    """
    Docstring for task_wait_rando
    :param max_delay: Description
    :type max_delay: int
    :return: Description
    :rtype: Task
    """
    return max_delay
