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

# Create a 6x10 contact sheet (60 sampled frames, every 4 frames)
sampled = []
for idx in range(0, total_frames, 4):
    f = cv2.resize(all_frames[idx], (192, 108))
    cv2.putText(f, str(idx), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)
    sampled.append(f)

# 10 rows of 6
rows = []
for r in range(10):
    rows.append(cv2.hconcat(sampled[r*6 : (r+1)*6]))
contact = cv2.vconcat(rows)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/latest_contact_60.jpg', contact)
print("Saved latest_contact_60.jpg")