import cv2
import numpy as np

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
frames = {}
for i in range(240):
    ret, frame = cap.read()
    if not ret: break
    if 120 <= i <= 130 or 203 <= i <= 212:
        head = frame[50:550, 700:1220]
        frames[i] = cv2.resize(head, (160, 150))
cap.release()

for group_name, r in [('blink1', range(120, 131)), ('blink2', range(203, 213))]:
    strip = np.zeros((150, len(r)*160, 3), dtype=np.uint8)
    for idx, k in enumerate(r):
        img = frames[k].copy()
        cv2.putText(img, f'F:{k}', (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        strip[:, idx*160:(idx+1)*160] = img
    cv2.imwrite(f'/home/mmuhina/repo/port/portfolio-2.0/scripts/{group_name}.jpg', strip)

print('Saved blink inspection strips')