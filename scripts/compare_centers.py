import math

def run_test(fx_pct, fy_pct):
    w, h = 1920, 1080
    faceX = w * fx_pct
    faceY = h * fy_pct
    def clamp(val, min_v, max_v): return max(min_v, min(max_v, val))
    
    def compute(mx, my):
        u = (mx - faceX) / (w * 0.45)
        v = (my - faceY) / (h * 0.45)
        top_weight = clamp((-v - 0.15) / 0.45, 0.0, 1.0)
        nav_center_weight = clamp(1.0 - abs(u + 0.18) / 0.75, 0.0, 1.0)
        pull_top = top_weight * nav_center_weight * 0.80
        adj_u = u * (1.0 - pull_top)
        bottom_weight = clamp((v - 0.20) / 0.50, 0.0, 1.0)
        bottom_center_weight = clamp(1.0 - abs(u + 0.10) / 0.70, 0.0, 1.0)
        pull_bottom = bottom_weight * bottom_center_weight * 0.80
        adj_u = adj_u * (1.0 - pull_bottom)
        right_weight = clamp((u - 0.35) / 0.45, 0.0, 1.0)
        right_mid_weight = clamp(1.0 - abs(v) / 0.70, 0.0, 1.0)
        pull_right = right_weight * right_mid_weight * 0.75
        adj_v = v * (1.0 - pull_right)
        angle = math.atan2(adj_v, -adj_u) + math.pi / 2
        if angle < 0: angle += 2 * math.pi
        norm = angle % (2 * math.pi)
        return int(round((norm / (2 * math.pi)) * 64)) % 64
        
    print(f'=== fx={fx_pct}, fy={fy_pct} ===')
    for name, (x, y) in [
        ('Navbar Left (700, 40)', (700, 40)),
        ('Navbar Mid (960, 40)', (960, 40)),
        ('Navbar Right (1350, 40)', (1350, 40)),
        ('Below Center (1152, 950)', (1152, 950)),
        ('Below Screen Mid (960, 950)', (960, 950)),
        ('Far Right Mid (1850, 450)', (1850, 450)),
        ('Far Right Upper (1850, 250)', (1850, 250)),
        ('Top Right Corner (1880, 40)', (1880, 40)),
        ('Top Left Corner (100, 40)', (100, 40)),
    ]:
        print(f'{name:30}: Frame #{compute(x, y):2d}')

run_test(0.60, 0.42)
print()
run_test(0.64, 0.43)
