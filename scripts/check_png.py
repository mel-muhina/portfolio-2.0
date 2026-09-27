import cv2

png = cv2.imread('/home/mmuhina/repo/port/portfolio-2.0/public/character.png')
print("PNG shape:", png.shape)
f225 = cv2.imread('/home/mmuhina/repo/port/portfolio-2.0/public/frames/center.webp')

# Compare PNG and frame 225
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/check_png.jpg', cv2.resize(png, (320, 180)))