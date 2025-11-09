#include "lcm_connected_components.hpp"

#include <gtest/gtest.h>

#include <vector>

namespace
{
struct TestCase
{
  std::vector<int> nums;
  int threshold;
  int expected;
};
} // namespace

class ConnectedComponentsInLCMGraphTest : public ::testing::TestWithParam<TestCase>
{};

TEST_P(ConnectedComponentsInLCMGraphTest, CountsComponentsCorrectly)
{
  const TestCase &test = GetParam();
  ConnectedComponentsInLCMGraph graph(test.nums, test.threshold);
  EXPECT_EQ(test.expected, graph.countComponents());
}

INSTANTIATE_TEST_SUITE_P(
    Examples,
    ConnectedComponentsInLCMGraphTest,
    ::testing::Values(
        TestCase{{2, 4, 8, 3, 9}, 5, 4},
        TestCase{{2, 4, 8, 3, 9, 12}, 10, 2}));

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
