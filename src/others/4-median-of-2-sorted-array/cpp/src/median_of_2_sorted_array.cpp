#include "median_of_2_sorted_array.hpp"

#include <climits>

using namespace std;

// Get the smaller value between nums1[p1] and nums2[p2] and move the
// pointer forward.
Solutions::Solutions() : p1(0), p2(0)
{
}
int Solutions::getMin(const vector<int> &nums1, const vector<int> &nums2)
{
    if (p1 < nums1.size() && p2 < nums2.size())
    {
        return nums1[p1] < nums2[p2] ? nums1[p1++] : nums2[p2++];
    }
    else if (p1 < nums1.size())
    {
        return nums1[p1++];
    }
    else if (p2 < nums2.size())
    {
        return nums2[p2++];
    }
    return -1;
}

float Solutions::findMedianSortedArrays_mergeSort(const vector<int> &nums1, const vector<int> &nums2)
{
    int m = int(nums1.size()), n = int(nums2.size());

    if ((m + n) % 2 == 0)
    {
        for (int i = 0; i < (m + n) / 2 - 1; ++i)
        {
            int _ = getMin(nums1, nums2);
        }
        int a = getMin(nums1, nums2);
        int b = getMin(nums1, nums2);
        return (float)(a + b) / 2;
    }
    else
    {
        for (int i = 0; i < (m + n) / 2; ++i)
        {
            int _ = getMin(nums1, nums2);
        }
        return getMin(nums1, nums2);
    }

    return -1;
}

float Solutions::findMedianSortedArrays_binarySearch(const vector<int> &nums1, const vector<int> &nums2)
{
    if (nums1.size() > nums2.size())
    {
        return findMedianSortedArrays_binarySearch(nums2, nums1);
    }

    int m = nums1.size(), n = nums2.size();
    int left = 0, right = m;

    while (left <= right)
    {
        int partitionA = (left + right) / 2;
        int partitionB = (m + n + 1) / 2 - partitionA;

        int maxLeftA = (partitionA == 0) ? INT_MIN : nums1[partitionA - 1];
        int minRightA = (partitionA == m) ? INT_MAX : nums1[partitionA];
        int maxLeftB = (partitionB == 0) ? INT_MIN : nums2[partitionB - 1];
        int minRightB = (partitionB == n) ? INT_MAX : nums2[partitionB];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA)
        {
            if ((m + n) % 2 == 0)
            {
                return (max(maxLeftA, maxLeftB) +
                        min(minRightA, minRightB)) /
                       2.0;
            }
            else
            {
                return max(maxLeftA, maxLeftB);
            }
        }
        else if (maxLeftA > minRightB)
        {
            right = partitionA - 1;
        }
        else
        {
            left = partitionA + 1;
        }
    }

    return 0.0;
}
