def lengthOfLongestSubstring(s: str) -> int:
    """Return length of the longest substring without repeating characters.

    Maintains a sliding window of unique characters using a set; expands the
    window by moving the right pointer, but when a duplicate is seen, shrinks
    the window from the left until uniqueness is restored.
    """

    left = 0
    maxLength = 0
    charSet = set()  # Characters currently inside the sliding window
    for right in range(len(s)):
        # Drop characters from the left until s[right] becomes unique
        while s[right] in charSet:
            charSet.discard(s[left])
            left += 1
        charSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength
