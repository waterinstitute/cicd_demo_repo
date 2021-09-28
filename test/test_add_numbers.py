#!/usr/bin/env python3 

from src.add_numbers import add_numbers

def test_add_two_numbers():
    assert add_numbers(3,5) == 8

def test_add_three_numbers():
    assert add_numbers(2,3,4) == 9
