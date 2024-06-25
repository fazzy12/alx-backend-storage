#!/usr/bin/env python3
"""
Main file
"""
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import redis
from exercise import Cache

cache = Cache()

# Test cases
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    retrieved_value = cache.get(key, fn=fn)
    assert retrieved_value == value
    print(f"Stored value: {value} -> Retrieved value: {retrieved_value}")

# Testing get_str and get_int methods
str_key = cache.store("hello")
int_key = cache.store(42)

assert cache.get_str(str_key) == "hello"
assert cache.get_int(int_key) == 42

print("All tests passed.")
