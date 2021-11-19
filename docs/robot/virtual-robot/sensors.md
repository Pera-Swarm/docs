---
layout: default
parent: Virtual Robot
grand_parent: Robots
title: Robot Class Overview
nav_order: 4
permalink: robot/virtual-robot/sensors

gh_link: docs/robot/virtual-robot/sensors.md
---


# Sensors

Virtual robots are used to emulate real world physical robot behaviours. Hence Sensor modules are written with physical hardware implementations in mind. The Sensors available can be used as direct inputs in designing the robot logic.


## DistanceSensor(Robot robot, RobotMqttClient m) 


### getDistance() -> double
Returns double type value for the distance of obstacle or robot in front.
    
## ProximitySensor(Robot robot, RobotMqttClient m) 

### getProximity() -> double

## ColorSensor(Robot robot, RobotMqttClient m) 

### getColor() -> RGBColorType
