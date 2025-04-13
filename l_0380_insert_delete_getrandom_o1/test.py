import pytest

from l_0380_insert_delete_getrandom_o1.solution import RandomizedSet

@pytest.mark.parametrize(
    "commands,inputs,expected_results",
    (
        (
            ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"],
            [[],[1],[2],[2],[],[1],[2],[]],
            [None, True, False, True, {1, 2}, True, False, {2,}],
        ),
    )
)
def test(commands, inputs, expected_results):

    randomized_set: RandomizedSet = RandomizedSet()

    for com, inp, exp in zip(commands[1:], inputs[1:], expected_results[1:]):
        if com == "insert":
            res = randomized_set.insert(inp[0])
            assert res == exp
        if com == "remove":
            res = randomized_set.remove(inp[0])
            assert res == exp
        if com == "getRandom":
            res = randomized_set.getRandom()
            assert res in exp
