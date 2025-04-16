import pytest

from l_0134_gas_station.solution import Solution

@pytest.mark.parametrize(
    "gas,cost,expected_output",
    (
        ([1,2,3,4,5],[3,4,5,1,2],3),
        ([2,3,4],[3,4,3],-1),
        ([2],[2],0),
    )
)
def test(gas, cost, expected_output):

    assert Solution().canCompleteCircuit(gas, cost) == expected_output
