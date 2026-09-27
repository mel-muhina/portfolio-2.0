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

# Let's inspect background color across multiple regions
samples = []
for f in all_frames:
    samples.append(f[15, 15])
    samples.append(f[15, 1900])
    samples.append(f[1060, 15])
    samples.append(f[1060, 1900])

samples = np.array(samples)
med_b = int(np.median(samples[:, 0]))
med_g = int(np.median(samples[:, 1]))
med_r = int(np.median(samples[:, 2]))
bg_hex = f"#{med_r:02x}{med_g:02x}{med_b:02x}"
print(f"Median Background: RGB({med_r}, {med_g}, {med_b}) -> {bg_hex}")

# Save detailed contact sheet: 0 to 239 in steps of 5
contact_frames = []
for i in range(0, total_frames, 5):
    img = cv2.resize(all_frames[i], (192, 108))
    cv2.putText(img, str(i), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    contact_frames.append(img)

# Arrange into 8 rows of 6
rows = []
for r in range(8):
    rows.append(cv2.hconcat(contact_frames[r*6 : (r+1)*6]))
full_sheet = cv2.vconcat(rows)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/detailed_sheet.jpg', full_sheet)
print("Saved detailed_sheet.jpg")