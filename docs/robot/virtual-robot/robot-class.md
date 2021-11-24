---
layout: default
parent: Virtual Robot
grand_parent: Robots
title: Robot Class Overview
nav_order: 3
permalink: robot/virtual-robot/robot-class

gh_link: docs/robot/virtual-robot/robot-class.md
---

# Robot Class
{: .no_toc }

### Table of content
{: .no_toc }
- TOC
{:toc}

---

## Introduction

## Sensors

Virtual robots are used to emulate real world physical robot behaviours. Hence Sensor modules are written with physical hardware implementations in mind. The Sensors available can be used as direct inputs in designing the robot logic.


### DistanceSensor(Robot robot, RobotMqttClient m) 


#### getDistance() -> double
Returns double type value for the distance of obstacle or robot in front.
    
### ProximitySensor(Robot robot, RobotMqttClient m) 

#### getProximity() -> double

### ColorSensor(Robot robot, RobotMqttClient m) 

#### getColor() -> RGBColorType



## Communication

### DirectedCommunication(int robotId, RobotMqttClient m)




### SimpleCommunication(int robotId, RobotMqttClient m)


## Indicators

Indicators used signify various states of the robots. 

### NeoPixel(Robot robot, RobotMqttClient m)


#### changeColor(int r, int g, int b)
Used to change colors of the neopixel by inputing RGB values as integers.




## Helpers


### Coordinate(int robotId, double x, double y, double heading, RobotMqttClient m)

#### getX()

#### getY()

#### setX(double x)

#### setY(double y)

#### getHeading()

#### getHeadingRad()

#### setHeading(double heading)

#### setHeadingRad(double heading)

#### setCoordinate(double x, double y)


#### setCoordinate(double x, double y, double heading)



