from .solution import max_power


def test_example_case():
    assert max_power([1, 2, 4, 5, 0], 1, 2) == 5


def test_no_extra_stations():
    assert max_power([2, 2, 2], 0, 0) == 2


def test_full_coverage_window():
    assert max_power([0, 0, 0], 2, 3) == 3


def test_sparse_power_requires_new_station():
    assert max_power([10, 0, 0], 1, 1) == 1


def test_large_window_balances_edges():
    stations = [0, 5, 0, 0, 5, 0]
    # Additional stations can lift every city to at least 6 power
    assert max_power(stations, 2, 2) == 6
