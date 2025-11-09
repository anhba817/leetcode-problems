#include "shifting_letters_ii.hpp"

#include <gtest/gtest.h>

#include <string>
#include <vector>

namespace
{
struct TestCase
{
  std::string s;
  std::vector<std::vector<int>> shifts;
  std::string expected;
};
} // namespace

class ShiftingLettersTest : public ::testing::TestWithParam<TestCase>
{};

TEST_P(ShiftingLettersTest, ProducesExpectedString)
{
  const TestCase &test = GetParam();
  EXPECT_EQ(test.expected, shifting_letters(test.s, test.shifts));
}

INSTANTIATE_TEST_SUITE_P(
    Examples,
    ShiftingLettersTest,
    ::testing::Values(
        TestCase{"abc",
                 {{0, 1, 0},
                  {1, 2, 1},
                  {0, 2, 1}},
                 "ace"},
        TestCase{"dztz",
                 {{0, 0, 0},
                  {1, 1, 1}},
                 "catz"}));

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
