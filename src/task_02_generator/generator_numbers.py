'''Numbers generator module'''

import re
from typing import Callable
from collections.abc import Generator

def extract_numbers_from_text(text: str) -> list[float]:
    '''Extract all real numbers from text'''
    pattern = r" {1}-?\d+\.?\d* {1}"
    return [float(x) for x in re.findall(pattern, text)]

def generator_numbers(text: str) -> Generator[float]:
    '''Numbers generator from text'''
    for number in extract_numbers_from_text(text):
        yield number

def sum_profit(text: str, func: Callable[[],str]) -> float:
    '''Sum all numbers in numbers generator'''
    return sum(func(text))
