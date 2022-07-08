import pytest

def funcTest(x):
    return x+3

def test_module():
    assert funcTest (3) == 6