import pytest

from src.algorithms import add, is_palindrome


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative_and_positive():
    assert add(-1, 1) == 0


@pytest.mark.parametrize("s,expected", [
    ("", True),
    ("A man a plan a canal Panama", True),
    ("Hello", False),
    ("No lemon, no melon", True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected
