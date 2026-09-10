from pathlib import Path
import gzip, hashlib, json
root = Path(__file__).resolve().parent
manifest = json.loads((root / "manifest.json").read_text())
html = gzip.decompress(b"".join((root / name).read_bytes() for name in manifest["parts"]))
assert len(html) == manifest["bytes"]
assert hashlib.sha256(html).hexdigest() == manifest["sha256"], "Source checksum mismatch"
out = root / "_site"
out.mkdir(exist_ok=True)
(out / "index.html").write_bytes(html)
(out / ".nojekyll").touch()
print("Verified full original HTML and embedded video; built _site/index.html")
