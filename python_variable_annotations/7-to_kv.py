#!/usr/bin/env python3


""" Import Module """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Find The Tuple """
    return k, v * v
    """ Return Tuple """
