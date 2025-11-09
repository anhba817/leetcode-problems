import { maxPower } from "./solution";

describe("Maximize the Minimum Powered City", () => {
  test("Example case 1", () => {
    // Input: stations = [1,2,4,5,0], r = 1, k = 2
    // Output: 5
    // Explanation:
    // One of the optimal ways is to install both the power stations at city 1.
    // So stations will become [1,4,4,5,0].
    // - City 0 is provided by 1 + 4 = 5 power stations.
    // - City 1 is provided by 1 + 4 + 4 = 9 power stations.
    // - City 2 is provided by 4 + 4 + 5 = 13 power stations.
    // - City 3 is provided by 5 + 4 = 9 power stations.
    // - City 4 is provided by 5 + 0 = 5 power stations.
    // So the minimum power of a city is 5.
    // Since it is not possible to obtain a larger power, we return 5.
    const result = maxPower([1, 2, 4, 5, 0], 1, 2);
    expect(result).toEqual(5);
  });
  test("Example case 2", () => {
    // Input: stations = [4,4,4,4], r = 0, k = 3
    // Output: 4
    // Explanation:
    // It can be proved that we cannot make the minimum power of a city greater than 4.
    const result = maxPower([4,4,4,4], 0, 3);
    expect(result).toEqual(4);
  });
});
