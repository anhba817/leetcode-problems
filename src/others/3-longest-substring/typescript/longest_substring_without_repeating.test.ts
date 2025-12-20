import { lengthOfLongestSubstring } from "./longest_substring_without_repeating";

describe("Longest substring without repeating characters", () => {
  test("Example case 1", () => {
    // Input: s = "abcabcbb"
    // Output: 3
    // Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
    const result = lengthOfLongestSubstring("abcabcbb");
    expect(result).toEqual(3);
  });
  test("Example case 2", () => {
    // Input: s = "bbbbb"
    // Output: 1
    // Explanation: The answer is "b", with the length of 1.
    const result = lengthOfLongestSubstring("bbbbb");
    expect(result).toEqual(1);
  });
  test("Example case 2", () => {
    // Input: s = "pwwkew"
    // Output: 3
    // Explanation: The answer is "wke", with the length of 3.
    const result = lengthOfLongestSubstring("pwwkew");
    expect(result).toEqual(3);
  });
});
