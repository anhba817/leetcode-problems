import {
  findMedianSortedArrays_mergeSort,
  findMedianSortedArrays_binarySearch,
} from "./median_of_2_sorted_array";

const testCases = [
  {
    name: "Example case 1",
    nums1: [1, 3],
    nums2: [2],
    expected: 2,
  },
  {
    name: "Example case 2",
    nums1: [1, 2],
    nums2: [3, 4],
    expected: 2.5,
  },
];

const approaches = [
  {
    label: "Median of 2 sorted array approach 1 - Merge Sort",
    fn: findMedianSortedArrays_mergeSort,
  },
  {
    label: "Median of 2 sorted array approach 2 - Binary Search",
    fn: findMedianSortedArrays_binarySearch,
  },
];

describe.each(approaches)("$label", ({ fn }) => {
  test.each(testCases)("$name", ({ nums1, nums2, expected }) => {
    const result = fn(nums1, nums2);
    expect(result).toEqual(expected);
  });
});
