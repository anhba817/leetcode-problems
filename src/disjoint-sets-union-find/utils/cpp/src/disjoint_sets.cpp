#include "disjoint_sets/disjoint_sets.hpp"

#include <algorithm>
#include <numeric>

DisjointSets::DisjointSets(int n)
    : _parent(std::max(0, n) + 1), _size(std::max(0, n) + 1, 1)
{
  std::iota(_parent.begin(), _parent.end(), 0);
}

int DisjointSets::find(int x)
{
  if (_parent[x] == x)
  {
    return x;
  }
  _parent[x] = find(_parent[x]);
  return _parent[x];
}

void DisjointSets::unite(int a, int b)
{
  int rootA = find(a);
  int rootB = find(b);
  if (rootA == rootB)
  {
    return;
  }
  if (_size[rootA] < _size[rootB])
  {
    _parent[rootA] = rootB;
    _size[rootB] += _size[rootA];
  }
  else
  {
    _parent[rootB] = rootA;
    _size[rootA] += _size[rootB];
  }
}
