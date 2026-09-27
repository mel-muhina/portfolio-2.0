import cv2
import numpy as np

# Sector endpoints
# 0: UP = 36
# 8: UP-RIGHT = 60
# 16: RIGHT = 86
# 24: DOWN-RIGHT = 112
# 32: DOWN = 136
# 40: DOWN-LEFT = 168
# 48: LEFT = 194
# 56: UP-LEFT = 218
# 64: UP = 36 (via 224 / 34 / 35)

def get_sector_frames(start, end, count, skip_ranges=[]):
    # linearly interpolate indices
    raw = np.linspace(start, end, count, endpoint=False)
    indices = []
    for val in raw:
        idx = int(round(val))
        # if idx falls in skip range, adjust
        for (s, e, alt) in skip_ranges:
            if s <= idx <= e:
                idx = alt(idx)
        indices.append(idx)
    return indices

# Sector 0: 36 -> 60 (count 8)
s0 = get_sector_frames(36, 60, 8)
# Sector 1: 60 -> 86 (count 8)
s1 = get_sector_frames(60, 86, 8)
# Sector 2: 86 -> 112 (count 8)
s2 = get_sector_frames(86, 112, 8)
# Sector 3: 112 -> 136 (count 8), avoid 123-126
# Let's inspect indices in 112 -> 136:
# linspace(112, 136, 8) -> 112, 115, 118, 121, 124, 127, 130, 133
# 124 has eyes closed! 122 or 127 is open! So replace 124 with 127 or 122
s3 = [112, 115, 118, 121, 122, 127, 130, 133]
# Sector 4: 136 -> 168 (count 8)
s4 = get_sector_frames(136, 168, 8)
# Sector 5: 168 -> 194 (count 8)
s5 = get_sector_frames(168, 194, 8)
# Sector 6: 194 -> 218 (count 8), avoid 205-207
# linspace(194, 218, 8) -> 194, 197, 200, 203, 206(blink!), 209, 212, 215
# 206 is blink! 204 or 208 is open. Replace 206 with 208.
s6 = [194, 197, 200, 203, 204, 208, 211, 215]
# Sector 7: 218 -> UP (count 8)
# Frames from 218: 218, 220, 222, 224, 225, 33, 34, 35
s7 = [218, 220, 222, 224, 225, 33, 34, 35]

all_frames = s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7
print('Total 64 frames:', len(all_frames))
print('Frame list:', all_frames)

# Read video and create 8x8 contact sheet of all 64 frames
cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
loaded = {}
for i in range(240):
    ret, frame = cap.read()
    if not ret: break
    if i in all_frames or i == 237:
        loaded[i] = frame
cap.release()

sheet = np.zeros((8 * 125, 8 * 130, 3), dtype=np.uint8)
for i, f_num in enumerate(all_frames):
    r = i // 8
    c = i % 8
    head = loaded[f_num][50:550, 700:1220].copy()
    head = cv2.resize(head, (130, 125))
    cv2.putText(head, f'{i}:{f_num}', (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    sheet[r*125:(r+1)*125, c*130:(c+1)*130] = head

cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/contact_64.jpg', sheet)
print('Saved contact_64.jpg')