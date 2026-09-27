import cv2
import os
import json
import numpy as np

VIDEO_PATH = '/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'
OUTPUT_DIR = '/home/mmuhina/repo/port/portfolio-2.0/public/frames'
PUBLIC_DIR = '/home/mmuhina/repo/port/portfolio-2.0/public'

os.makedirs(OUTPUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

all_video_frames = []
for i in range(total_frames):
    ret, frame = cap.read()
    if not ret: break
    all_video_frames.append(frame)
cap.release()
print(f"Loaded {len(all_video_frames)} frames into memory")

# 72 trajectory frames
s0 = [17, 19, 21, 23, 25, 27, 29, 31, 33]
s1 = [35, 39, 43, 47, 51, 55, 60, 64, 68]
s2 = [70, 73, 75, 78, 81, 84, 86, 89, 91]
s3 = [92, 95, 98, 101, 103, 106, 109, 112, 114]
s4 = [115, 117, 118, 120, 122, 123, 125, 126, 127]
s5 = [128, 131, 133, 136, 139, 142, 144, 147, 149]
s6 = [150, 154, 158, 161, 163, 164, 165, 166, 168]
s7 = [170, 171, 173, 174, 176, 177, 178, 179, 180]

trajectory_72 = s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7
assert len(trajectory_72) == 72, f"Expected 72, got {len(trajectory_72)}"

# Transition frames from UP to CENTER
transition_frames = [180, 184, 188, 192, 195, 198, 203, 208, 235]

b, g, r = all_video_frames[0][10, 10]
bg_hex = f"#{r:02x}{g:02x}{b:02x}"
print(f"Detected Background Color: {bg_hex} (RGB: {r}, {g}, {b})")

webp_params = [cv2.IMWRITE_WEBP_QUALITY, 92]

# Save 72 trajectory frames
for idx, f_num in enumerate(trajectory_72):
    frame = all_video_frames[f_num]
    cv2.imwrite(f"{OUTPUT_DIR}/frame_{idx}.webp", frame, webp_params)
    cv2.imwrite(f"{OUTPUT_DIR}/{idx}.webp", frame, webp_params)

# Save transition frames
for idx, f_num in enumerate(transition_frames):
    frame = all_video_frames[f_num]
    cv2.imwrite(f"{OUTPUT_DIR}/transition_{idx}.webp", frame, webp_params)

# Save center neutral frame
center_frame = all_video_frames[235]
cv2.imwrite(f"{PUBLIC_DIR}/center.webp", center_frame, webp_params)
cv2.imwrite(f"{OUTPUT_DIR}/center.webp", center_frame, webp_params)

manifest = {
    "total_frames": 72,
    "degrees_per_frame": 360.0 / 72.0,
    "background_hex": bg_hex,
    "background_rgb": [int(r), int(g), int(b)],
    "resolution": {"width": width, "height": height},
    "face_center_normalized": {"x": 0.491, "y": 0.380},
    "compass_frame_indices": {
        "UP": 0,
        "UP_RIGHT": 9,
        "RIGHT": 18,
        "DOWN_RIGHT": 27,
        "DOWN": 36,
        "DOWN_LEFT": 45,
        "LEFT": 54,
        "UP_LEFT": 63
    },
    "source_video_frames": trajectory_72,
    "transition_video_frames": transition_frames,
    "center_source_frame": 235
}

with open(f"{OUTPUT_DIR}/manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print("Successfully extracted 72 trajectory frames, 9 transition frames, and center.webp!")