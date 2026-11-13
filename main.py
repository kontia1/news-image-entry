"""Copy the prepared entry image into the harness output directory."""
from pathlib import Path
import os
import shutil

SRC: Path = Path("entry.png")
# Cap is 1 MiB (1024 * 1024 bytes) by competition rule.
MAX_BYTES: int = 1024 * 1024


def main() -> int:
    """Copy entry.png byte-for-byte into the harness output directory."""
    size: int = SRC.stat().st_size
    if size >= MAX_BYTES:
        print(f"refused: entry.png is {size} bytes, limit is {MAX_BYTES}")
        return 1
    dest_dir: Path = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest: Path = dest_dir / "entry.png"
    shutil.copyfile(SRC, dest)
    print(f"copied {size} bytes -> {dest}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
