"""Compare synthetic edge profiles. Run with Python 3; no camera or packages."""

from statistics import pvariance


def score(row):
    """Variance of the interior 1-D second differences, excluding the border."""
    if len(row) < 4:
        raise ValueError("Use at least four samples for two differences.")
    differences = [right - 2 * mid + left
                   for left, mid, right in zip(row, row[1:], row[2:])]
    return pvariance(differences)


if __name__ == "__main__":
    profiles = {
        "flat": [50] * 8,
        "soft edge": [0, 0, 15, 40, 60, 85, 100, 100],
        "sharp edge": [0, 0, 0, 0, 100, 100, 100, 100],
        "alternating pattern": [0, 100] * 4,
    }
    for label, row in profiles.items():
        print(f"{label:20} {score(row):8.2f}")
