---
layout: default
parent: Localization
title: Setup
nav_order: 1
permalink: localization/setup/

gh_link: docs/localization/1_setup.md
---

# Setup 

This is run on a Raspberry Pi computer. With the help of default Raspberry Pi camera, this codebase can act as the localization system of the hardware robots.

Please find the source code from [https://github.com/Pera-Swarm/localization](https://github.com/Pera-Swarm/localization)

----
Python repository for address the Localization problem of Swarm Robotics

### Requirements

Please install following pip packages if they aren't pre-installed

```bash
pip install numpy
pip install aruco
pip install paho-mqtt
pip3 install opencv-python
pip3 install opencv-contrib-python
pip3 install pyyaml
```

or use following command

```bash
pip install -r requirement.txt
```

### Initial Configurations

- First, copy __scripts/config-mapping_sample.yaml__ file and rename it as __scripts/config-mapping.yaml__
- Keep the default values at first, but later update while the mapping calibration process
- Next, copy __scripts/config-mqtt_sample.yaml__ file and rename it as __scripts/config-mqtt.yaml__ 
- Update following parameters with the actual values
  - mqtt_server
  - mqtt_port
  - mqtt_keepalive

### Run the scripts

- You can test the camera by running the script, __/scripts/pycamera.py__.
- The localization system can be started using the script, __scripts/script.py__.

<br/>

**NOTE**: You need to run the scripts only after move into the __/scripts__ directory, as following:

```bash
cd ./scripts 
python3 script.py
```

### Calibration 

You need to properly calibrate the camera to correctly map the identified coordinate values into the Mixed Reality environment. Please refer the guide in [here](/docs/localization/calibration) for details.

### Read More
- [ar-markers 0.5.0](https://pypi.org/project/ar-markers/)
- [Augmented Reality using ArUco Markers in OpenCV (C++ / Python)](https://www.learnopencv.com/augmented-reality-using-aruco-markers-in-opencv-c-python/)
- [OpenCV: Detection of ArUco Markers](https://docs.opencv.org/trunk/d5/dae/tutorial_aruco_detection.html)
- [OpenCV: Detection of ArUco Boards](https://docs.opencv.org/master/db/da9/tutorial_aruco_board_detection.html)
- [Calibrating the board](https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/sandbox/ludovic/aruco_calibration_rotation.html)
