"""Generate 1200x630 Open Graph images into assets/images/og/ for each post
and a default one. Usage: uv run scripts/generate_og_images.py"""

import re
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets/images/og"
W, H = 1200, 630
BG, FG, MUTED, ACCENT = (17, 24, 39), (249, 250, 251), (156, 163, 175), (96, 165, 250)
FONTS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
BLOG = "Tongium's Blog"


def font(size):
    for f in FONTS:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    sys.exit("No bold font found; edit FONTS in this script.")


def render(title, path):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 16, H], fill=ACCENT)
    size = 76
    while True:
        f = font(size)
        lines = textwrap.wrap(title, width=max(10, int(1000 / (size * 0.55))))
        if len(lines) <= 4 and all(
            d.textlength(line, font=f) <= 1030 for line in lines
        ):
            break
        size -= 4
    lh = int(size * 1.25)
    y = (H - lh * len(lines)) // 2 - 20
    for line in lines:
        d.text((80, y), line, font=f, fill=FG)
        y += lh
    d.text((80, H - 90), BLOG, font=font(34), fill=ACCENT)
    d.text(
        (W - 80 - d.textlength("tongium.github.io", font=font(28)), H - 86),
        "tongium.github.io",
        font=font(28),
        fill=MUTED,
    )
    img.save(path, optimize=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    render(BLOG, OUT / "default.png")
    for p in sorted((ROOT / "_posts").glob("*.md")):
        text = p.read_text()
        m = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
        title = m.group(1).strip().strip("\"'")
        render(title, OUT / (p.stem[11:] + ".png"))
        print("generated", p.stem[11:])


if __name__ == "__main__":
    main()
