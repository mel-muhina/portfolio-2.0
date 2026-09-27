import cv2
import os

video_path = '/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'
out_dir = '/home/mmuhina/repo/port/portfolio-2.0/scripts/sampled_frames'
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

step = 4 # Every 4 frames -> 60 samples
for i in range(0, total_frames, step):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    if not ret:
        break
    # Resize to width 320 for quick preview
    h, w = frame.shape[:2]
    thumb = cv2.resize(frame, (320, int(320 * h / w)))
    cv2.putText(thumb, f'F:{i}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.imwrite(f'{out_dir}/frame_{i:03d}.jpg', thumb)

print('Saved sampled frames to', out_dir)
cap.release()