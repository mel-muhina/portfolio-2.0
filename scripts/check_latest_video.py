import cv2
import os

mp4_path = '/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'

size = os.path.getsize(mp4_path)
mtime = os.path.getmtime(mp4_path)

cap = cv2.VideoCapture(mp4_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
ret, first_frame = cap.read()
cap.release()

print(f"File size: {size} bytes, Modified time: {mtime}")
print(f"Total frames: {total_frames}, FPS: {fps}, Dimensions: {width}x{height}")

if ret and first_frame is not None:
    b, g, r = first_frame[15, 15]
    print(f"Frame 0 Top-Left RGB: ({r}, {g}, {b}) -> #{r:02x}{g:02x}{b:02x}")