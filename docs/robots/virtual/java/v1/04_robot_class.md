---
title: "Robot Class"
nav_order: 4
---

## Robot Class

This will guide the basic Methods available for a Java Virtual Robot implementations.

### Introduction

The Robot Class implements a collection of sensors, communication methods, output devices, Helper functions to emulate a real hardware robot in the virtual space.

```java
Robot(int id, double x, double y, double heading, char reality)
```

- `id`: id of the robot (unique in virtual and real)
- `x`: x coordinates on the arena
- `y`: y coordinates on the arena
- `heading`: The absolute angle of the robot from the positive direction of the x axis
- `reality`: specify whether real or virtual

Defines **robotMqttClient** for MQTT connection to create a robot instance in the Simulator.

### Sensors

Sensor modules are written with physical hardware implementations in mind. The Sensors available can be used as direct inputs in designing the robot logic.

#### DistanceSensor(Robot robot, RobotMqttClient m)

 DistanceSensor distSensor = new DistanceSensor(this, robotMqttClient);

##### getDistance()

Returns double type value for the distance of obstacle or robot in front.

```java
distSensor.getDistance()
```

###### Returns

- `Double`

###### Example Code

```java
// ProximitySensor(Robot robot, RobotMqttClient m)
ProximitySensor proximitySensor = new ProximitySensor(this, robotMqttClient);
```

##### getProximity()

Returns ProximityReadingType value indicating .......

```java
proximitySensor.getProximity();
```

###### Returns

- `swarm.robot.types.ProximityReadingType`

---

#### ColorSensor(Robot robot, RobotMqttClient m)

```java
ColorSensor colorSensor = new ColorSensor(this, robotMqttClient);
```

##### getColor()

Returns RGBColor type value indicating the color detected at the front of the robot.

```java
colorSensor.getColor()
```

###### Returns

- `swarm.robot.types.RGBColorType`

---

### Communication

#### SimpleCommunication(int robotId, RobotMqttClient m)

```java
SimpleCommunication simpleComm = new SimpleCommunication(id, robotMqttClient);
```

##### sendMessage(String msg, int distance)

Broadcasts message to robots within the defined radius.

```java
simpleComm.sendMessage(String msg, int distance);
simpleComm.sendMessage(String msg);
```

###### Parameters

- String `msg`: message to be passed
- int `distance`: radius that will receive the broadcasted message

###### Returns

- `Void`

#### DirectedCommunication(int robotId, RobotMqttClient m)

```java
DirectedCommunication directedComm = new DirectedCommunication(id, robotMqttClient);
```

##### sendMessage(String msg, int distance)

Sends a broadcast type message to robots at front within [-15,15] angle

```java
directedComm.sendMessage(String msg, int distance);
directedComm.sendMessage(String msg);
```

###### Parameters

- String `msg`: message to be passed
- int `distance`: radius that will receive the broadcasted message.

###### Returns

- `Void`

---

### Indicators

Indicators used signify various states of the robots.

#### NeoPixel(Robot robot, RobotMqttClient m)

```java
NeoPixel neoPixel = new NeoPixel(this, robotMqttClient);
```

##### changeColor(int r, int g, int b)

Used to change colors of the NeoPixel by inputting RGB values as integers.

```java
neoPixel.changeColor(int r,int g,int b);
```

###### Parameters

- int `r`: red
- int `g`: green
- int `b`: blue

###### Returns

- `Void`

---

### Helpers

Helper and Controller objects

#### Coordinate(int robotId, double x, double y, double heading, RobotMqttClient m)

```java
Coordinate coordinates = new Coordinate(int robotId, double x, double y, double heading, RobotMqttClient m);
```

##### getX()

Get x coordinate of the robot.

```java
coordinates.getX()
```

###### Returns

- `double`

##### getY()

Get y coordinate of the robot.

```java
coordinates.getY()
```

###### Returns

- `double`

##### setX(double x)

Set x coordinate of the robot.

```java
coordinates.setX(double x)
```

###### Parameters

- double `x`: x coordinate of the robot

###### Returns

- `Void`

##### setY(double y)

Set y coordinate of the robot.

```java
coordinates.setY(double y)
```

###### Parameters

- double `y`: y coordinate of the robot

###### Returns

- `Void`

##### getHeading()

Get heading of the robot.

```java
coordinates.getHeading()
```

###### Returns

- `double`

##### getHeadingRad()

Get heading of the robot in Radians.

```java
coordinates.getHeadingRad()
```

###### Returns

- `double`

