import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
ret, frame = cap.read()
cap.release()

h, w = frame.shape[:2]
print(f"Video resolution: {w}x{h}")

# Draw vertical lines across the ENTIRE frame from 0 to 100% in steps of 10%
for pct in range(10, 100, 10):
    x = int(w * pct / 100)
    cv2.line(frame, (x, 0), (x, h), (0, 255, 0), 2)
    cv2.putText(frame, f"{pct}%", (x+5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

for pct in range(10, 100, 10):
    y = int(h * pct / 100)
    cv2.line(frame, (0, y), (w, y), (0, 255, 0), 2)
    cv2.putText(frame, f"{pct}%", (50, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/full_frame_grid.jpg', cv2.resize(frame, (960, 540)))
print("Saved full_frame_grid.jpg")