import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

# Let's test blending adjacent trajectory frames
# Say frame 46 (UP-RIGHT) and 49 (next in UP-RIGHT)
f1 = all_frames[46]
f2 = all_frames[49]

# Blend 50/50
blend = cv2.addWeighted(f1, 0.5, f2, 0.5, 0)

h, w = f1.shape[:2]
c1 = f1[int(h*0.25):int(h*0.65), int(w*0.5):int(w*0.8)]
cb = blend[int(h*0.25):int(h*0.65), int(w*0.5):int(w*0.8)]
c2 = f2[int(h*0.25):int(h*0.65), int(w*0.5):int(w*0.8)]

comp = cv2.hconcat([c1, cb, c2])
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/test_adjacent_blend.jpg', comp)
print("Saved test_adjacent_blend.jpg")