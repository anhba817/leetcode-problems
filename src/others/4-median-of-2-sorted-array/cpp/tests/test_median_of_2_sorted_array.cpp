#include "median_of_2_sorted_array.hpp"

#include <gtest/gtest.h>

#include <string>
#include <vector>

namespace
{
    struct TestCase
    {
        vector<int> nums1;
        vector<int> nums2;
        float expected;
    };
} // namespace

class MedianOf2SortedArraysMergeSortTest : public ::testing::TestWithParam<TestCase>
{
};

TEST_P(MedianOf2SortedArraysMergeSortTest, ProducesExpectedString)
{
    const TestCase &test = GetParam();
    Solutions s = Solutions();
    EXPECT_EQ(test.expected, s.findMedianSortedArrays_mergeSort(test.nums1, test.nums2));
}

INSTANTIATE_TEST_SUITE_P(
    Examples,
    MedianOf2SortedArraysMergeSortTest,
    ::testing::Values(
        TestCase{{1, 2}, {3}, 2.0},
        TestCase{{1, 2}, {3, 4}, 2.5}));

class MedianOf2SortedArraysBinarySearchTest : public ::testing::TestWithParam<TestCase>
{
};

TEST_P(MedianOf2SortedArraysBinarySearchTest, ProducesExpectedString)
{
    const TestCase &test = GetParam();
    Solutions s = Solutions();
    EXPECT_EQ(test.expected, s.findMedianSortedArrays_binarySearch(test.nums1, test.nums2));
}

INSTANTIATE_TEST_SUITE_P(
    Examples,
    MedianOf2SortedArraysBinarySearchTest,
    ::testing::Values(
        TestCase{{1, 2}, {3}, 2.0},
        TestCase{{1, 2}, {3, 4}, 2.5}));

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
