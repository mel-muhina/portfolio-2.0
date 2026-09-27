import math

w, h = 1920, 1080
faceX = w * 0.60
faceY = h * 0.42

def compute_frame(mx, my):
    # Normalized offset from face center
    u = (mx - faceX) / (w * 0.45)
    v = (my - faceY) / (h * 0.45)
    
    adj_u = u
    adj_v = v
    
    # 1. Nav bar area (v is negative / top of screen):
    # Across the top bar, user wants character to look UP (frame 0)
    # until they move into the far corners.
    if v < -0.35:
        # If between far-left and far-right of top
        if -0.8 < u < 0.5:
            # Dampen horizontal deviation so gaze is directed UP
            # Stronger dampening near the center of the nav bar
            factor = 0.25 if -0.5 < u < 0.3 else 0.45
            adj_u = u * factor

    # 2. Directly below (v is positive / bottom of screen):
    # User feedback: 'the character looks to the right too quickly when the cursor is still directly below'
    # Dampen horizontal deviation when cursor is in bottom area
    if v > 0.35:
        if -0.6 < u < 0.6:
            adj_u = u * 0.25 # keep gaze firmly looking DOWN (frame 32)

    # 3. Far right edge:
    # User feedback: 'she looks up to the right top too quickly when the cursor is still far right'
    # Dampen vertical deviation unless genuinely in the top or bottom corner
    if u > 0.45:
        if -0.6 < v < 0.45:
            adj_v = v * 0.30 # keep gaze looking RIGHT (frame 48)

    angle = math.atan2(adj_v, -adj_u) + math.pi / 2
    if angle < 0: angle += 2 * math.pi
    norm = angle % (2 * math.pi)
    frame_idx = int(round((norm / (2 * math.pi)) * 64)) % 64
    return frame_idx, u, v

print('--- NAV BAR / TOP AREA (y=40) ---')
for x in [100, 300, 600, 800, 960, 1152, 1350, 1550, 1750, 1880]:
    f, u, v = compute_frame(x, 40)
    print(f'x={x:4d}, y= 40: Frame #{f:2d} (u={u:+.2f}, v={v:+.2f})')

print('\n--- DIRECTLY BELOW / BOTTOM AREA (y=950) ---')
for x in [300, 600, 800, 960, 1152, 1350, 1500, 1700, 1880]:
    f, u, v = compute_frame(x, 950)
    print(f'x={x:4d}, y=950: Frame #{f:2d} (u={u:+.2f}, v={v:+.2f})')

print('\n--- FAR RIGHT SIDE (x=1850) ---')
for y in [40, 150, 250, 350, 450, 550, 650, 750, 850, 1000]:
    f, u, v = compute_frame(1850, y)
    print(f'x=1850, y={y:4d}: Frame #{f:2d} (u={u:+.2f}, v={v:+.2f})')


print('\n--- LEFT SIDE / BIO & BUTTONS (x=350) ---')
for y in [100, 250, 400, 500, 600, 750, 900]:
    f, u, v = compute_frame(350, y)
    print(f'x=350, y={y:4d}: Frame #{f:2d} (u={u:+.2f}, v={v:+.2f})')

