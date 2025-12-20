#include "longest_substring_without_repeating.hpp"

#include <gtest/gtest.h>

#include <string>
#include <vector>

namespace
{
  struct TestCase
  {
    std::string s;
    int expected;
  };
} // namespace

class LongestSubstringWithoutRepeatingTest : public ::testing::TestWithParam<TestCase>
{
};

TEST_P(LongestSubstringWithoutRepeatingTest, ProducesExpectedString)
{
  const TestCase &test = GetParam();
  EXPECT_EQ(test.expected, lengthOfLongestSubstring(test.s));
}

INSTANTIATE_TEST_SUITE_P(
    Examples,
    LongestSubstringWithoutRepeatingTest,
    ::testing::Values(
        TestCase{"abcabcbb", 3},
        TestCase{"bbbbb", 1},
        TestCase{"pwwkew", 3}));

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
