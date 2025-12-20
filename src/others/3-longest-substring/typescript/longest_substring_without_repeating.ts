/**
 * Returns the longest length of a substring with all unique characters.
 *
 * Implements the sliding window pattern: expand to the right while tracking the
 * unique characters in a Set, and shift the left edge whenever a duplicate is
 * encountered to keep the window valid.
 */
export function lengthOfLongestSubstring(s: string): number {
  let left = 0;
  let maxLength = 0;
  const charSet = new Set(); // Stores characters currently in the window
  for (let right = 0; right < s.length; right++) {
    // Remove chars from the left until s[right] is unique again
    while (charSet.has(s[right])) {
      charSet.delete(s[left]);
      left++;
    }
    charSet.add(s[right]);
    maxLength = Math.max(maxLength, right - left + 1);
  }
  return maxLength;
}
