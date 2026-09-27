import cv2
import numpy as np

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

center = all_frames[225]

# Directions to test:
# Right: 76
# Lower-Right: 96
# Down: 124
# Lower-Left: 148
# Left: 170
# Upper-Left: 188
# Up: 32
# Upper-Right: 56

test_dirs = {
    "Right": 76,
    "LowerRight": 96,
    "Down": 124,
    "LowerLeft": 148,
    "Left": 170,
    "UpperLeft": 188,
    "Up": 32,
    "UpperRight": 56
}

# For each direction, blend with center at alpha = [0.0, 0.25, 0.5, 0.75, 1.0]
strips = []
for name, f_num in test_dirs.items():
    src = all_frames[f_num]
    blends = []
    for alpha in [0.0, 0.25, 0.5, 0.75, 1.0]:
        # alpha 0 = src, alpha 1 = center
        blended = cv2.addWeighted(src, 1.0 - alpha, center, alpha, 0)
        s = cv2.resize(blended, (160, 90))
        cv2.putText(s, f"{name} a={alpha}", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
        blends.append(s)
    strips.append(cv2.hconcat(blends))

comp = cv2.vconcat(strips)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/test_radial_blends.jpg', comp)
print("Saved test_radial_blends.jpg")