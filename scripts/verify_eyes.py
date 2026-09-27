import struct

def get_pupil(bmp_path):
    with open(bmp_path, "rb") as f:
        data = f.read()
    offset = struct.unpack("<I", data[10:14])[0]
    w, h = struct.unpack("<ii", data[18:26])
    row_size = (w * 3 + 3) & ~3
    candidates = []
    for y in range(60, 85):
        row_offset = offset + (h - 1 - y) * row_size
        for x in range(170, 225):
            b, g, r = struct.unpack("BBB", data[row_offset + x*3 : row_offset + x*3 + 3])
            lum = 0.299*r + 0.587*g + 0.114*b
            candidates.append((lum, x, y))
    candidates.sort()
    top40 = candidates[:40]
    return sum(c[1] for c in top40)/40, sum(c[2] for c in top40)/40

for idx in [0, 8, 16, 24, 32, 40, 48, 56]:
    px, py = get_pupil(f"/home/mmuhina/repo/port/portfolio-2.0/scripts/f{idx}.bmp")
    print(f"Frame #{idx:2d}: pupil X={px:.2f}, Y={py:.2f}")