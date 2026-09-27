import cv2

cap = cv2.VideoCapture('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4')
all_frames = [cap.read()[1] for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))]
cap.release()

# Let's inspect the 9 poses in the new video:
poses = {
    "center_forward": 228,
    "slightly_up": 32,
    "upper_right": 56,
    "slightly_right": 76,
    "lower_right": 96,
    "slightly_down": 124,
    "lower_left": 144,
    "slightly_left": 168,
    "upper_left": 188
}

sheet = []
for name, f_num in poses.items():
    img = cv2.resize(all_frames[f_num], (320, 180))
    cv2.putText(img, f"{name} (#{f_num})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
    sheet.append(img)

# 3x3 grid:
# Upper-Left, Up, Upper-Right
# Left, Center, Right
# Lower-Left, Down, Lower-Right
grid_3x3 = cv2.vconcat([
    cv2.hconcat([sheet[8], sheet[1], sheet[2]]), # Upper-Left, Up, Upper-Right
    cv2.hconcat([sheet[7], sheet[0], sheet[3]]), # Left, Center, Right
    cv2.hconcat([sheet[6], sheet[5], sheet[4]])  # Lower-Left, Down, Lower-Right
])

cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/nine_poses.jpg', grid_3x3)
print("Saved nine_poses.jpg")