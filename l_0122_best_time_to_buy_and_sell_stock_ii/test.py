import pytest

from l_0122_best_time_to_buy_and_sell_stock_ii.solution import Solution


@pytest.mark.parametrize(
    "prices,expected_profit",
    (
        ([7,1,5,3,6,4], 7),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0),
    )
)
def test(prices, expected_profit):

    actual_profit: int = Solution().maxProfit(prices)

    assert actual_profit == expected_profit
