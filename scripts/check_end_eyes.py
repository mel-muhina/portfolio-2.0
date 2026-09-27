import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

# Let's crop eyes for frames 210 to 239 in steps of 2
crops = []
for i in range(210, 240, 2):
    f = all_frames[i]
    h, w = f.shape[:2]
    crop = f[int(h*0.35):int(h*0.48), int(w*0.50):int(w*0.70)]
    crop = cv2.resize(crop, (160, 100))
    cv2.putText(crop, f"{i}", (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    crops.append(crop)

# 3 rows of 5
r1 = cv2.hconcat(crops[:5])
r2 = cv2.hconcat(crops[5:10])
r3 = cv2.hconcat(crops[10:15])
grid = cv2.vconcat([r1, r2, r3])
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/end_eyes.jpg', grid)
print("Saved end_eyes.jpg")