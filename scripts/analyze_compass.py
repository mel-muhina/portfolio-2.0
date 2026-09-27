import cv2
import numpy as np

mp4_path = '/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'
cap = cv2.VideoCapture(mp4_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
all_frames = [cap.read()[1] for _ in range(total_frames)]
cap.release()

# Detect face center using facial feature bounding box or eyes
# Let's crop around head (y: 15% to 50%, x: 35% to 65%)
h, w = all_frames[0].shape[:2]

# Let's find background color
bg_samples = []
for f in all_frames:
    bg_samples.extend([f[20, 20], f[20, w-20], f[h-20, 20], f[h-20, w-20]])
bg_samples = np.array(bg_samples)
med_b, med_g, med_r = np.median(bg_samples, axis=0).astype(int)
print(f"Background Hex: #{med_r:02x}{med_g:02x}{med_b:02x}, RGB: ({med_r}, {med_g}, {med_b})")

# Let's analyze frames around key regions:
# 1. UP: around 20..30
# 2. UP-RIGHT: around 45..55
# 3. RIGHT: around 70..80
# 4. DOWN-RIGHT: around 85..95
# 5. DOWN: around 115..125
# 6. DOWN-LEFT: around 140..155
# 7. LEFT: around 165..175
# 8. UP-LEFT: around 185..195
# 9. UP: around 200..205
# 10. UP to CENTER: 200..220
# 11. CENTER: 0..5 and 220..239

# Let's save a strip of each region to pinpoint the exact frame numbers
regions = {
    "UP_start": (15, 30),
    "UP_RIGHT": (40, 60),
    "RIGHT": (65, 85),
    "DOWN_RIGHT": (85, 105),
    "DOWN": (110, 130),
    "DOWN_LEFT": (135, 155),
    "LEFT": (160, 180),
    "UP_LEFT": (180, 202),
    "UP_end": (198, 208),
    "TRANS_TO_CENTER": (202, 222),
    "CENTER": (220, 239)
}

for name, (start, end) in regions.items():
    frames_in_region = []
    for idx in range(start, end):
        f = cv2.resize(all_frames[idx], (160, 90))
        cv2.putText(f, str(idx), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        frames_in_region.append(f)
    strip = cv2.hconcat(frames_in_region)
    cv2.imwrite(f'/home/mmuhina/repo/port/portfolio-2.0/scripts/strip_{name}.jpg', strip)

print("Saved all region strips!")