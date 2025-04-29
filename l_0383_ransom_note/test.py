import pytest

from l_0383_ransom_note.solution import Solution

@pytest.mark.parametrize(
    "ransomNote,magazine,expected_output",
    (
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
    )
)
def test(ransomNote, magazine, expected_output):

    assert Solution().canConstruct(ransomNote, magazine) == expected_output
