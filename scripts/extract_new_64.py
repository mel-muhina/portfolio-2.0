import cv2
import os
import json
import glob

VIDEO_PATH = '/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'
OUTPUT_DIR = '/home/mmuhina/repo/port/portfolio-2.0/public/frames'
PUBLIC_DIR = '/home/mmuhina/repo/port/portfolio-2.0/public'

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Remove any old frame files (especially 64..71 from previous 72-frame run)
old_frames = glob.glob(f"{OUTPUT_DIR}/frame_*.webp") + glob.glob(f"{OUTPUT_DIR}/[0-9]*.webp")
for f in old_frames:
    try:
        os.remove(f)
    except:
        pass

cap = cv2.VideoCapture(VIDEO_PATH)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

all_frames = []
for i in range(total_frames):
    ret, frame = cap.read()
    if not ret: break
    all_frames.append(frame)
cap.release()

print(f"Loaded {len(all_frames)} frames.")

# 64 trajectory frames
o0 = [20, 23, 26, 30, 33, 36, 40, 43]
o1 = [46, 49, 52, 56, 59, 62, 66, 69]
o2 = [72, 75, 78, 80, 83, 86, 88, 91]
o3 = [94, 97, 100, 103, 106, 109, 112, 115]
o4 = [118, 121, 124, 127, 130, 133, 136, 139]
o5 = [142, 145, 148, 152, 155, 158, 162, 165]
o6 = [168, 170, 173, 176, 178, 180, 183, 186]
o7 = [188, 190, 191, 192, 194, 196, 197, 198]

trajectory_64 = o0 + o1 + o2 + o3 + o4 + o5 + o6 + o7
assert len(trajectory_64) == 64, f"Expected 64, got {len(trajectory_64)}"

# Transition frames from UP to CENTER
transition_frames = [198, 202, 204, 206, 208, 210, 214, 220, 225]

# Center frame
center_frame_num = 225

webp_params = [cv2.IMWRITE_WEBP_QUALITY, 95]

# Save 64 trajectory frames
for idx, f_num in enumerate(trajectory_64):
    frame = all_frames[f_num]
    cv2.imwrite(f"{OUTPUT_DIR}/frame_{idx}.webp", frame, webp_params)
    cv2.imwrite(f"{OUTPUT_DIR}/{idx}.webp", frame, webp_params)

# Save 9 transition frames
for idx, f_num in enumerate(transition_frames):
    frame = all_frames[f_num]
    cv2.imwrite(f"{OUTPUT_DIR}/transition_{idx}.webp", frame, webp_params)

# Save center frame
center_frame = all_frames[center_frame_num]
cv2.imwrite(f"{PUBLIC_DIR}/center.webp", center_frame, webp_params)
cv2.imwrite(f"{OUTPUT_DIR}/center.webp", center_frame, webp_params)

manifest = {
    "total_frames": 64,
    "degrees_per_frame": 360.0 / 64.0,
    "background_hex": "#212455",
    "background_rgb": [33, 36, 85],
    "resolution": {"width": width, "height": height},
    "face_center_normalized": {"x": 0.640, "y": 0.430},
    "compass_frame_indices": {
        "UP": 0,
        "UP_RIGHT": 8,
        "RIGHT": 16,
        "DOWN_RIGHT": 24,
        "DOWN": 32,
        "DOWN_LEFT": 40,
        "LEFT": 48,
        "UP_LEFT": 56
    },
    "source_video_frames": trajectory_64,
    "transition_video_frames": transition_frames,
    "center_source_frame": center_frame_num
}

with open(f"{OUTPUT_DIR}/manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print("Successfully extracted 64 high-quality WebP frames, 9 transition frames, and center.webp!")