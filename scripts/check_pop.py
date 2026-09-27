# Compare f0.bmp (video 32) and f63.bmp (video 200)
# Let us convert frame_63.webp to f63.bmp first
import struct

def read_bmp_pixels(bmp_path):
    with open(bmp_path, "rb") as f:
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