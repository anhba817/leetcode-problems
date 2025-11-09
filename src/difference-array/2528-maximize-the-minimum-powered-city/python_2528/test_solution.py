from .solution import max_power


def test_example_case():
    # Input: stations = [1,2,4,5,0], r = 1, k = 2
    # Output: 5
    # Explanation:
    # One of the optimal ways is to install both the power stations at city 1.
    # So stations will become [1,4,4,5,0].
    # - City 0 is provided by 1 + 4 = 5 power stations.
    # - City 1 is provided by 1 + 4 + 4 = 9 power stations.
    # - City 2 is provided by 4 + 4 + 5 = 13 power stations.
    # - City 3 is provided by 5 + 4 = 9 power stations.
    # - City 4 is provided by 5 + 0 = 5 power stations.
    # So the minimum power of a city is 5.
    # Since it is not possible to obtain a larger power, we return 5.
    assert max_power([1, 2, 4, 5, 0], 1, 2) == 5


def test_example_case_2():
    # Input: stations = [4,4,4,4], r = 0, k = 3
    # Output: 4
    # Explanation:
    # It can be proved that we cannot make the minimum power of a city greater than 4.
    assert max_power([4, 4, 4, 4], 0, 3) == 4


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
