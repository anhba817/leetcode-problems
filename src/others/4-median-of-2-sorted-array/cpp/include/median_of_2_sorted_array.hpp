#pragma once

#include <vector>

using namespace std;

class Solutions
{
public:
    int p1, p2 ;
    Solutions();
    int getMin(const vector<int> &nums1, const vector<int> &nums2);
    float findMedianSortedArrays_mergeSort(const vector<int> &nums1, const vector<int> &nums2);
    float findMedianSortedArrays_binarySearch(const vector<int> &nums1, const vector<int> &nums2);
};
