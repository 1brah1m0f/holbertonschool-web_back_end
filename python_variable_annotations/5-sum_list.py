#!/usr/bin/env python3
"""Docstring for python_variable_annotations.5-sum_list"""


def sum_list(input_list: list[float]) -> float:
    s = 0
    """Docstring for sum_list"""
    for i in input_list:
        s = s + i
    return float(s)
