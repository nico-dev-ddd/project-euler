from project_euler.pb0_10.problem1.multipleof3or5 import sum_multiples


def test_sum_multiples() -> None:
    assert sum_multiples(1) == 0
    assert sum_multiples(2) == 0
    assert sum_multiples(3) == 0
    assert sum_multiples(4) == 3
    assert sum_multiples(5) == 3
    assert sum_multiples(6) == 8
    assert sum_multiples(7) == 14
    assert sum_multiples(8) == 14
    assert sum_multiples(9) == 14
    assert sum_multiples(10) == 23
    assert sum_multiples(11) == 33
