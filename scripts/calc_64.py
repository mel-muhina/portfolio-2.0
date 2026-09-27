import cv2
import numpy as np

# Let's inspect the 8 octants:
# UP (0): 20
# UP_RIGHT (45): 46
# RIGHT (90): 72
# DOWN_RIGHT (135): 94
# DOWN (180): 118
# DOWN_LEFT (225): 142
# LEFT (270): 168
# UP_LEFT (315): 188
# UP (360): 200

# Let's test octant ranges:
# Octant 0 (0 to 45 deg): 20 to 46 (8 frames)
# Octant 1 (45 to 90 deg): 46 to 72 (8 frames)
# Octant 2 (90 to 135 deg): 72 to 94 (8 frames)
# Octant 3 (135 to 180 deg): 94 to 118 (8 frames)
# Octant 4 (180 to 225 deg): 118 to 142 (8 frames)
# Octant 5 (225 to 270 deg): 142 to 168 (8 frames)
# Octant 6 (270 to 315 deg): 168 to 188 (8 frames)
# Octant 7 (315 to 360 deg): 188 to 200 (8 frames)

def linspace_frames(start, end, count):
    return [int(round(x)) for x in np.linspace(start, end, count, endpoint=False)]

o0 = linspace_frames(20, 46, 8)
o1 = linspace_frames(46, 72, 8)
o2 = linspace_frames(72, 94, 8)
o3 = linspace_frames(94, 118, 8)
o4 = linspace_frames(118, 142, 8)
o5 = linspace_frames(142, 168, 8)
o6 = linspace_frames(168, 188, 8)
o7 = linspace_frames(188, 200, 8)

frames_64 = o0 + o1 + o2 + o3 + o4 + o5 + o6 + o7
print(f"Total 64 frames: {len(frames_64)}")
print("Octants:")
for i in range(8):
    print(f"O{i}: {frames_64[i*8:(i+1)*8]}")

# Center frame:
# Look at frames 215..235
# Let's check frame 225 as center neutral
print("Center frame: 225")

# Transition from UP (200) to CENTER (225):
# Frames: 200, 202, 204, 206, 208, 210, 213, 217, 225 (9 frames)
transition_frames = [200, 202, 204, 206, 208, 210, 213, 217, 225]
print("Transition frames:", transition_frames)

# Save contact sheet of the 64 frames
cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

sheet_imgs = []
for idx, f_num in enumerate(frames_64):
    img = cv2.resize(all_frames[f_num], (160, 90))
    cv2.putText(img, f"#{idx}:{f_num}", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    sheet_imgs.append(img)

# 8 rows of 8
rows = [cv2.hconcat(sheet_imgs[r*8:(r+1)*8]) for r in range(8)]
contact_64 = cv2.vconcat(rows)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/contact_64_new.jpg', contact_64)
print("Saved contact_64_new.jpg")