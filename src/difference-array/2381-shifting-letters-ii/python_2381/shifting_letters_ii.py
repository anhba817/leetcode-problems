from typing import List


def shifting_letters(s: str, shifts: List[List[int]]) -> str:
    n = len(s)
    diff = [0] * n
    for shift in shifts:
        if shift[2] == 0:
            # Backward direction
            diff[shift[0]] -= 1
            if shift[1] + 1 < n:
                diff[shift[1] + 1] += 1
        else:
            # Forward direction
            diff[shift[0]] += 1
            if shift[1] + 1 < n:
                diff[shift[1] + 1] -= 1

    num_of_shifts = 0
    results = list(s)
    for i in range(n):
        num_of_shifts = (num_of_shifts + diff[i]) % 26
        if num_of_shifts < 0:
            num_of_shifts += 26
        shifted_char = chr((ord(s[i]) - ord("a") + num_of_shifts) % 26 + ord("a"))
        results[i] = shifted_char
    return "".join(results)
