def findMedianSortedArrays_mergeSort(
    nums1: list[int],
    nums2: list[int],
) -> int:
    """Return the median by merging until the middle point.

    The function simulates the merge step from merge sort with two pointers and
    advances only as far as needed to reach the median. This avoids materializing
    the merged array while still leveraging the fact that both lists are sorted.
    """
    m = len(nums1)
    n = len(nums2)
    p1 = 0
    p2 = 0

    # Get the smaller value between nums1[p1] and nums2[p2].
    def get_min():
        nonlocal p1, p2
        if p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
        elif p2 == n:
            ans = nums1[p1]
            p1 += 1
        else:
            ans = nums2[p2]
            p2 += 1
        return ans

    if (m + n) % 2 == 0:
        # Skip to just before the two middle numbers, then pull both and average.
        for _ in range((m + n) // 2 - 1):
            _ = get_min()
        return (get_min() + get_min()) / 2
    else:
        # Skip to the middle element and return it directly.
        for _ in range((m + n) // 2):
            _ = get_min()
        return get_min()


def findMedianSortedArrays_binarySearch(
    nums1: list[int],
    nums2: list[int],
) -> int:
    """Return the median using binary search on the partition index.

    The smaller array is partitioned such that the left halves of both arrays
    contain exactly half of the combined elements. The search moves the
    partition until every value on the left side is less than or equal to every
    value on the right side, at which point the median is known in constant
    time.
    """
    if len(nums1) > len(nums2):
        return findMedianSortedArrays_binarySearch(nums2, nums1)

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        partitionA = (left + right) // 2
        partitionB = (m + n + 1) // 2 - partitionA
        # Sentinel values allow us to treat edges as +/- infinity and keep the
        # comparisons uniform.
        maxLeftA = float("-inf") if partitionA == 0 else nums1[partitionA - 1]
        minRightA = float("inf") if partitionA == m else nums1[partitionA]
        maxLeftB = float("-inf") if partitionB == 0 else nums2[partitionB - 1]
        minRightB = float("inf") if partitionB == n else nums2[partitionB]
        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if (m + n) % 2 == 0:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                return max(maxLeftA, maxLeftB)
        elif maxLeftA > minRightB:
            right = partitionA - 1
        else:
            left = partitionA + 1
