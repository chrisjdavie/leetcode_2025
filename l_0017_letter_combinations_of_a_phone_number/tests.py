import pytest

from l_0017_letter_combinations_of_a_phone_number.solution import Solution

@pytest.mark.parametrize(
    "digits,expected_output",
    (
        (
            "23",
            ["ad","ae","af","bd","be","bf","cd","ce","cf"],
        ),
        (
            "",
            []
        ),
        (
            "2",
            ["a","b","c"]
        )
    ),
)
def test(digits, expected_output):
    assert Solution().letterCombinations(digits) == expected_output
