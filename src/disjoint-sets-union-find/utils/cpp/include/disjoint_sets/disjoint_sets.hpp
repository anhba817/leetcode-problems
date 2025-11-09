#pragma once

#include <vector>

class DisjointSets
{
public:
  explicit DisjointSets(int n);

  int find(int x);
  void unite(int a, int b);

private:
  std::vector<int> _parent;
  std::vector<int> _size;
};
