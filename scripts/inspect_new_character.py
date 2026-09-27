import cv2
import numpy as np

mp4_path = '/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'
cap = cv2.VideoCapture(mp4_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

all_frames = []
for i in range(total_frames):
    ret, frame = cap.read()
    if not ret: break
    all_frames.append(frame)
cap.release()

print(f"Loaded {len(all_frames)} frames.")

# Check corners background across frames
corners_rgb = []
for f in all_frames[::10]:
    b, g, r = f[10, 10]
    corners_rgb.append((r, g, b))

avg_r = int(np.mean([c[0] for c in corners_rgb]))
avg_g = int(np.mean([c[1] for c in corners_rgb]))
avg_b = int(np.mean([c[2] for c in corners_rgb]))
bg_hex = f"#{avg_r:02x}{avg_g:02x}{avg_b:02x}"
print(f"Average Corner RGB: ({avg_r}, {avg_g}, {avg_b}) -> {bg_hex}")

# Sample 24 frames across video to make a 4x6 montage
sampled = [cv2.resize(all_frames[i], (320, 180)) for i in range(0, total_frames, 10)]
rows = []
for r in range(4):
    row = cv2.hconcat(sampled[r*6 : (r+1)*6])
    rows.append(row)
montage = cv2.vconcat(rows)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/new_char_montage.jpg', montage)
print("Saved new_char_montage.jpg")
