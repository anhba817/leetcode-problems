import { ConnectedComponentsInLCMGraph } from "./lcm_connected_components";

describe("Test Count Connected Components", () => {
  it("Example case 1", async () => {
    // Input: nums = [2,4,8,3,9], threshold = 5
    // Output: 4
    // Explanation: The four connected components are (2, 4), (3), (8), (9).
    const graph = new ConnectedComponentsInLCMGraph([2, 4, 8, 3, 9], 5);
    const results = graph.countComponents();
    expect(results).toEqual(4);
  });
  it("Example case 2", async () => {
    // Input: nums = [2,4,8,3,9,12], threshold = 10
    // Output: 2
    // Explanation: The two connected components are (2, 3, 4, 8, 9), and (12).
    const graph = new ConnectedComponentsInLCMGraph([2, 4, 8, 3, 9, 12], 10);
    const results = graph.countComponents();
    expect(results).toEqual(2);
  });
});
