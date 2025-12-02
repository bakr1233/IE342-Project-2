import csv
import math
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path("/Users/bakrbouhaya/Downloads/Project2")
FIRST_DIGITS_CSV = BASE_DIR / "firstdigits.csv"


def load_first_digits(path: Path):
    digits = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                d = int(row["first_digit"])
            except (KeyError, ValueError):
                continue
            if 1 <= d <= 9:
                digits.append(d)
    return digits


def empirical_distribution(digits):
    n = len(digits)
    counts = Counter(digits)
    probs = {d: counts.get(d, 0) / n for d in range(1, 10)}
    return counts, probs


def benford_distribution():
    probs = {d: math.log10(1 + 1 / d) for d in range(1, 10)}
    return probs


def plot_empirical(probs_emp):
    digits = list(range(1, 10))
    values = [probs_emp[d] for d in digits]

    plt.figure(figsize=(6, 4))
    plt.bar(digits, values, color="skyblue")
    plt.xlabel("First digit")
    plt.ylabel("Probability")
    plt.title("Empirical First-Digit Distribution")
    plt.xticks(digits)
    plt.tight_layout()
    plt.savefig(BASE_DIR / "empirical_first_digits.png", dpi=200)
    plt.close()


def plot_benford(probs_benford):
    digits = list(range(1, 10))
    values = [probs_benford[d] for d in digits]

    plt.figure(figsize=(6, 4))
    plt.bar(digits, values, color="salmon")
    plt.xlabel("First digit")
    plt.ylabel("Probability")
    plt.title("Benford First-Digit Distribution")
    plt.xticks(digits)
    plt.tight_layout()
    plt.savefig(BASE_DIR / "benford_first_digits.png", dpi=200)
    plt.close()


def plot_grouped(probs_emp, probs_benford):
    digits = list(range(1, 10))
    emp = [probs_emp[d] for d in digits]
    ben = [probs_benford[d] for d in digits]

    x = range(len(digits))
    width = 0.4

    plt.figure(figsize=(8, 4))
    plt.bar([i - width / 2 for i in x], emp, width=width, label="Empirical", color="skyblue")
    plt.bar([i + width / 2 for i in x], ben, width=width, label="Benford", color="salmon")
    plt.xlabel("First digit")
    plt.ylabel("Probability")
    plt.title("Empirical vs Benford First-Digit Distribution")
    plt.xticks(list(x), digits)
    plt.legend()
    plt.tight_layout()
    plt.savefig(BASE_DIR / "empirical_vs_benford.png", dpi=200)
    plt.close()


def main():
    digits = load_first_digits(FIRST_DIGITS_CSV)
    if not digits:
        print(f"No digits loaded from {FIRST_DIGITS_CSV}. Make sure firstdigits.py has been run.")
        return

    counts_emp, probs_emp = empirical_distribution(digits)
    probs_benford = benford_distribution()

    print("Empirical first-digit counts:")
    for d in range(1, 10):
        print(f"Digit {d}: count = {counts_emp.get(d, 0)}, "
              f"prob = {probs_emp[d]:.4f}, Benford = {probs_benford[d]:.4f}")

    plot_empirical(probs_emp)
    plot_benford(probs_benford)
    plot_grouped(probs_emp, probs_benford)

    print("\nSaved plots:")
    print(f"- {BASE_DIR / 'empirical_first_digits.png'}")
    print(f"- {BASE_DIR / 'benford_first_digits.png'}")
    print(f"- {BASE_DIR / 'empirical_vs_benford.png'}")


if __name__ == "__main__":
    main()


