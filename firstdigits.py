import collections
import csv
from pathlib import Path

SIZES_FILE = Path("/Users/bakrbouhaya/Downloads/Project2/sizes_bytes.txt")


def first_nonzero_digit(x: float):
    if x == 0:
        return None
    s = f"{abs(x):g}"
    for ch in s:
        if ch in "123456789":
            return int(ch)
    return None


def main():
    sizes = []
    with open(SIZES_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                size = float(line)
            except ValueError:
                continue
            sizes.append(size)

    first_digits = []
    for size in sizes:
        d = first_nonzero_digit(size)
        if d is not None:
            first_digits.append(d)

    out_path = Path("/Users/bakrbouhaya/Downloads/Project2/firstdigits.csv")
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["first_digit"])
        for d in first_digits:
            writer.writerow([d])

    counts = collections.Counter(first_digits)
    print("First-digit frequency table:\n")
    print("Digit\tCount")
    for d in range(1, 10):
        print(f"{d}\t{counts.get(d, 0)}")


if __name__ == "__main__":
    main()
