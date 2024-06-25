#!/usr/bin/env python3
"""
Module to implement get_page function with caching and access tracking.
"""

import requests
import redis
import time
from functools import wraps

redis_client = redis.Redis()

def track_access(url):
    """
    Track access count for a specific URL.

    Parameters
    ----------
    url : str
        The URL whose access count needs to be tracked.
    """
    key = f"count:{url}"
    redis_client.incr(key)

def cache_page(url, content):
    """
    Cache the HTML content of a URL with an expiration time of 10 seconds.

    Parameters
    ----------
    url : str
        The URL whose content is being cached.
    content : str
        The HTML content of the URL.
    """
    key = f"cache:{url}"
    redis_client.setex(key, 10, content)

def get_page(url):
    """
    Fetches the HTML content of a URL. If cached,
    returns from cache; otherwise, fetches and caches it.

    Parameters
    ----------
    url : str
        The URL from which to fetch the HTML content.

    Returns
    -------
    str
        The HTML content of the URL.
    """
    cached_content = redis_client.get(f"cache:{url}")
    if cached_content:
        print(f"Cache HIT for {url}")
        return cached_content.decode('utf-8')

    print(f"Cache MISS for {url}")
    response = requests.get(url)
    content = response.text

    cache_page(url, content)

    track_access(url)

    return content

def cache_and_track(func):
    """
    Decorator to cache and track access for the get_page function.
    """
    @wraps(func)
    def wrapper(url):
        cached_content = redis_client.get(f"cache:{url}")
        if cached_content:
            print(f"Cache HIT for {url}")
            return cached_content.decode('utf-8')

        print(f"Cache MISS for {url}")
        content = func(url)

        cache_page(url, content)

        track_access(url)

        return content

    return wrapper

get_page = cache_and_track(get_page)

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    for _ in range(3):
        html_content = get_page(url)
        print(f"Content length: {len(html_content)}")
        time.sleep(1)
