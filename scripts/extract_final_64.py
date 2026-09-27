import cv2
import os
import json
import glob

VIDEO_PATH = '/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'
OUTPUT_DIR = '/home/mmuhina/repo/port/portfolio-2.0/public/frames'
PUBLIC_DIR = '/home/mmuhina/repo/port/portfolio-2.0/public'

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Clean up all existing frames
for f in glob.glob(f"{OUTPUT_DIR}/*.webp"):
    try: os.remove(f)
    except: pass

cap = cv2.VideoCapture(VIDEO_PATH)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
all_frames = [cap.read()[1] for _ in range(total_frames)]
cap.release()

print(f"Loaded {len(all_frames)} frames.")

# 8 octants, 8 frames each:
o0 = [32, 35, 38, 41, 44, 47, 50, 53] # UP (0) -> UPPER-RIGHT (45)
o1 = [56, 58, 61, 64, 67, 70, 72, 74] # UPPER-RIGHT (45) -> RIGHT (90)
o2 = [76, 78, 81, 84, 87, 90, 92, 94] # RIGHT (90) -> LOWER-RIGHT (135)
o3 = [96, 99, 103, 107, 110, 114, 118, 122] # LOWER-RIGHT (135) -> DOWN (180)
o4 = [124, 127, 130, 133, 136, 139, 142, 144] # DOWN (180) -> LOWER-LEFT (225)
o5 = [146, 149, 152, 155, 158, 161, 164, 167] # LOWER-LEFT (225) -> LEFT (270)
o6 = [170, 172, 174, 177, 180, 182, 185, 187] # LEFT (270) -> UPPER-LEFT (315)
o7 = [188, 190, 192, 194, 196, 197, 198, 200] # UPPER-LEFT (315) -> UP (360)

trajectory_64 = o0 + o1 + o2 + o3 + o4 + o5 + o6 + o7
assert len(trajectory_64) == 64

# Transition frames from UP to CENTER
trans_10 = [200, 202, 204, 206, 208, 210, 214, 218, 224, 228]
center_f = 228

webp_params = [cv2.IMWRITE_WEBP_QUALITY, 95]

# Save 64 trajectory frames
for idx, f_num in enumerate(trajectory_64):
    frame = all_frames[f_num]
    cv2.imwrite(f"{OUTPUT_DIR}/frame_{idx}.webp", frame, webp_params)
    cv2.imwrite(f"{OUTPUT_DIR}/{idx}.webp", frame, webp_params)

# Save 10 transition frames
for idx, f_num in enumerate(trans_10):
    frame = all_frames[f_num]
    cv2.imwrite(f"{OUTPUT_DIR}/transition_{idx}.webp", frame, webp_params)

# Save center neutral frame (228)
center_frame = all_frames[center_f]
cv2.imwrite(f"{PUBLIC_DIR}/center.webp", center_frame, webp_params)
cv2.imwrite(f"{OUTPUT_DIR}/center.webp", center_frame, webp_params)

manifest = {
    "total_frames": 64,
    "total_transitions": 10,
    "degrees_per_frame": 360.0 / 64.0,
    "background_hex": "#212455",
    "background_rgb": [33, 36, 85],
    "resolution": {"width": width, "height": height},
    "face_center_normalized": {"x": 0.640, "y": 0.430},
    "compass_frame_indices": {
        "slightly_up": 0,
        "upper_right": 8,
        "slightly_right": 16,
        "lower_right": 24,
        "slightly_down": 32,
        "lower_left": 40,
        "slightly_left": 48,
        "upper_left": 56
    },
    "source_video_frames": trajectory_64,
    "transition_video_frames": trans_10,
    "center_source_frame": center_f
}

with open(f"{OUTPUT_DIR}/manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print("Extraction complete! 64 trajectory frames, 10 transition frames, and center.webp saved successfully.")