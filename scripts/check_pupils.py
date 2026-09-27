import struct

def read_bmp(path):
    with open(path, "rb") as f:
        data = f.read()
    offset = struct.unpack("<I", data[10:14])[0]
    w, h = struct.unpack("<ii", data[18:26])
    row_size = (w * 3 + 3) & ~3
    pixels = []
    for y in range(h):
        row_offset = offset + (h - 1 - y) * row_size
        row = []
        for x in range(w):
            b, g, r = struct.unpack("BBB", data[row_offset + x*3 : row_offset + x*3 + 3])
            row.append((r, g, b))
        pixels.append(row)
    return w, h, pixels

# Face is at x: 50% to 75% (160 to 240), y: 30% to 50% (54 to 90)
# Let's find the eye region:
# The pupils are dark. Let's find the average (x, y) of the darkest 50 pixels in the eye box
for f_idx in [0, 8, 16, 24, 32, 40, 48, 56]:
    w, h, pix = read_bmp(f"/home/mmuhina/repo/port/portfolio-2.0/scripts/f{f_idx}.bmp")
    # eye region: y from 60 to 85, x from 170 to 225
    candidates = []
    for y in range(60, 85):
        for x in range(170, 225):
            r, g, b = pix[y][x]
            # luminance
            lum = 0.299*r + 0.587*g + 0.114*b
            candidates.append((lum, x, y))
    candidates.sort()
    top50 = candidates[:60]
    avg_x = sum(c[1] for c in top50) / len(top50)
    avg_y = sum(c[2] for c in top50) / len(top50)
    print(f"Frame #{f_idx:2d}: pupil center = (x={avg_x:.1f}, y={avg_y:.1f})")