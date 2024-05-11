#!/usr/bin/env python3


""" Import Module """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Find a function that multiplies a float by the given multiplier. """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    """ Return the function """
    return multiplier_function
