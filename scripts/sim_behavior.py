import cv2
import numpy as np

OUTPUT_DIR = '/home/mmuhina/repo/port/portfolio-2.0/public/frames'
frames_72 = [cv2.imread(f"{OUTPUT_DIR}/frame_{i}.webp") for i in range(72)]
transitions = [cv2.imread(f"{OUTPUT_DIR}/transition_{i}.webp") for i in range(9)]
center = cv2.imread(f"{OUTPUT_DIR}/center.webp")

class SimTracker:
    def __init__(self):
        self.mode = 'CENTER'
        self.currentRotationIndex = 0
        self.transitionStep = 8
        self.smoothedAngle = 0
        self.tick_count = 0
        
    def step(self, mouse_dist, target_angle, is_out_of_view):
        # Hysteresis
        enter_radius = 80
        exit_radius = 140
        
        want_center = is_out_of_view or (mouse_dist <= enter_radius)
        want_track = (not is_out_of_view) and (mouse_dist > exit_radius)
        
        if self.mode == 'CENTER':
            if want_track:
                self.mode = 'FROM_CENTER'
                self.transitionStep = 8
            img = center
            
        elif self.mode == 'FROM_CENTER':
            if want_center:
                self.mode = 'TO_CENTER'
            else:
                self.transitionStep -= 1
                if self.transitionStep <= 0:
                    self.transitionStep = 0
                    self.currentRotationIndex = 0
                    self.smoothedAngle = 0
                    self.mode = 'TRACKING'
            img = transitions[max(0, min(8, self.transitionStep))]
            
        elif self.mode == 'TRACKING':
            if want_center:
                self.mode = 'TO_UP'
            else:
                # lerp angle
                diff = (target_angle - self.smoothedAngle) % (2 * np.pi)
                if diff < -np.pi: diff += 2 * np.pi
                if diff > np.pi: diff -= 2 * np.pi
                self.smoothedAngle += diff * 0.24
                
                norm = self.smoothedAngle % (2 * np.pi)
                if norm < 0: norm += 2 * np.pi
                self.currentRotationIndex = int(round((norm / (2 * np.pi)) * 72)) % 72
            img = frames_72[self.currentRotationIndex]
            
        elif self.mode == 'TO_UP':
            if want_track:
                self.mode = 'TRACKING'
                img = frames_72[self.currentRotationIndex]
            else:
                # Step towards 0
                dist_cw = (72 - self.currentRotationIndex) % 72
                dist_ccw = self.currentRotationIndex
                if dist_cw <= dist_ccw:
                    self.currentRotationIndex = (self.currentRotationIndex + 2) % 72
                    if self.currentRotationIndex < 2:
                        self.currentRotationIndex = 0
                else:
                    self.currentRotationIndex = (self.currentRotationIndex - 2 + 72) % 72
                    if self.currentRotationIndex > 70:
                        self.currentRotationIndex = 0
                        
                img = frames_72[self.currentRotationIndex]
                if self.currentRotationIndex == 0:
                    self.mode = 'TO_CENTER'
                    self.transitionStep = 0
                    
        elif self.mode == 'TO_CENTER':
            if want_track:
                self.mode = 'FROM_CENTER'
            else:
                self.transitionStep += 1
                if self.transitionStep >= 8:
                    self.transitionStep = 8
                    self.mode = 'CENTER'
            img = transitions[max(0, min(8, self.transitionStep))]
            
        return img, self.mode

tracker = SimTracker()

# Simulate scenario:
# 1. Start at center (10 frames)
# 2. Mouse moves to LEFT (dist = 300, angle = 270 deg = 3*pi/2) for 30 frames
# 3. Mouse moves into MIDDLE (dist = 40) for 30 frames
# 4. Mouse moves to RIGHT (dist = 300, angle = 90 deg = pi/2) for 30 frames
# 5. Mouse LEAVES WINDOW (is_out_of_view = True) for 40 frames

sim_frames = []
modes = []

# 1. Center
for _ in range(10):
    img, m = tracker.step(40, 0, False)
    sim_frames.append(img)
    modes.append(m)
    
# 2. To Left
for _ in range(30):
    img, m = tracker.step(300, 3 * np.pi / 2, False)
    sim_frames.append(img)
    modes.append(m)

# 3. Move into middle
for _ in range(30):
    img, m = tracker.step(40, 3 * np.pi / 2, False)
    sim_frames.append(img)
    modes.append(m)

# 4. Move to Right
for _ in range(30):
    img, m = tracker.step(300, np.pi / 2, False)
    sim_frames.append(img)
    modes.append(m)

# 5. Mouse leaves window
for _ in range(40):
    img, m = tracker.step(300, np.pi / 2, True)
    sim_frames.append(img)
    modes.append(m)

print(f"Total simulated frames: {len(sim_frames)}")

# Sample 16 key points across the simulation to create a storyboard
step_size = len(sim_frames) // 16
storyboard_imgs = [cv2.resize(sim_frames[i * step_size], (160, 90)) for i in range(16)]

# 2 rows of 8
row1 = cv2.hconcat(storyboard_imgs[:8])
row2 = cv2.hconcat(storyboard_imgs[8:])
grid = cv2.vconcat([row1, row2])
cv2.imwrite('/home/mmuhina/repo/port/portfolio-2.0/scripts/sim_storyboard.jpg', grid)
print("Saved sim_storyboard.jpg")
