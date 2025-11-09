from .lcm_connected_components import ConnectedComponentsInLCMGraph


def test_lcm_connected_components_example_case_1():
    # Input: nums = [2,4,8,3,9], threshold = 5
    # Output: 4
    # Explanation: The four connected components are (2, 4), (3), (8), (9).
    graph = ConnectedComponentsInLCMGraph([2, 4, 8, 3, 9], 5)
    results = graph.count_components()
    assert results == 4


def test_lcm_connected_components_example_case_2():
    # Input: nums = [2,4,8,3,9,12], threshold = 10
    # Output: 2
    # Explanation: The two connected components are (2, 3, 4, 8, 9), and (12).
    graph = ConnectedComponentsInLCMGraph([2, 4, 8, 3, 9, 12], 10)
    results = graph.count_components()
    assert results == 2
