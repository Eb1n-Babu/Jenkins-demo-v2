from app import greet
import pytest

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") != "Hello, Alice!"