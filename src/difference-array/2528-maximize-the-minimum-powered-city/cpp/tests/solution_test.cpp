#include "solution.hpp"

#include <gtest/gtest.h>

#include <vector>

namespace
{
struct TestCase
{
  std::vector<int> stations;
  int radius;
  long long extra;
  long long expected;
};
} // namespace

class MaxPowerTest : public ::testing::TestWithParam<TestCase>
{};

TEST_P(MaxPowerTest, ComputesExpectedPower)
{
  const TestCase &test = GetParam();
  EXPECT_EQ(test.expected, maxPower(test.stations, test.radius, test.extra));
}

INSTANTIATE_TEST_SUITE_P(
    Examples,
    MaxPowerTest,
    ::testing::Values(
        TestCase{{1, 2, 4, 5, 0}, 1, 2, 5},
        TestCase{{4, 4, 4, 4}, 0, 3, 4},
        TestCase{{0, 0, 0}, 1, 6, 6},
        TestCase{{1, 0, 0, 0}, 1, 4, 2},
        TestCase{{1, 2, 3}, 2, 1, 7}));

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
