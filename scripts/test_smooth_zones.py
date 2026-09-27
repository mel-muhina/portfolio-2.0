import math

w, h = 1920, 1080
faceX = w * 0.60
faceY = h * 0.42

def clamp(val, min_v, max_v):
    return max(min_v, min(max_v, val))

def compute_frame_smooth(mx, my):
    u = (mx - faceX) / (w * 0.45)
    v = (my - faceY) / (h * 0.45)
    
    # 1. Nav bar / Top zone: pull u towards center (so character looks UP)
    # Active when v is negative (top of screen) and u is in the navbar range
    top_weight = clamp((-v - 0.15) / 0.45, 0.0, 1.0)
    nav_center_weight = clamp(1.0 - abs(u + 0.18) / 0.75, 0.0, 1.0)
    pull_top = top_weight * nav_center_weight * 0.80
    adj_u = u * (1.0 - pull_top)
    
    # 2. Directly below / Bottom zone: pull u towards center (so character looks DOWN)
    # Active when v is positive (bottom of screen) and u is near vertical line below face/center
    bottom_weight = clamp((v - 0.20) / 0.50, 0.0, 1.0)
    bottom_center_weight = clamp(1.0 - abs(u + 0.10) / 0.70, 0.0, 1.0)
    pull_bottom = bottom_weight * bottom_center_weight * 0.80
    adj_u = adj_u * (1.0 - pull_bottom)
    
    # 3. Far right edge: pull v towards 0 (so character looks RIGHT)
    # Active when u is positive (far right) and cursor is not at extreme top/bottom
    right_weight = clamp((u - 0.35) / 0.45, 0.0, 1.0)
    right_mid_weight = clamp(1.0 - abs(v) / 0.70, 0.0, 1.0)
    pull_right = right_weight * right_mid_weight * 0.75
    adj_v = v * (1.0 - pull_right)
    
    angle = math.atan2(adj_v, -adj_u) + math.pi / 2
    if angle < 0: angle += 2 * math.pi
    norm = angle % (2 * math.pi)
    frame_idx = int(round((norm / (2 * math.pi)) * 64)) % 64
    return frame_idx, u, v

print('--- NAV BAR / TOP AREA (y=40) ---')
for x in [100, 300, 500, 700, 960, 1152, 1350, 1550, 1750, 1880]:
    f, u, v = compute_frame_smooth(x, 40)
    print(f'x={x:4d}, y= 40: Frame #{f:2d} (u={u:+.2f}, v={v:+.2f})')

print('\n--- DIRECTLY BELOW / BOTTOM AREA (y=950) ---')
for x in [300, 500, 700, 960, 1152, 1350, 1550, 1750, 1880]:
    f, u, v = compute_frame_smooth(x, 950)
    print(f'x={x:4d}, y=950: Frame #{f:2d} (u={u:+.2f}, v={v:+.2f})')

print('\n--- FAR RIGHT SIDE (x=1850) ---')
for y in [40, 150, 250, 350, 450, 550, 650, 750, 850, 1000]:
    f, u, v = compute_frame_smooth(1850, y)
    print(f'x=1850, y={y:4d}: Frame #{f:2d} (u={u:+.2f}, v={v:+.2f})')

print('\n--- LEFT SIDE / BIO (x=350) ---')
for y in [100, 250, 400, 500, 600, 750, 900]:
    f, u, v = compute_frame_smooth(350, y)
    print(f'x=350, y={y:4d}: Frame #{f:2d} (u={u:+.2f}, v={v:+.2f})')

