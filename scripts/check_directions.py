import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

center = all_frames[228]
frames_to_check = [32, 56, 76, 96, 124, 144, 170, 188, 228]
h, w = center.shape[:2]

crops = []
for f_idx in frames_to_check:
    img = all_frames[f_idx]
    cropped = img[int(h*0.25):int(h*0.60), int(w*0.50):int(w*0.78)].copy()
    cv2.putText(cropped, f'#{f_idx}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    crops.append(cropped)

strip1 = cv2.hconcat(crops[:5])
pad = crops[0].copy()
pad[:] = 0
strip2 = cv2.hconcat(crops[5:] + [pad])
final_comp = cv2.vconcat([strip1, strip2])
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/pupil_comp.jpg', final_comp)
print('Saved pupil_comp.jpg successfully')
