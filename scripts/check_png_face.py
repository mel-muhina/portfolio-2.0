import cv2

png = cv2.imread('/home/mmuhina/repo/port/portfolio-2.0/public/character.png')
h, w = png.shape[:2]
print(f"PNG size: {w}x{h}")
crop = png[int(h*0.3):int(h*0.6), int(w*0.5):int(w*0.8)]
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/png_face.jpg', crop)