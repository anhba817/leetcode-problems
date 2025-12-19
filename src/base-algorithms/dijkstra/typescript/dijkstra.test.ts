import { dijkstra } from "./dijkstra";

describe("Test Min Heap", () => {
  it("Example case 1", async () => {
    // Input: src = 0, n = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
    // Output:  0 4 8 10 10
    // Explanation:  Shortest Paths:
    // 0 to 1 = 4. 0 → 1
    // 0 to 2 = 8. 0 → 2
    // 0 to 3 = 10. 0 → 2 → 3
    // 0 to 4 = 10. 0 → 1 → 4
    const n = 5;
    const src = 0;

    // edge list format: [u, v, weight]
    const edges = [
      [0, 1, 4],
      [0, 2, 8],
      [1, 4, 6],
      [2, 3, 2],
      [3, 4, 10],
    ];

    const result = dijkstra(n, edges, src);
    expect(result).toEqual([0, 4, 8, 10, 10]);
  });
});
