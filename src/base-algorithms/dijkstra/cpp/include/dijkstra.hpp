#pragma once

#include <vector>

// Returns the shortest distance from src to every vertex in an undirected
// weighted graph described by edge list {u, v, weight}.
std::vector<int> dijkstra(int n, std::vector<std::vector<int>> &edges, int src);
