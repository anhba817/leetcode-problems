#include "solution.hpp"

#include <cstdlib>
#include <iostream>
#include <vector>

namespace {
struct TestCase {
  std::vector<int> stations;
  int radius;
  long long extra;
  long long expected;
};
}

int main() {
  const std::vector<TestCase> cases = {
      {{1, 2, 4, 5, 0}, 1, 2, 5},
      {{4, 4, 4}, 1, 0, 8},
      {{0, 0, 0}, 1, 6, 6},
      {{1, 0, 0, 0}, 1, 4, 2},
      {{1, 2, 3}, 2, 1, 7},
  };

  for (const auto& test : cases) {
    const long long actual = maxPower(test.stations, test.radius, test.extra);
    if (actual != test.expected) {
      std::cerr << "Expected " << test.expected << " but got " << actual << "\n";
      return EXIT_FAILURE;
    }
  }

  std::cout << "All tests passed\n";
  return EXIT_SUCCESS;
}
