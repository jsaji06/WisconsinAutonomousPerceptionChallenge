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

## Algorithm

1. **Data Collection**: Extract traffic light 3D positions from depth maps
   - Iterate through each frame's traffic light bounding box data
   - Calculate midpoint to identify proper indices to retrieve depth data per frame
   - Retrieve and collect depth data of traffic light per frame
2. **Frame Alignment**: Rotate coordinates so initial traffic light position aligns with +X axis
   - Project onto the positive X axis since the car moves in that same direction (forward)
   - Then rotate coordinates to convert to world frame
3. **Visualization**: Plot trajectory in BEV format
   - Using the newly calculated coordinates, create a scatterplot visual of the coordinates

## Output

- **trajectory.png**: Static BEV plot showing ego-vehicle trajectory
- **Key**:
  - Blue line: Ego trajectory
  - Green circle: Start position
  - Red square: End position
  - Orange triangle: Traffic light (world origin)

## Results
The system successfully tracks the ego-vehicle's trajectory in a fixed world frame, providing a clear Bird's Eye View of the vehicle's path relative to the traffic light reference point.

