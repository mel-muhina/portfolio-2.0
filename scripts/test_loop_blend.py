import struct

def read_bmp(path):
    with open(path, "rb") as f:
        data = f.read()
    offset = struct.unpack("<I", data[10:14])[0]
    w, h = struct.unpack("<ii", data[18:26])
    row_size = (w * 3 + 3) & ~3
    pix = []
    for y in range(h):
        row_offset = offset + (h - 1 - y) * row_size
        row = []
        for x in range(w):
            b, g, r = struct.unpack("BBB", data[row_offset + x*3 : row_offset + x*3 + 3])
            pix.append((r, g, b))
    return pix

def diff(pA, pB):
    return sum(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) for a, b in zip(pA, pB)) / len(pA)

def blend(pA, pB, alpha):
    return [(int(a[0]*(1-alpha) + b[0]*alpha), int(a[1]*(1-alpha) + b[1]*alpha), int(a[2]*(1-alpha) + b[2]*alpha)) for a, b in zip(pA, pB)]

p0 = read_bmp("/home/mmuhina/repo/port/portfolio-2.0/scripts/f0.bmp")
p61 = read_bmp("/home/mmuhina/repo/port/portfolio-2.0/scripts/f62.bmp") # proxy for 61
p63_orig = read_bmp("/home/mmuhina/repo/port/portfolio-2.0/scripts/f63.bmp")

# Blend frame 63 as 50% p63_orig + 50% p0
b62 = blend(p61, p0, 0.33)
b63 = blend(p63_orig, p0, 0.67)

print(f"Diff 61 to b62: {diff(p61, b62):.2f}")
print(f"Diff b62 to b63: {diff(b62, b63):.2f}")
print(f"Diff b63 to 0  : {diff(b63, p0):.2f}")