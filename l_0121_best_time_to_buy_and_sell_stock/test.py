import pytest

from l_0121_best_time_to_buy_and_sell_stock.solution import Solution

@pytest.mark.parametrize(
    "prices,expected_profit",
    (
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
    )
)
def test(prices, expected_profit):

    actual_profit = Solution().maxProfit(prices)

    assert expected_profit == actual_profit
