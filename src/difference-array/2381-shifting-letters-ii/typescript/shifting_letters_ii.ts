export function shiftingLetters(s: string, shifts: number[][]): string {
  const n: number = s.length;
  const diff: number[] = new Array(n).fill(0);
  for (const shift of shifts) {
    if (shift[2] === 0) {
      // Backward direction
      diff[shift[0]] -= 1;
      if (shift[1] + 1 < n) {
        diff[shift[1] + 1] += 1;
      }
    } else {
      // Forward direction
      diff[shift[0]] += 1;
      if (shift[1] + 1 < n) {
        diff[shift[1] + 1] -= 1;
      }
    }
  }
  let num_of_shifts = 0;
  const results = s.split("").map((char, index) => {
    num_of_shifts = (num_of_shifts + diff[index]) % 26;
    if (num_of_shifts < 0) num_of_shifts += 26;
    const newCharCode =
      ((char.charCodeAt(0) - "a".charCodeAt(0) + num_of_shifts) % 26) +
      "a".charCodeAt(0);
    return newCharCode;
  });
  return String.fromCharCode(...results);
}
