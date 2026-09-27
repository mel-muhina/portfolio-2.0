import cv2
import numpy as np

# Load trajectory frames and transition frames
OUTPUT_DIR = '/home/mmuhina/repo/port/portfolio-2.0/public/frames'
frames_72 = [cv2.imread(f"{OUTPUT_DIR}/frame_{i}.webp") for i in range(72)]
transitions = [cv2.imread(f"{OUTPUT_DIR}/transition_{i}.webp") for i in range(9)]
center = cv2.imread(f"{OUTPUT_DIR}/center.webp")

def get_path_to_center(start_idx, speed=1):
    # Shortest path to index 0
    # Option 1: clockwise or counterclockwise
    dist_cw = (72 - start_idx) % 72
    dist_ccw = start_idx
    
    path_indices = []
    curr = start_idx
    if dist_cw <= dist_ccw:
        # Move forward towards 72/0
        while curr != 0:
            path_indices.append(frames_72[curr])
            curr = (curr + speed) % 72
            if curr < speed and curr != 0:
                curr = 0
    else:
        # Move backward towards 0
        while curr != 0:
            path_indices.append(frames_72[curr])
            curr = (curr - speed + 72) % 72
            if curr > (72 - speed) and curr != 0:
                curr = 0
                
    path_indices.append(frames_72[0])
    
    # Now append transition frames 1..8
    for t in transitions[1:]:
        path_indices.append(t)
    path_indices.append(center)
    return path_indices

# Let's test from LEFT (index 54)
path_left = get_path_to_center(54, speed=2)
print(f"Path from LEFT to center has {len(path_left)} frames")

# Create a montage of path_left
sampled = [cv2.resize(f, (160, 90)) for f in path_left[::2]]
if len(sampled) > 12:
    # take 12 evenly spaced
    idxs = np.linspace(0, len(path_left)-1, 12, dtype=int)
    sampled = [cv2.resize(path_left[i], (160, 90)) for i in idxs]

strip = cv2.hconcat(sampled)
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/test_path_left.jpg', strip)
print("Saved test_path_left.jpg")
