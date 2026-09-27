import subprocess
import numpy as np

def read_webp(path):
    cmd = ["ffmpeg", "-i", path, "-f", "rawvideo", "-pix_fmt", "bgr24", "pipe:1"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    out, _ = proc.communicate()
    return np.frombuffer(out, dtype=np.uint8).reshape((1080, 1920, 3)).astype(float)

orig_60 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_60.webp")
orig_61 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_61.webp")
orig_62 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_62.webp")
orig_63 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_63.webp")
orig_0  = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_0.webp")
orig_1  = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_1.webp")

# Let's test progressive blend:
new_61 = 0.80 * orig_61 + 0.20 * orig_0
new_62 = 0.55 * orig_62 + 0.45 * orig_0
new_63 = 0.25 * orig_63 + 0.75 * orig_0

def d(a, b):
    return np.mean(np.abs(a - b))

print(f"Diff 60 -> new_61: {d(orig_60, new_61):.2f}")
print(f"Diff new_61 -> new_62: {d(new_61, new_62):.2f}")
print(f"Diff new_62 -> new_63: {d(new_62, new_63):.2f}")
print(f"Diff new_63 -> 0     : {d(new_63, orig_0):.2f}")
print(f"Diff 0 -> 1          : {d(orig_0, orig_1):.2f}")