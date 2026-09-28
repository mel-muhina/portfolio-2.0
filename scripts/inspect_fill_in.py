import cv2

mp4_path = '/home/mmuhina/repo/port/portfolio-2.0/public/character-up.mp4'
cap = cv2.VideoCapture(mp4_path)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frames = []
for _ in range(total):
    ok, f = cap.read()
    if not ok: break
    frames.append(f)
cap.release()
print("total frames:", total)

# Labeled contact sheet, every 2nd frame for fine detail near the top arc
tiles = []
for i in range(0, total, 2):
    img = cv2.resize(frames[i], (192, 108))
    cv2.putText(img, str(i), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    tiles.append(img)
cols = 6
rows = [cv2.hconcat(tiles[r*cols:(r+1)*cols]) for r in range((len(tiles)+cols-1)//cols)]
# pad last row if needed
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/fillin_sheet.jpg', cv2.vconcat(rows))
print("saved fillin_sheet.jpg")
