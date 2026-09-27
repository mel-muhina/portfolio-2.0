import cv2
import numpy as np

video_path = '/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'
cap = cv2.VideoCapture(video_path)

frames = []
idx = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Resize to small thumbnail (e.g. 160x90)
    thumb = cv2.resize(frame, (160, 90))
    cv2.putText(thumb, str(idx), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    frames.append(thumb)
    idx += 1

cap.release()
print(f'Total frames sequentially read: {len(frames)}')

# Create grid: 240 frames -> 15 columns x 16 rows
cols = 15
rows = 16
montage = np.zeros((rows * 90, cols * 160, 3), dtype=np.uint8)

for i, f in enumerate(frames):
    r = i // cols
    c = i % cols
    montage[r*90:(r+1)*90, c*160:(c+1)*160] = f

cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/montage.jpg', montage)
print('Saved montage to /home/mmuhina/repo/port/portfolio-2.0/scripts/montage.jpg')