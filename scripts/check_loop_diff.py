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
    return w, h, pix

w0, h0, p0 = read_bmp("/home/mmuhina/repo/port/portfolio-2.0/scripts/f0.bmp")
w63, h63, p63 = read_bmp("/home/mmuhina/repo/port/portfolio-2.0/scripts/f63.bmp")
w1, h1, p1 = read_bmp("/home/mmuhina/repo/port/portfolio-2.0/scripts/f1.bmp")
w62, h62, p62 = read_bmp("/home/mmuhina/repo/port/portfolio-2.0/scripts/f62.bmp")

def diff(pA, pB):
    total = sum(abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) for a, b in zip(pA, pB))
    return total / len(pA)

print(f"Diff f62 to f63: {diff(p62, p63):.2f}")
print(f"Diff f63 to f0 : {diff(p63, p0):.2f}")
print(f"Diff f0  to f1 : {diff(p0, p1):.2f}")