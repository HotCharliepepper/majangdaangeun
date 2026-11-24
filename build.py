"""Build the intentionally unlocked Daangn proposal, excluding all non-site files."""
from pathlib import Path
from urllib.parse import urlsplit
from html import escape
import os, shutil
ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
if DIST.exists(): shutil.rmtree(DIST)
DIST.mkdir()
origin = os.environ.get("URL", "").strip().rstrip("/")
page = (ROOT / "index.html").read_text(encoding="utf-8")
if origin:
    p = urlsplit(origin)
    if p.scheme != "https" or not p.hostname or p.username or p.password or p.query or p.fragment or p.path or any(c.isspace() or c in '\"<>\\' for c in origin):
        raise SystemExit("URL must be an HTTPS site origin")
    origin = escape(origin, quote=True)
    page = page.replace('content="./" property="og:url"', 'content="'+origin+'/" property="og:url"')
    page = page.replace('content="assets/share-thumbnail.jpg" property="og:image"', 'content="'+origin+'/assets/share-thumbnail.jpg" property="og:image"')
    page = page.replace('content="assets/share-thumbnail.jpg" name="twitter:image"', 'content="'+origin+'/assets/share-thumbnail.jpg" name="twitter:image"')
(DIST / "index.html").write_text(page, encoding="utf-8")
(DIST / "assets").mkdir()
for name in ("strategy-cover.jpg", "share-thumbnail.jpg"):
    shutil.copyfile(ROOT / "assets" / name, DIST / "assets" / name)
(DIST / "_headers").write_text("/*\n  X-Robots-Tag: noindex, nofollow, noarchive\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: no-referrer\n", encoding="utf-8")
print("Unlocked proposal built. No release variables required.")
