#include "dijkstra.hpp"

#include <gtest/gtest.h>

#include <vector>

TEST(DijkstraTest, ExampleCase1)
{
  const int n = 5;
  const int src = 0;

  // edge list format: {u, v, weight}
  std::vector<std::vector<int>> edges = {
      {0, 1, 4},
      {0, 2, 8},
      {1, 4, 6},
      {2, 3, 2},
      {3, 4, 10},
  };

  const std::vector<int> expected = {0, 4, 8, 10, 10};
  EXPECT_EQ(expected, dijkstra(n, edges, src));
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
