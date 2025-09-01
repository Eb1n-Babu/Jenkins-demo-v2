import pytest
from app import *

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") != "Hello, Alice!"