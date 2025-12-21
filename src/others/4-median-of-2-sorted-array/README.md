# Problem
## Description
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

## Examples
### Example 1:
> **Input:** `nums1 = [1,3], nums2 = [2]`  
**Output:** `2.00000`  
**Explanation:** `merged array = [1,2,3] and median is 2.`

### Example 2:**
> **Input:** `nums1 = [1,2], nums2 = [3,4]`  
**Output:** `2.50000`  
**Explanation:** `merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.`

## Constraints
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

# Solutions
## Approach 1: Merge Sort
### Algorithm:
1. Get the total size of two arrays `m + n`
    - If `m + n` is odd, we are looking for the `(m + n) / 2`-th element.
    - If `m + n` is even, we are looking for the average of the `(m + n) / 2`-th and the `(m + n) / 2 + 1`-th elements.
2. Set two pointers `p1` and `p2` at the beginning of arrays `nums1` and `nums2`.
3. If both `p1` and `p2` are in bounds of the arrays, compare the values at `p1` and `p2`:
    - If `nums1[p1]` is smaller than `nums2[p2]`, we move `p1` one place to the right.
    - Otherwise, we move `p2` one place to the right.

    If `p1` is outside `nums1`, just move `p2` one place to the right.  
    If `p2` is outside `nums2`, just move `p1` one place to the right.
4. Get the target elements and calculate the median:
    - If `m + n` is odd, repeat step 3 by `(m + n + 1) / 2` times and return the element from the last step.
    - If `m + n` is even, repeat step 3 by `(m + n) / 2 + 1` times and return the average of the elements from the last two steps.

### Complexity Analysis:
Let m be the size of array nums1 and n be the size of array nums2.
- Time complexity: `O(m+n)`
    - We get the smallest element by comparing two values at `p1` and `p2`, it takes `O(1)` to compare two elements and move the corresponding pointer to the right.
    - We need to traverse half of the arrays before reaching the median element(s).
    - To sum up, the time complexity is `O(m+n)`.
- Space complexity: `O(1)`
    - We only need to maintain two pointers `p1` and `p2`.

## Approach 2: Binary search
### Algorithm:
1. Assuming `nums1` to be the smaller array (If `nums2` is smaller, we can swap them). Let `m`, `n` represent the size of `nums1` and `nums2`, respectively.
2. Define the search space for the partitioning index `partitionA` by setting boundaries as `left = 0` and `right = m`.
3. While `left <= right` holds, do the following.
4. Compute the partition index of `nums1` as `partitionA = (left + right) / 2`. Consequently, the partition index of `nums2` is `(m + n + 1) / 2 - partitionA`.
5. Obtain the edge elements:
    - Determine the maximum value of the section `A_left` as `maxLeftA = nums1[partitionA - 1]`. If `partitionA - 1 < 0`, set it as `maxLeftA = float(-inf)`.
    - Determine the minimum value of the section `A_right` as `minRightA = nums1[partitionA]`. If `partitionA >= m`, set it as `minRightA = float(inf)`.
    - Determine the maximum value of the section `B_left` as `maxLeftB = nums2[partitionB - 1]`. If `partitionB - 1 < 0`, set it as `maxLeftB = float(-inf)`.
    - Determine the maximum value of the section `B_right` as `minRightB = nums2[partitionB]`. If `partitionB >= n`, set it as `minRightB = float(inf)`.
6. Compare and recalculate: Compare `maxLeftA` with `minRightB` and `maxLeftB` with `minRightA`.
    - If `maxLeftA > minRightB`, it means the `maxLeftA` is too large to be in the smaller half, so we update `right = partitionA - 1` to move to the left half of the search space.
    - If `maxLeftB > minRightA`, it means that we are too far on the left side for `partitionA` and we need to go to the right half of the search space by updating `left = partitionA + 1`.
    
    Repeat step 4.
7. When both `maxLeftA <= minRightB` and `maxLeftB <= minRightA` are true:
    - If `(m + n) % 2 = 0`, the median value is the average of the maximum value of the smaller half and the minimum value of the larger half, given by `answer = (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2`.
    - Otherwise, the median value is the maximum value of the smaller half, given by `answer = max(maxLeftA, maxLeftB)`.

### Complexity Analysis:
Let `m` be the size of array `nums1` and `n` be the size of array `nums2`.
- Time complexity: `O(log(min(m,n)))`  
    We perform a binary search over the smaller array of size `min(m,n)`.
- Space complexity: `O(1)`  
    The algorithm only requires a constant amount of additional space to store and update a few parameters during the binary search.
