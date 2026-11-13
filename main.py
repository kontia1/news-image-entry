import os, shutil
d = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(d, exist_ok=True)
s = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
t = os.path.join(d, "entry.png")
shutil.copyfile(s, t)
if os.path.getsize(s) >= 1 << 20: raise SystemExit("source image >= 1 MiB")
print(os.path.getsize(t))
