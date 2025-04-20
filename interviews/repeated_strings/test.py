import pytest

from interviews.repeated_strings.solution import reduce_repeated_strings


@pytest.mark.parametrize(
    "input_string,max_len,expected_output",
    (
        ("aa", 1, "a"),
        ("aaaaabccccddd", 2, "aabccdd"),
        ("asdoifjaoijoioijjiodd", 0, "")
    )
)
def test(input_string, max_len, expected_output):
    actual_output: str = reduce_repeated_strings(input_string, max_len)

    assert actual_output == expected_output
