"""news-image-20261122: write the shipped front page to /output/entry.png.

The entry is the image itself: a dense broadsheet front page summing up
Sunday 22 November 2026 in 36 numbered stories (lead: Iran's Saturday-night
strikes on two US bases in Bahrain and the widening Gulf war) plus a labelled
world-map panel. This program draws nothing and touches no network; it copies
the shipped PNG byte for byte, so every run produces identical output.
"""

import os
import shutil
import struct
import sys
from pathlib import Path

SHIPPED = "entry.png"
OUTPUT = "entry.png"
MAX_BYTES = 1048576
WANT_WIDTH = 1024
WANT_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_png_size(data: bytes) -> tuple[int, int]:
    """Return (width, height) from the PNG IHDR chunk, stdlib only."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("not a PNG file: missing IHDR chunk")
    return struct.unpack(">II", data[16:24])


def shipped_path() -> Path:
    here = Path(__file__).resolve().parent / SHIPPED
    if here.is_file():
        return here
    alt = Path.cwd() / SHIPPED
    if alt.is_file():
        return alt
    raise FileNotFoundError(f"shipped image not found: {here}")


def output_dir() -> Path:
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(override) if override else Path("/output")


def main() -> int:
    src = shipped_path()
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / OUTPUT
    shutil.copyfile(src, out)
    os.chmod(out, 0o644)
    data = out.read_bytes()
    if data != src.read_bytes():
        raise ValueError("output differs from the shipped image")
    if data[:8] != PNG_MAGIC:
        raise ValueError("output is not a PNG file")
    if len(data) > MAX_BYTES:
        raise ValueError(f"output too large: {len(data)} bytes")
    width, height = read_png_size(data)
    if (width, height) != (WANT_WIDTH, WANT_HEIGHT):
        raise ValueError(f"unexpected dimensions: {width}x{height}")
    print(f"wrote {out} ({len(data)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
