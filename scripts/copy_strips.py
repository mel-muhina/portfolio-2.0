import cv2

# Copy strips to brain directory for inspection
import shutil

for s in ["strip_UP_start.jpg", "strip_RIGHT.jpg", "strip_DOWN.jpg", "strip_LEFT.jpg", "strip_UP_end.jpg", "strip_TRANS_TO_CENTER.jpg", "strip_CENTER.jpg"]:
    shutil.copy(f"/home/mmuhina/repo/port/portfolio-2.0/scripts/{s}", f"/home/mmuhina/repo/port/portfolio-2.0/public/{s}")
print("Copied to public")