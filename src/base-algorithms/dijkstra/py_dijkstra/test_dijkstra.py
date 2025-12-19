from .dijkstra import dijkstra


def test_dijkstra_example_case_1():
    # Input: src = 0, n = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
    # Output:  0 4 8 10 10
    # Explanation:  Shortest Paths:
    # 0 to 1 = 4. 0 → 1
    # 0 to 2 = 8. 0 → 2
    # 0 to 3 = 10. 0 → 2 → 3
    # 0 to 4 = 10. 0 → 1 → 4
    n = 5
    src = 0

    # edge list format: {u, v, weight}
    edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]

    result = dijkstra(n, edges, src)
    assert result == [0, 4, 8, 10, 10]
