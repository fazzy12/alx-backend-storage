#!/usr/bin/env python3
"""
This module defines a Cache class for interacting with a Redis database.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to interact with a Redis database.

    Methods
    -------
    store(data: Union[str, bytes, int, float]) -> str
        Stores data in Redis and returns the generated key.
    """

    def __init__(self):
        """
        Initializes a new Cache instance and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis using a randomly generated key.

        Parameters
        ----------
        data : Union[str, bytes, int, float]
            The data to be stored in Redis.

        Returns
        -------
        str
            The generated key for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
