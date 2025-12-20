#include "solution.hpp"

#include <algorithm>
#include <numeric>
#include <vector>

/**
 * Finds the largest minimum power achievable after adding at most k new stations.
 * Binary searches the answer, using a difference array to simulate coverage additions.
 */
long long maxPower(const std::vector<int>& stations, int r, long long k)
{
  int n = stations.size();
  std::vector<long long> cnt(n + 1); // base difference array for window coverage
  for (int i = 0; i < n; i++)
  {
    int left = std::max(0, i - r);
    int right = std::min(n, i + r + 1);
    cnt[left] += stations[i];
    cnt[right] -= stations[i];
  }

  auto check = [&](long long val) -> bool
  {
    std::vector<long long> diff = cnt; // mutable difference array while we add power
    long long sum = 0;
    long long remaining = k;

    for (int i = 0; i < n; i++)
    {
      sum += diff[i];
      if (sum < val)
      {
        long long add = val - sum;
        if (remaining < add)
        {
          return false;
        }
        remaining -= add;
        int end = std::min(n, i + 2 * r + 1); // new station affects cities up to this index
        diff[end] -= add;
        sum += add;
      }
    }
    return true;
  };

  long long lo = std::ranges::min(stations);
  long long hi = accumulate(stations.begin(), stations.end(), 0LL) + k;
  long long res = 0;
  while (lo <= hi)
  {
    long long mid = lo + (hi - lo) / 2;
    if (check(mid))
    {
      res = mid;
      lo = mid + 1;
    }
    else
    {
      hi = mid - 1;
    }
  }
  return res;
}
