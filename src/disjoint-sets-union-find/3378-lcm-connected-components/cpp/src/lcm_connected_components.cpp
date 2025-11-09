#include "lcm_connected_components.hpp"

#include <unordered_set>

ConnectedComponentsInLCMGraph::ConnectedComponentsInLCMGraph(
    std::vector<int> nums, int threshold)
    : _nums(std::move(nums)),
      _threshold(threshold),
      _disjointSets(threshold)
{
  setup();
}

void ConnectedComponentsInLCMGraph::setup()
{
  for (int num : _nums)
  {
    if (num > _threshold)
    {
      _singleComponents.push_back(num);
      continue;
    }

    _belowThresholdNums.push_back(num);
    long long multiple = num;
    while (multiple <= _threshold)
    {
      _disjointSets.unite(num, static_cast<int>(multiple));
      multiple += num;
    }
  }
}

int ConnectedComponentsInLCMGraph::countComponents()
{
  std::unordered_set<int> roots;
  for (int num : _belowThresholdNums)
  {
    roots.insert(_disjointSets.find(num));
  }
  return static_cast<int>(roots.size() + _singleComponents.size());
}
