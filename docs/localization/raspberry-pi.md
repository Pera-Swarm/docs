---
layout: default
parent: Localization
title: Paspberry Pi
nav_order: 1
permalink: localization/raspberry-pi

gh_link: docs/localization/raspberry-pi.md
---

This is run on a Raspberry Pi computer. With the help of default Raspberry Pi camera, this codebase can act as the localization system of the hardware robots.

Please find the source code from [https://github.com/Pera-Swarm/localization](https://github.com/Pera-Swarm/localization)

----
Python repository for address the Localization problem of Swarm Robotics

### Requirements

Please install following pip packages if they aren't pre-installed

```
pip install numpy
pip install opencv-python
pip install aruco
pip install paho-mqtt
```

or use following command

```
pip install -r requirement.txt
```

### Run the scripts

You can try scripts on the ./scripts directory

### Read More
- [ar-markers 0.5.0](https://pypi.org/project/ar-markers/)
- [Augmented Reality using ArUco Markers in OpenCV (C++ / Python)](https://www.learnopencv.com/augmented-reality-using-aruco-markers-in-opencv-c-python/)
- [OpenCV: Detection of ArUco Markers](https://docs.opencv.org/trunk/d5/dae/tutorial_aruco_detection.html)
- [OpenCV: Detection of ArUco Boards](https://docs.opencv.org/master/db/da9/tutorial_aruco_board_detection.html)
- [Calibrating the board](https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/sandbox/ludovic/aruco_calibration_rotation.html)
