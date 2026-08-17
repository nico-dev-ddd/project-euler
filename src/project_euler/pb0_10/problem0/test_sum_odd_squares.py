from project_euler.pb0_10.problem0.sum_odd_squares import sum_odd_squares


class TestSumOddSquares:
    def test_sum_odd_squares(self):
        assert sum_odd_squares(1) == 1
        assert sum_odd_squares(2) == 1
        assert sum_odd_squares(3) == 10
        assert sum_odd_squares(4) == 10
        assert sum_odd_squares(5) == 35
