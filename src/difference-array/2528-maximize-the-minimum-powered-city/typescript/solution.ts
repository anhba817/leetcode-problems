/**
 * Binary-searches the best achievable minimum power after adding at most k stations.
 * Builds a difference array to quickly simulate the circular coverage window for each city.
 */
export function maxPower(stations: number[], r: number, k: number): number {
  const n: number = stations.length;
  const cnt: number[] = new Array(n + 1).fill(0); // coverage difference array

  // Build the base difference array representing current window coverage
  for (let i = 0; i < n; i++) {
    const left: number = Math.max(0, i - r);
    const right: number = Math.min(n, i + r + 1);
    cnt[left] += stations[i];
    cnt[right] -= stations[i];
  }

  const check = (val: number): boolean => {
    // diff keeps the mutable prefix sums as we inject new stations
    const diff: number[] = [...cnt];
    let sum: number = 0;
    let remaining: number = k;

    for (let i = 0; i < n; i++) {
      sum += diff[i];
      if (sum < val) {
        const add: number = val - sum;
        if (remaining < add) {
          return false;
        }
        remaining -= add;
        const end: number = Math.min(n, i + 2 * r + 1); // effect of added stations ends here
        diff[end] -= add;
        sum += add;
      }
    }
    return true;
  };

  let lo: number = Math.min(...stations);
  let hi: number = stations.reduce((a, b) => a + b, 0) + k;
  let res: number = 0;

  while (lo <= hi) {
    const mid: number = Math.floor(lo + (hi - lo) / 2);
    if (check(mid)) {
      res = mid;
      lo = mid + 1;
    } else {
      hi = mid - 1;
    }
  }
  return res;
}
