import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = []
while True:
    ret, f = cap.read()
    if not ret: break
    all_frames.append(f)
cap.release()

print(f"Total video frames: {len(all_frames)}")
# Let's inspect what happens in:
# 0..17
# 17..180
# 180..240
# Are there any other cuts or shots?
