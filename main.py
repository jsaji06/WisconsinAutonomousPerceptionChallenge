import os
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_file = "./dataset/bbox_light.csv"
df = pd.read_csv(csv_file)

def _num_from_name(name):
    match = re.search(r"(\d+)", name)
    return int(match.group(1)) if match else -1

# Sort depth files numerically by the index in the filename
depth_files = [f for f in os.listdir("./dataset/xyz") if f.endswith(".npz")]
depth_files.sort(key=_num_from_name)
depths = [os.path.join("./dataset/xyz", f) for f in depth_files]

rgb_files = [f for f in os.listdir("./dataset/rgb") if f.endswith(".png")]
rgb_files.sort(key=_num_from_name)
rgb_images = [os.path.join("./dataset/rgb", f) for f in rgb_files]

# Collect traffic light positions in ego frame
traffic_light_x = []
traffic_light_y = []

for i, row in df.iterrows():
    x1 = row['x1']
    y1 = row['y1']
    x2 = row['x2']
    y2 = row['y2']

    if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:

        width = x2 - x1
        height = y2 - y1

        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        if i < len(depths):
            depth_file = np.load(depths[i])
            depth_data = depth_file['xyz']
            data = depth_data[int(mid_y), int(mid_x)]
            x = data[0]
            y = data[1]
            z = data[2]
            if not np.isnan(x) and not np.isnan(y) and np.isfinite(x) and np.isfinite(y):
                traffic_light_x.append(x)
                traffic_light_y.append(y)

# Convert to world frame
if len(traffic_light_x) > 0:
    # Align first position to +X axis
    theta = np.arctan2(traffic_light_y[0], traffic_light_x[0])
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, s], [-s, c]])
    
    # Transform to world frame
    light_positions = np.array([traffic_light_x, traffic_light_y]).T
    light_world = (R @ light_positions.T).T
    
    # Ego position is negative of light position
    ego_world = -light_world
    
    # Set origin at traffic light
    ego_world = ego_world - ego_world[0]    
    
    # Create proper BEV plot
    plt.figure(figsize=(10, 10))
    plt.plot(ego_world[:, 0], ego_world[:, 1], 'b-', linewidth=2, label='Ego Trajectory')
    plt.scatter(ego_world[0, 0], ego_world[0, 1], color='green', s=100, label='Start', marker='o')
    plt.scatter(ego_world[-1, 0], ego_world[-1, 1], color='red', s=100, label='End', marker='s')
    plt.scatter(0, 0, color='orange', s=150, label='Traffic Light', marker='^')
    
    # BEV formatting
    plt.xlabel('X (meters)')
    plt.ylabel('Y (meters)')
    plt.title('Bird\'s Eye View - Ego Vehicle Trajectory')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')  # Equal aspect ratio for proper BEV
    plt.gca().invert_yaxis()  # Invert Y axis so +Y points up (standard BEV convention)
    plt.savefig("trajectory.png")

    