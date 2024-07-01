#!/usr/bin/env python3

"""Generic utility functions for
GitHub Organization Client."""

import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]

def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a value in a nested map using a sequence of keys.
    
    Parameters
    ----------
    nested_map: Mapping
        A nested dictionary or similar mapping.
    path: Sequence
        A sequence of keys representing the path to the value.
    
    Returns
    -------
    Any
        The value found at the end of the key path.
    
    Raises
    ------
    KeyError
        If a key in the path is not found in the nested map.
    
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map

def get_json(url: str) -> Dict:
    """Retrieve JSON data from a remote URL.
    
    Parameters
    ----------
    url: str
        The URL to fetch JSON data from.
    
    Returns
    -------
    Dict
        The JSON response converted to a dictionary.
    
    Example
    -------
    >>> url = "https://api.github.com/orgs/google"
    >>> get_json(url)
    {...}  # JSON response from the URL
    """
    response = requests.get(url)
    return response.json()

def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method's result.
    
    Parameters
    ----------
    fn: Callable
        The function to memoize.
    
    Returns
    -------
    Callable
        The memoized function.
    
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        
        """Wrapper function to check and store the
        result of the original function."""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
