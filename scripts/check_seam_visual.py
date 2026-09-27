import subprocess
import numpy as np

def read_webp(path):
    cmd = ["ffmpeg", "-i", path, "-f", "rawvideo", "-pix_fmt", "bgr24", "pipe:1"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    out, _ = proc.communicate()
    return np.frombuffer(out, dtype=np.uint8).reshape((1080, 1920, 3)).astype(float)

def write_jpg(arr, path):
    cmd = ["ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", "1920x1080", "-i", "pipe:0", "-q:v", "2", path]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    proc.communicate(input=np.clip(arr, 0, 255).astype(np.uint8).tobytes())

orig_61 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_61.webp")
orig_62 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_62.webp")
orig_63 = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_63.webp")
orig_0  = read_webp("/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_0.webp")

new_61 = 0.80 * orig_61 + 0.20 * orig_0
new_62 = 0.55 * orig_62 + 0.45 * orig_0
new_63 = 0.25 * orig_63 + 0.75 * orig_0

write_jpg(new_62, "/home/mmuhina/repo/port/portfolio-2.0/scripts/check_new_62.jpg")
write_jpg(new_63, "/home/mmuhina/repo/port/portfolio-2.0/scripts/check_new_63.jpg")
print("Saved check_new_62.jpg and check_new_63.jpg")