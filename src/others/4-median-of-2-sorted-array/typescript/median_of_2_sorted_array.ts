export function findMedianSortedArrays_mergeSort(
  nums1: number[],
  nums2: number[],
): number {
  const m = nums1.length,
    n = nums2.length;
  let p1 = 0,
    p2 = 0;

  const getMin = function (): number {
    if (p1 < m && p2 < n) {
      return nums1[p1] < nums2[p2] ? nums1[p1++] : nums2[p2++];
    } else if (p1 < m) {
      return nums1[p1++];
    } else if (p2 < n) {
      return nums2[p2++];
    }
    return -1;
  };

  if ((m + n) % 2 === 0) {
    for (let i = 0; i < (m + n) / 2 - 1; ++i) {
      getMin();
    }
    return (getMin() + getMin()) / 2;
  } else {
    for (let i = 0; i < Math.floor((m + n) / 2); ++i) {
      getMin();
    }
    return getMin();
  }
}

export function findMedianSortedArrays_binarySearch(
  nums1: number[],
  nums2: number[],
): number {
  if (nums1.length > nums2.length) {
    const temp = nums1;
    nums1 = nums2;
    nums2 = temp;
  }
  const m = nums1.length,
    n = nums2.length;
  let left = 0,
    right = m;
  while (left <= right) {
    const partitionA = Math.floor((left + right) / 2);
    const partitionB = Math.floor((m + n + 1) / 2 - partitionA);
    const maxLeftA =
      partitionA == 0 ? Number.MIN_SAFE_INTEGER : nums1[partitionA - 1];
    const minRightA =
      partitionA == m ? Number.MAX_SAFE_INTEGER : nums1[partitionA];
    const maxLeftB =
      partitionB == 0 ? Number.MIN_SAFE_INTEGER : nums2[partitionB - 1];
    const minRightB =
      partitionB == n ? Number.MAX_SAFE_INTEGER : nums2[partitionB];
    if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
      if ((m + n) % 2 == 0) {
        return (
          (Math.max(maxLeftA, maxLeftB) + Math.min(minRightA, minRightB)) / 2.0
        );
      } else {
        return Math.max(maxLeftA, maxLeftB);
      }
    } else if (maxLeftA > minRightB) {
      right = partitionA - 1;
    } else {
      left = partitionA + 1;
    }
  }
  return 0;
}
