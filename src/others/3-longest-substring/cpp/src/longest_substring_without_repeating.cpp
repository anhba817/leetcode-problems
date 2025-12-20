#include "longest_substring_without_repeating.hpp"

#include <unordered_set>
#include <algorithm>

using namespace std;
int lengthOfLongestSubstring(string s)
{
    int left = 0;
    int maxLength = 0;
    unordered_set<char> charSet; // Current window's unique characters
    for (int right = 0; right < s.length(); right++)
    {
        // Shrink the window until the duplicate s[right] is removed
        while (charSet.find(s[right]) != charSet.end())
        {
            charSet.erase(s[left]);
            left++;
        }
        charSet.insert(s[right]);
        // Update the best answer for the current window size
        maxLength = max(maxLength, right - left + 1);
    }
    return maxLength;
}
