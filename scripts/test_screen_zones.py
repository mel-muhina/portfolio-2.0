import math

w, h = 1920, 1080
faceX = w * 0.60
faceY = h * 0.42

def compute_frame(mx, my):
    # Normalized offset
    u = (mx - faceX) / (w * 0.45)
    v = (my - faceY) / (h * 0.45)
    
    # If in upper zone (navbar area), widen UP sector by dampening u
    adj_u = u
    adj_v = v
    
    # 1. Nav bar area (v is negative / top of screen):
    # If cursor is near top of screen (v < -0.4), widen UP sector
    if v < -0.4:
        # soften u towards 0 unless u is very far left/right
        if -0.7 < u < 0.4:
            adj_u = u * 0.35 # pull towards center so she looks UP!
            
    # 2. Directly below (v is positive / bottom of screen):
    # If cursor is near bottom of screen (v > 0.4), widen DOWN sector
    if v > 0.4:
        if -0.5 < u < 0.5:
            adj_u = u * 0.35 # pull towards center so she looks DOWN!
            
    # 3. Far right (u is positive):
    # Don't look up-right unless cursor is genuinely in upper-right corner
    if u > 0.5 and -0.5 < v < 0.4:
        adj_v = v * 0.4 # pull towards horizontal so she looks RIGHT!
        
    # Compute angle with mirrored horizontal (-adj_u)
    angle = math.atan2(adj_v, -adj_u) + math.pi / 2
    if angle < 0: angle += 2 * math.pi
    norm = angle % (2 * math.pi)
    frame_idx = int(round((norm / (2 * math.pi)) * 64)) % 64
    return frame_idx

test_points = {
    "Nav Bar (top center)": (960, 40),
    "Directly below": (1200, 950),
    "Directly below slightly right": (1350, 950),
    "Far right (level with eyes)": (1850, 450),
    "Far right (slightly up)": (1850, 350),
    "Upper-Right corner": (1880, 40),
    "Upper-Left corner": (50, 40),
    "Lower-Left corner": (100, 1000),
    "Lower-Right corner": (1880, 1000),
    "Left side (bio)": (350, 500)
}

# Key frame reference:
# 0: UP
# 8: UPPER-LEFT
# 16: LEFT
# 24: LOWER-LEFT
# 32: DOWN
# 40: LOWER-RIGHT
# 48: RIGHT
# 56: UPPER-RIGHT

for name, (mx, my) in test_points.items():
    idx = compute_frame(mx, my)
    print(f"{name:32}: Frame #{idx:2d}")