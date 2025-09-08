import pytest

from l_1768_merge_strings_alternately.solution import Solution


@pytest.mark.parametrize(
    "word1,word2,expected_output",
    [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    ],
)
def test(word1, word2, expected_output):
    assert Solution().mergeAlternately(word1, word2) == expected_output
