import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

trans_frames = [198, 202, 204, 206, 208, 210, 214, 220, 225]
sampled = []
for idx, f_num in enumerate(trans_frames):
    img = cv2.resize(all_frames[f_num], (160, 90))
    cv2.putText(img, f"T{idx}:{f_num}", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    sampled.append(img)

strip = cv2.hconcat(sampled)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/new_trans_sequence.jpg', strip)
print("Saved new_trans_sequence.jpg")