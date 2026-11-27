"""Inspect binary STL meshes before opening a slicer. Python 3, standard library only."""
import argparse
import math
from pathlib import Path
import struct
import sys

PARTS = Path(__file__).resolve().parents[1] / "mountable items - 3D CAD"
FACET = struct.Struct("<12fH")  # normal, three vertices, attribute count


def inspect_mesh(path):
    """Return the triangle count and X/Y/Z spans in the STL's native units."""
    with path.open("rb") as stream:
        header = stream.read(84)
        if len(header) != 84:
            raise ValueError("no complete binary STL header")
        count = struct.unpack_from("<I", header, 80)[0]
        if not count or path.stat().st_size != 84 + count * FACET.size:
            raise ValueError("empty mesh or byte length inconsistent with binary STL header")
        low, high = [math.inf] * 3, [-math.inf] * 3
        for _ in range(count):
            data = stream.read(FACET.size)
            if len(data) != FACET.size:
                raise ValueError("truncated triangle")
            coords = FACET.unpack(data)[3:12]
            for i, val in enumerate(coords):
                if not math.isfinite(val):
                    raise ValueError("non-finite vertex coordinate")
                axis = i % 3
                low[axis] = min(low[axis], val)
                high[axis] = max(high[axis], val)
        return count, tuple(b - a for a, b in zip(low, high))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path,
                        help="binary STL files (default: the repository's six parts)")
    paths = parser.parse_args().paths or sorted(PARTS.glob("*.stl"))
    if not paths:
        parser.exit(1, "No STL parts found. Supply a path or run from a full checkout.\n")
    print("triangles   span X   span Y   span Z   part   [native STL units]")
    failed = False
    for path in paths:
        try:
            count, (x, y, z) = inspect_mesh(path)
        except (OSError, ValueError) as err:
            print(f"{path}: {err}", file=sys.stderr)
            failed = True
        else:
            print(f"{count:9d} {x:8.2f} {y:8.2f} {z:8.2f}   {path.name}")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
