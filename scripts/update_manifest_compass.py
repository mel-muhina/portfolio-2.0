import json

path = '/home/mmuhina/repo/port/portfolio-2.0/public/frames/manifest.json'
with open(path, 'r') as f:
    data = json.load(f)

data["compass_frame_indices"] = {
    "slightly_up": 0,
    "upper_right": 56,
    "slightly_right": 48,
    "lower_right": 40,
    "slightly_down": 32,
    "lower_left": 24,
    "slightly_left": 16,
    "upper_left": 8
}

with open(path, 'w') as f:
    json.dump(data, f, indent=2)

print("Updated manifest.json")