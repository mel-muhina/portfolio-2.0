import cv2

frames = [cv2.imread(f'/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_{i}.webp') for i in range(40, 60)]

crops = []
for i, f in enumerate(frames):
    idx = i + 40
    h, w = f.shape[:2]
    crop = f[int(h*0.35):int(h*0.48), int(w*0.54):int(w*0.74)]
    crop = cv2.resize(crop, (150, 90))
    cv2.putText(crop, f"#{idx}", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    crops.append(crop)

r1 = cv2.hconcat(crops[:10])
r2 = cv2.hconcat(crops[10:20])
comp = cv2.vconcat([r1, r2])
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/check_frames_40_60.jpg', comp)
print("Saved check_frames_40_60.jpg")