##### setHeading(double heading)

Set heading of the robot.

```java
coordinates.setHeading(double heading)
```

###### Parameters

- double `heading`: heading of the robot

###### Returns

- `Void`

##### setHeadingRad(double heading)

Set heading of the robot in Radians.

```java
coordinates.setHeadingRad(double heading)
```

###### Parameters

- double `heading`: heading of the robot in Radians

###### Returns

- `Void`

##### setCoordinate(double x, double y, double heading)

Set x and y coordinates.

```java
coordinates.setCoordinate(double x, double y)
coordinates.setCoordinate(double x, double y, double heading)
```

###### Parameters

- double `x`: x coordinate
- double `y`: y coordinate
- double `heading`: heading of coordinate

###### Returns

- `Void`

##### toString()

return string of x , y and heading.

```java
coordinate.toString()
```

###### Parameters

- `Void`

###### Returns

- `String`

##### publishCoordinate()

Publish coordinate details under topic **localization/update**.

```java
coordinate.publishCoordinate()
```

###### Returns

- `Void`

#### MotionController(Coordinate c)

```java
MotionController motion = new MotionController(Communication(c));
```

##### rotate(int speed, int interval)

###### Description

Rotate virtual robot with a given speed and interval.

###### Syntax

```java
motion.rotate(int speed)
motion.rotate(int speed, int interval)
```

###### Parameters

 int speed : speed of rotation
 int interval : time interval for all steps to occur?

###### Returns

- `Void`

##### move(int leftSpeed, int rightSpeed, int interval)

Move virtual robot with a given speed and interval.

```java
motion.move(int leftSpeed, int rightSpeed, int interval)
motion.move(int leftSpeed, int rightSpeed)
```

###### Parameters

- int `leftSpeed`: speed of left motor
- int `rightSpeed`: speed of right motor
- int `interval`: time interval for all steps to occur

###### Returns

- `Void`

##### rotateDegree(int speed, float degree)

// To be implemented

##### moveDistance(int speed, float distance)

// To be implemented

##### goToGoal(double targetX, double targetY, int velocity)

Move virtual robot to defined location

```java
motion.gotoGoal(double targetX, int targetY, int velocity,in t interval )
motion.gotoGoal(double targetX, int targetY, int velocity)
```

###### Parameters

- double `targetX`: target x coordinate
- double `targetY`: target y coordinate
- int `velocity`: velocity of robot
- int `interval`: time interval for all steps to occur

###### Returns

- `boolean`

##### isSpeedInRange(int speed)

Check if given speed is in acceptable range (if speed within ROBOT_SPEED_MIN && ROBOT_SPEED_MAX).

```java
motion.isSpeedInRange(int speed)
```

###### Parameters

- int `speed`: Speed of the robot

###### Returns

- `boolean`

##### delay(int interval)

Delay to hold thread.

```java
motion.delay(int interval)
```

###### Parameters

- int `interval`: sleep for a defined interval

###### Returns

- `Void`

##### getSlope(double x1, double y1, double x2, double y2)

Angle in degrees between two points.

```java
motion.getSlop(idouble x1, double y1, double x2, double y2)
```

###### Parameters

- double `x1`: start x coordinate
- double `y1`: start y coordinate
- double `x2`: goal x coordinate
- double `y2`: goal y coordinate

###### Returns

- `double`

##### debug(String msg, int level)

### Miscellaneous

#### RobotMqtt(int robotId,RobotMqttClient mqtt, char reality)

```java
RobotMQTT robotMQTT = new RobotMqtt(int robotId,RobotMqttClient mqtt, char reality)
```

##### robotCreate(double x, double y, double heading)

Create a robot in the simulator.

```java
robotMQTT.robotCreate(double x, double y,double heading)
```

###### Parameters

- double `x`: position x coordinate
- double `y`: position y coordinate
- double `heading`: heading of the robot

###### Returns

- `Void`

##### subscribe(mqttTopic key, String topic)

Subscribe to a topic.

```java
robotMQTT.subscribe(mqttTopic key, String topic)
```

###### Parameters

- mqttTopic `key`: an enum value to identify the topic
- String `topic`: topic to subscribe

###### Returns

- `Void`

##### handleSubscription(Robot r, MqttMsg m)

Handle the mqtt subscription of the robots.

```java
robotMQTT.handleSubscription(Robot r, MqttMsg m)
```

###### Parameters

- Robot `r` : considered robot
- Mqttmsg `m`: topic and message (Calling out various functions through MQTT)

###### Returns

- `Void`
