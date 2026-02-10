#!/usr/bin/env python3
"""Docstring for python_variable_annotations.7-to_kv"""

from typing import List, Union

def to_kv(k: str, v: int | float) -> tuple[str, float]:
    return (k, float(v * v))
