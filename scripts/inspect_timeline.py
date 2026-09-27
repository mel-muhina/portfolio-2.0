import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = []
while True:
    ret, f = cap.read()
    if not ret: break
    all_frames.append(f)
cap.release()

# Let's save a strip of frames 0..17 to see the motion
strip = [cv2.resize(all_frames[i], (240, 135)) for i in range(0, 18, 2)]
strip_img = cv2.hconcat(strip)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/strip_0_17.jpg', strip_img)
print("Saved strip_0_17.jpg")
