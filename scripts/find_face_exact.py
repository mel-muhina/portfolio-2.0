import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

center_frame = all_frames[225]
h, w = center_frame.shape[:2]

grid_img = center_frame.copy()

for x_pct in range(50, 80, 2):
    x = int(w * x_pct / 100)
    cv2.line(grid_img, (x, 0), (x, h), (0, 255, 0), 1)
    cv2.putText(grid_img, f"{x_pct}", (x-10, int(h*0.36)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

crop = grid_img[int(h*0.33):int(h*0.52), int(w*0.50):int(w*0.80)]
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/face_exact_x.jpg', crop)