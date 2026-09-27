import cv2
import numpy as np

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')

frames = []
idx = 0
while True:
    ret, frame = cap.read()
    if not ret: break
    # Crop head region: Y: 50..550, X: 700..1220
    head = frame[50:550, 700:1220].copy()
    head = cv2.resize(head, (130, 125))
    cv2.putText(head, str(idx), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    frames.append(head)
    idx += 1
cap.release()

# Let's save 3 contact sheets:
# Sheet 1: 0 to 79
# Sheet 2: 80 to 159
# Sheet 3: 160 to 239
cols = 10
rows = 8
for sheet_idx, start_f in enumerate([0, 80, 160]):
    sheet = np.zeros((rows * 125, cols * 130, 3), dtype=np.uint8)
    for i in range(80):
        f_num = start_f + i
        if f_num < len(frames):
            r = i // cols
            c = i % cols
            sheet[r*125:(r+1)*125, c*130:(c+1)*130] = frames[f_num]
    cv2.imwrite(f'/home/mmuhina/repo/port/portfolio-2.0/scripts/sheet_{sheet_idx}.jpg', sheet)

print('Saved sheets 0, 1, 2')