import pytest

from l_0013_roman_to_integer.solution import Solution


@pytest.mark.parametrize(
    "s,expected_output",
    (
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    )
)
def test(s, expected_output):
    assert expected_output == Solution().romanToInt(s)
