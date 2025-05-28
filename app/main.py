from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}
    def wrapper(*args, **kwargs):
        cache_kay = (args, tuple(sorted(kwargs.items())))
        if cache_kay in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_kay]
        print("Calculating new result")
        cache_dict[cache_kay] = func(*args, **kwargs)
        return cache_dict[cache_kay]
    return wrapper
