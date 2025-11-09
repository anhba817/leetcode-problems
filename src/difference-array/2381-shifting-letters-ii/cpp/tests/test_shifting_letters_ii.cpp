#include "shifting_letters_ii.hpp"

#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>

namespace
{
  struct TestCase
  {
    std::string s;
    std::vector<std::vector<int>> shifts;
    std::string expected;
  };
}

int main()
{
  const std::vector<TestCase> cases = {
      {"abc", {
                  {0, 1, 0},
                  {1, 2, 1},
                  {0, 2, 1},
              },
       "ace"},
      {"dztz", {
                   {0, 0, 0},
                   {1, 1, 1},
               },
       "catz"}};

  for (const auto &test : cases)
  {
    const std::string actual = shifting_letters(test.s, test.shifts);
    if (actual != test.expected)
    {
      std::cerr << "Expected " << test.expected << " but got " << actual << "\n";
      return EXIT_FAILURE;
    }
  }

  std::cout << "All tests passed\n";
  return EXIT_SUCCESS;
}
