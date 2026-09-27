import struct
import glob
import os

def read_bmp(path):
    with open(path, "rb") as f:
        data = f.read()
    offset = struct.unpack("<I", data[10:14])[0]
    w, h = struct.unpack("<ii", data[18:26])
    row_size = (w * 3 + 3) & ~3
    pix = []
    for y in range(h):
        row_offset = offset + (h - 1 - y) * row_size
        for x in range(w):
            b, g, r = struct.unpack("BBB", data[row_offset + x*3 : row_offset + x*3 + 3])
            pix.append((r, g, b))
    return pix

def diff(pA, pB):
    return sum(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) for a, b in zip(pA, pB)) / len(pA)

start_files = sorted(glob.glob("/home/mmuhina/repo/port/portfolio-2.0/scripts/frames_loop/f_start_*.bmp"))
end_files = sorted(glob.glob("/home/mmuhina/repo/port/portfolio-2.0/scripts/frames_loop/f_end_*.bmp"))

start_pix = [(int(os.path.basename(f).split("_")[2].split(".")[0]) + 20, read_bmp(f)) for f in start_files]
end_pix = [(int(os.path.basename(f).split("_")[2].split(".")[0]) + 190, read_bmp(f)) for f in end_files]

matches = []
for f_end_num, pE in end_pix:
    for f_start_num, pS in start_pix:
        d = diff(pE, pS)
        matches.append((d, f_end_num, f_start_num))

matches.sort()
print("Top 10 closest frame matches between end (190..215) and start (20..40):")
for d, e, s in matches[:10]:
    print(f"Video frame {e} -> Video frame {s}: diff = {d:.2f}")