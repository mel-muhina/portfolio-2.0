import cv2
import numpy as np

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
frames = {}
for i in range(240):
    ret, frame = cap.read()
    if not ret: break
    if i in [34, 35, 36, 37, 38, 222, 223, 224, 225, 235, 236, 237, 238]:
        head = frame[50:550, 700:1220]
        frames[i] = cv2.resize(head, (160, 150))
cap.release()

# Save comparison image
keys = [222, 223, 224, 225, 34, 35, 36, 37, 38, 235, 236, 237, 238]
strip = np.zeros((150, len(keys)*160, 3), dtype=np.uint8)
for idx, k in enumerate(keys):
    img = frames[k].copy()
    cv2.putText(img, f'F:{k}', (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    strip[:, idx*160:(idx+1)*160] = img

cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/compare_up_center.jpg', strip)
print('Saved compare_up_center.jpg')