import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

# Let's crop eyes of frame 76 and frame 168
f76 = all_frames[76]
f168 = all_frames[168]

h, w = f76.shape[:2]
# Crop eyes (y: 35% to 48%, x: 54% to 74%)
crop76 = f76[int(h*0.35):int(h*0.48), int(w*0.54):int(w*0.74)]
crop168 = f168[int(h*0.35):int(h*0.48), int(w*0.54):int(w*0.74)]

cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/eyes_76.jpg', crop76)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/eyes_168.jpg', crop168)
print("Saved eyes_76.jpg and eyes_168.jpg")