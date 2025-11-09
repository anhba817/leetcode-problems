import { shiftingLetters } from "./shifting_letters_ii";

describe("Shifting Letters II", () => {
  test("Example case 1", () => {
    // Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
    // Output: "ace"
    // Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
    // Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
    // Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
    const result = shiftingLetters("abc", [
      [0, 1, 0],
      [1, 2, 1],
      [0, 2, 1],
    ]);
    expect(result).toEqual("ace");
  });
  test("Example case 2", () => {
    // Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
    // Output: "catz"
    // Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
    // Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
    const result = shiftingLetters("dztz", [
      [0, 0, 0],
      [1, 1, 1],
    ]);
    expect(result).toEqual("catz");
  });
});
