import cv2
import numpy as np

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

# 8 octants, 8 frames each:
o0 = [32, 35, 38, 41, 44, 47, 50, 53] # UP (0) -> UPPER-RIGHT (45)
o1 = [56, 58, 61, 64, 67, 70, 72, 74] # UPPER-RIGHT (45) -> RIGHT (90)
o2 = [76, 78, 81, 84, 87, 90, 92, 94] # RIGHT (90) -> LOWER-RIGHT (135)
o3 = [96, 99, 103, 107, 110, 114, 118, 122] # LOWER-RIGHT (135) -> DOWN (180)
o4 = [124, 127, 130, 133, 136, 139, 142, 144] # DOWN (180) -> LOWER-LEFT (225)
o5 = [146, 149, 152, 155, 158, 161, 164, 167] # LOWER-LEFT (225) -> LEFT (270)
o6 = [170, 172, 174, 177, 180, 182, 185, 187] # LEFT (270) -> UPPER-LEFT (315)
o7 = [188, 190, 192, 194, 196, 197, 198, 200] # UPPER-LEFT (315) -> UP (360)

trajectory_64 = o0 + o1 + o2 + o3 + o4 + o5 + o6 + o7
assert len(trajectory_64) == 64

# Transition frames from UP to CENTER
trans_10 = [200, 202, 204, 206, 208, 210, 214, 218, 224, 228]

# Save contact sheet
sheet_imgs = []
for idx, f_num in enumerate(trajectory_64):
    img = cv2.resize(all_frames[f_num], (160, 90))
    cv2.putText(img, f"#{idx}:{f_num}", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    sheet_imgs.append(img)

rows = [cv2.hconcat(sheet_imgs[r*8:(r+1)*8]) for r in range(8)]
contact_64 = cv2.vconcat(rows)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/perfect_contact_64.jpg', contact_64)
print("Saved perfect_contact_64.jpg")