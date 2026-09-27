import cv2
import numpy as np

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

print(f"Total frames: {len(all_frames)}")

# Let's inspect eye pupils and head orientation:
# We know from latest_contact_60.jpg:
# Frame 0..4: Center forward
# Frame 24..40: Looking UP
# Frame 50..64: Upper-Right
# Frame 70..84: Right
# Frame 90..105: Lower-Right
# Frame 115..135: Down
# Frame 140..160: Lower-Left
# Frame 165..180: Left
# Frame 185..200: Upper-Left
# Frame 200..216: UP to Center transition
# Frame 216..239: Center forward

# Let's save high-res crops of head for frames in steps of 2 around key ranges:
def save_crop_strip(name, start, end):
    crops = []
    for i in range(start, end, 2):
        f = all_frames[i]
        h, w = f.shape[:2]
        crop = f[int(h*0.25):int(h*0.65), int(w*0.5):int(w*0.78)]
        crop = cv2.resize(crop, (120, 160))
        cv2.putText(crop, str(i), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        crops.append(crop)
    strip = cv2.hconcat(crops)
    cv2.imwrite(f'/home/mmuhina/repo/port/portfolio-2.0/scripts/detail_{name}.jpg', strip)

save_crop_strip("up_to_right", 28, 80)
save_crop_strip("right_to_down", 76, 130)
save_crop_strip("down_to_left", 126, 180)
save_crop_strip("left_to_up", 176, 210)
save_crop_strip("trans_center", 200, 230)
print("Saved all detail strips!")