from .median_of_2_sorted_array import (
    findMedianSortedArrays_mergeSort,
    findMedianSortedArrays_binarySearch,
)


def test_median_of_2_sorted_array_example_case_1_merge_sort():
    # Input: nums1 = [1,3], nums2 = [2]
    # Output: 2.00000
    # Explanation: merged array = [1,2,3] and median is 2.
    result = findMedianSortedArrays_mergeSort([1, 3], [2])
    assert result == 2


def test_median_of_2_sorted_array_example_case_2_merge_sort():
    # Input: nums1 = [1,2], nums2 = [3,4]
    # Output: 2.50000
    # Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    result = findMedianSortedArrays_mergeSort([1, 2], [3, 4])
    assert result == 2.5


def test_median_of_2_sorted_array_example_case_1_binary_search():
    # Input: nums1 = [1,3], nums2 = [2]
    # Output: 2.00000
    # Explanation: merged array = [1,2,3] and median is 2.
    result = findMedianSortedArrays_binarySearch([1, 3], [2])
    assert result == 2


def test_median_of_2_sorted_array_example_case_2_binary_search():
    # Input: nums1 = [1,2], nums2 = [3,4]
    # Output: 2.50000
    # Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    result = findMedianSortedArrays_binarySearch([1, 2], [3, 4])
    assert result == 2.5
