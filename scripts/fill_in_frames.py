# fillin_frames.py
import cv2

NEW_VIDEO = '/home/mmuhina/repo/port/portfolio-2.0/public/character-up.mp4'  # <-- set this
OUT = '/home/mmuhina/repo/port/portfolio-2.0/public/frames'

cap = cv2.VideoCapture(NEW_VIDEO)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frames = []
for _ in range(total):
    ok, f = cap.read()
    if not ok: break
    frames.append(f)
cap.release()

webp = [cv2.IMWRITE_WEBP_QUALITY, 95]  # match your existing quality

# Map: destination slot index -> source frame number in the NEW video.
# Fill in these numbers from fillin_sheet.jpg (Step 2).
fill_map = {
    64: 188,   # <-- replace with real source frame numbers
    65: 192,
    66: 194,
}

for slot, src in fill_map.items():
    frame = frames[src]
    cv2.imwrite(f"{OUT}/frame_{slot}.webp", frame, webp)
    cv2.imwrite(f"{OUT}/{slot}.webp", frame, webp)   # keep the duplicate naming too
    print(f"slot {slot} <- new video frame {src}")

print("Done. Only slots", list(fill_map.keys()), "were overwritten.")
