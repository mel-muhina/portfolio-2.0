import subprocess
import numpy as np

def read_webp(path):
    cmd = ["ffmpeg", "-i", path, "-f", "rawvideo", "-pix_fmt", "bgr24", "pipe:1"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    out, _ = proc.communicate()
    return np.frombuffer(out, dtype=np.uint8).reshape((1080, 1920, 3))

def write_webp(arr, path, quality=95):
    cmd = ["ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", "1920x1080", "-i", "pipe:0", "-c:v", "libwebp", "-quality", str(quality), path]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    proc.communicate(input=arr.tobytes())

img0 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_0.webp")
img63 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_63.webp")
print(f"Read img0 shape: {img0.shape}, img63 shape: {img63.shape}")

# Average pixel difference
diff = np.mean(np.abs(img0.astype(float) - img63.astype(float)))
print(f"Mean pixel diff frame 0 vs frame 63: {diff:.2f}")