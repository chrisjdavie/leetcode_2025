import pytest

from l_0020_valid_parentheses.previous.solution import Solution


@pytest.mark.parametrize(
    "s,expected_output",
    (
        ("()", True),
        (r"()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("[", False),
    )
)
def test(s, expected_output):
    assert expected_output == Solution().isValid(s)
