#pragma once

#include "disjoint_sets/disjoint_sets.hpp"

#include <vector>

class ConnectedComponentsInLCMGraph
{
public:
  ConnectedComponentsInLCMGraph(std::vector<int> nums, int threshold);

  int countComponents();

private:
  void setup();

  std::vector<int> _nums;
  int _threshold;
  DisjointSets _disjointSets;
  std::vector<int> _singleComponents;
  std::vector<int> _belowThresholdNums;
};
