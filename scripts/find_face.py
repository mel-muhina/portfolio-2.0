import cv2
import numpy as np

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

center_frame = all_frames[225]
h, w = center_frame.shape[:2]

# Let's find the eyes / nose / face center in frame 225
# Crop the upper body
# Let's save a crop with a grid overlaid to see the exact normalized coordinates
grid_img = center_frame.copy()

# Draw vertical lines every 2%
for x_pct in range(40, 60, 2):
    x = int(w * x_pct / 100)
    cv2.line(grid_img, (x, 0), (x, h), (0, 255, 0), 1)
    cv2.putText(grid_img, f"{x_pct}%", (x+2, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

# Draw horizontal lines every 2%
for y_pct in range(25, 55, 2):
    y = int(h * y_pct / 100)
    cv2.line(grid_img, (0, y), (w, y), (0, 255, 0), 1)
    cv2.putText(grid_img, f"{y_pct}%", (50, y-2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

crop = grid_img[int(h*0.25):int(h*0.55), int(w*0.40):int(w*0.60)]
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/face_grid.jpg', crop)
print("Saved face_grid.jpg")