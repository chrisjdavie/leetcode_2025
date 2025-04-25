import pytest

from l_0125_valid_palindrome.solution import Solution


@pytest.mark.parametrize(
    "s,expected_output",
    (
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False)
    )
)

def test(s, expected_output):
    assert expected_output == Solution().isPalindrome(s)
