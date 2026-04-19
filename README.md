# Triangle Line and Corner Detection using OpenCV

## Objective
To detect lines and corners of an equilateral triangle using OpenCV and analyze the effect of planar and non-planar surfaces under different lighting conditions.

## Tools Used
- Python
- OpenCV
- NumPy
- Webcam

## Setup Instructions
1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install opencv-python numpy

3. Run the script:
   python3 task1_triangle_detection.py

## Methodology
- Convert frame to grayscale
- Apply Gaussian blur
- Perform edge detection using Canny
- Detect lines using Hough Transform
- Detect corners using Shi-Tomasi method

## Results

### Planar Surface
![Planar Normal](samples/planar_normal_detection.png)

![Planar Lighting](samples/planar_variable_lighting.png)

![Planar Low Light](samples/planar_low_light_detection.png)

### Non-Planar Surface
![Non Planar](samples/non_planar_triangle_detection.png)

## Observations

### Planar Surface
Edges were detected clearly and continuously. Corners were stable and close to actual triangle vertices. Detection worked well under different lighting conditions.

### Non-Planar Surface
Due to curvature, triangle edges appeared distorted. Line detection became fragmented and corners were less stable.

## Camera Parameters

### Intrinsic Parameters
Internal camera properties such as focal length and lens distortion affect how the triangle appears in the image.

### Extrinsic Parameters
Camera position and orientation affect how the triangle is viewed.

## Conclusion
Detection works better on planar surfaces and is affected by distortion on curved surfaces.

## Author
Parnika Sahu
