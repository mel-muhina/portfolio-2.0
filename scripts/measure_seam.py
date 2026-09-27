import subprocess
import numpy as np

def read_webp(path):
    cmd = ["ffmpeg", "-i", path, "-f", "rawvideo", "-pix_fmt", "bgr24", "pipe:1"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    out, _ = proc.communicate()
    return np.frombuffer(out, dtype=np.uint8).reshape((1080, 1920, 3))

imgs = {}
for idx in [59, 60, 61, 62, 63, 0, 1, 2, 3]:
    imgs[idx] = read_webp(f"/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_{idx}.webp")

seq = [59, 60, 61, 62, 63, 0, 1, 2, 3]
for i in range(len(seq) - 1):
    a = seq[i]
    b = seq[i+1]
    d = np.mean(np.abs(imgs[a].astype(float) - imgs[b].astype(float)))
    print(f"Diff frame {a:2d} -> frame {b:2d}: {d:.2f}")