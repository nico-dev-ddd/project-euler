from project_euler.pb11_20.problem14.collatz_sequence import collatz, length_seq_collatz


def test_collatz() -> None:
    assert collatz(13) == 40
    assert collatz(40) == 20


def test_length_seq_collatz() -> None:
    assert length_seq_collatz(13) == 10
