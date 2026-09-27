import cv2

f17 = cv2.imread('/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_0.webp')
f180 = cv2.imread('/home/mmuhina/repo/port/portfolio-2.0/public/frames/transition_0.webp')
f71 = cv2.imread('/home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_71.webp')

# Compare f17 and f180 side by side
h, w = f17.shape[:2]
crop17 = f17[int(h*0.1):int(h*0.7), int(w*0.3):int(w*0.7)]
crop180 = f180[int(h*0.1):int(h*0.7), int(w*0.3):int(w*0.7)]
crop71 = f71[int(h*0.1):int(h*0.7), int(w*0.3):int(w*0.7)]

comp = cv2.hconcat([crop17, crop71, crop180])
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/comp_17_71_180.jpg', comp)
print("Saved comp_17_71_180.jpg")
