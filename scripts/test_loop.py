import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

f20 = all_frames[20]
f198 = all_frames[198]
f200 = all_frames[200]

diff_198_20 = cv2.absdiff(f198, f20).mean()
diff_200_20 = cv2.absdiff(f200, f20).mean()
print(f"Diff 198 vs 20: {diff_198_20:.2f}")
print(f"Diff 200 vs 20: {diff_200_20:.2f}")

# Side by side of 198 and 20
h, w = f20.shape[:2]
c198 = f198[int(h*0.2):int(h*0.65), int(w*0.5):int(w*0.8)]
c20 = f20[int(h*0.2):int(h*0.65), int(w*0.5):int(w*0.8)]
comp = cv2.hconcat([c198, c20])
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/comp_loop.jpg', comp)
print("Saved comp_loop.jpg")