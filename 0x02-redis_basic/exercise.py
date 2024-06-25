#!/usr/bin/env python3
"""
This module defines a Cache class for interacting with a Redis database.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class to interact with a Redis database.

    Methods
    -------
    store(data: Union[str, bytes, int, float]) -> str
        Stores data in Redis and returns the generated key.

    get(key: str, fn: Optional[Callable] = None) ->
        Union[str, bytes, int, float, None]
        Retrieves data from Redis and optionally applies a conversion function.

    get_str(key: str) -> str
        Retrieves data from Redis as a UTF-8 decoded string.

    get_int(key: str) -> int
        Retrieves data from Redis as an integer.
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

    def get(self, key: str, fn: Optional[Callable] =
            None)-> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis and optionally applies a conversion function.

        Parameters
        ----------
        key : str
            The key for the data in Redis.
        fn : Optional[Callable]
            A function to apply to the data for conversion.

        Returns
        -------
        Union[str, bytes, int, float, None]
            The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves data from Redis as a UTF-8 decoded string.

        Parameters
        ----------
        key : str
            The key for the data in Redis.

        Returns
        -------
        str
            The data retrieved from Redis, decoded as a UTF-8 string.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieves data from Redis as an integer.

        Parameters
        ----------
        key : str
            The key for the data in Redis.

        Returns
        -------
        int
            The data retrieved from Redis, converted to an integer.
        """
        return self.get(key, int)
