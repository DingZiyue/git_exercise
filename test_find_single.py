import pytest
from find_single import find_single


def test_normal_case():
    assert find_single([1, 2, 3, 2, 1]) == 3

def test_single_element():
    assert find_single([4]) == 4

def test_single_at_beginning():
    assert find_single([5, 1, 1]) == 5

def test_single_at_end():
    assert find_single([1, 1, 5]) == 5

def test_negative_numbers():
    assert find_single([-1, 2, -1]) == 2

def test_large_array():
    assert find_single([1, 2, 3, 4, 3, 1, 2]) == 4
