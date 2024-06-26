#!/usr/bin/env python3


"""Import Module """


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Find a list of tuples containing elements of the input list. """
    return [(i, len(i)) for i in lst]
    """ Return a list"""
