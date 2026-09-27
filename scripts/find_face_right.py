import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

center_frame = all_frames[225]
h, w = center_frame.shape[:2]

grid_img = center_frame.copy()

for x_pct in range(50, 90, 2):
    x = int(w * x_pct / 100)
    cv2.line(grid_img, (x, 0), (x, h), (0, 255, 0), 1)
    cv2.putText(grid_img, f"{x_pct}%", (x+2, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

for y_pct in range(25, 60, 2):
    y = int(h * y_pct / 100)
    cv2.line(grid_img, (0, y), (w, y), (0, 255, 0), 1)
    cv2.putText(grid_img, f"{y_pct}%", (int(w*0.5)+10, y-2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

crop = grid_img[int(h*0.25):int(h*0.60), int(w*0.50):int(w*0.90)]
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/face_grid_right.jpg', crop)
print("Saved face_grid_right.jpg")