"""Greedy + binary-search solution for LeetCode 2528 using a difference array."""

from __future__ import annotations

from typing import List


def max_power(stations: List[int], r: int, k: int) -> int:
    """Binary search the best minimum power while simulating coverage with a diff array."""

    n = len(stations)
    if n == 0:
        return 0

    # Precompute the base contribution for each city using a difference array.
    diff = [0] * (n + 1)
    for idx, power in enumerate(stations):
        left = max(0, idx - r)
        right = min(n, idx + r + 1)
        diff[left] += power
        diff[right] -= power

    def can(target: int) -> bool:
        """Return True if we can raise every city to at least `target` power."""
        remaining = k
        running = 0
        local_diff = diff.copy()  # mutable prefix contributions during this feasibility check

        for city in range(n):
            running += local_diff[city]
            if running < target:
                need = target - running
                if need > remaining:
                    return False
                remaining -= need
                running += need
                window_end = min(n, city + 2 * r + 1)  # extra stations stop affecting after this index
                local_diff[window_end] -= need
        return True

    lo, hi = 0, sum(stations) + k
    best = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if can(mid):
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return best
