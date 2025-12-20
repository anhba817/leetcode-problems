from .longest_substring_without_repeating import lengthOfLongestSubstring


def test_longest_substring_without_repeating_example_case_1():
    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
    result = lengthOfLongestSubstring("abcabcbb")
    assert result == 3


def test_longest_substring_without_repeating_example_case_2():
    # Input: s = "bbbbb"
    # Output: 1
    # Explanation: The answer is "b", with the length of 1.
    result = lengthOfLongestSubstring("bbbbb")
    assert result == 1


def test_longest_substring_without_repeating_example_case_3():
    # Input: s = "pwwkew"
    # Output: 3
    # Explanation: The answer is "wke", with the length of 3.
    result = lengthOfLongestSubstring("pwwkew")
    assert result == 3
