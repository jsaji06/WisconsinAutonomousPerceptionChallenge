# Ego-Vehicle Trajectory Tracking

This project implements a Bird's Eye View (BEV) trajectory tracking system for an autonomous vehicle using traffic light detection and depth estimation.

## Overview

The system tracks the ego-vehicle's trajectory by:
1. Detecting traffic light bounding boxes in RGB frames
2. Extracting 3D coordinates from corresponding depth maps
3. Transforming coordinates to a world frame with the traffic light as reference
4. Visualizing the trajectory in a Bird's Eye View

## Coordinate Systems

### Camera/Ego Frame
- +X: Forward (car heading direction)
- +Y: Right
- +Z: Up

### World Frame
- Origin: Directly under traffic light on ground
- +X: Aligned with initial car-traffic light line
- +Y: Left (perpendicular to +X)
- +Z: Up (since we are only worried about 2D trajectories, this is ignored)

## Algorithm

1. **Data Collection**: Extract traffic light 3D positions from depth maps
3. **Frame Alignment**: Rotate coordinates so initial traffic light position aligns with +X axis
4. **World Transformation**: Convert to world frame (ego position = -traffic light position)
5. **Origin Setting**: Set world origin at traffic light location
6. **Visualization**: Plot trajectory in BEV format

## Output

- **trajectory.png**: Static BEV plot showing ego-vehicle trajectory
- **Key**:
  - Blue line: Ego trajectory
  - Green circle: Start position
  - Red square: End position
  - Orange triangle: Traffic light (world origin)

## Results
The system successfully tracks the ego-vehicle's trajectory in a fixed world frame, providing a clear Bird's Eye View of the vehicle's path relative to the traffic light reference point.

