#pragma once

#include <string>

using namespace std;

/**
 * Returns the length of the longest substring without repeating characters in s.
 *
 * Uses a sliding window and a hash set to track the current run of unique
 * characters, shrinking the window from the left whenever a duplicate appears.
 */
int lengthOfLongestSubstring(string s);
