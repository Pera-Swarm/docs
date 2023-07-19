---
layout: default
parent: Firmware
grand_parent: Virtual Robots
title: Robot Class Overview
nav_order: 3
permalink: robots/virtual/firmware/v1/robot-class/

gh_link: docs/robots/virtual/v1/firmware/3_robot-class.md
---

# Robot Class
{: .no_toc }

### Table of content
{: .no_toc }
- TOC
{:toc}

---


{% assign sub_color = "color: orange;" %}

## Introduction
The Robot Class implements a collection of sensors, communication methods, output devices, Helper functions to emulate a real hardware robot in the virtual space.

### Robot(int id, double x, double y, double heading, char reality)

	id      - id of the robot (unique in virtual and real)
	x       - x cordinates on the arena
	y       - y cordinates on the arena
	heading - The absolute angle of the robot from the positive direction of the x axis 
	reality - specify whether real or virtual


Defines <b>robotMqttClient</b> for MQTT connection to create a robot instance in the Simulator.


## Sensors

Sensor modules are written with physical hardware implementations in mind. The Sensors available can be used as direct inputs in designing the robot logic.


### DistanceSensor(Robot robot, RobotMqttClient m) 
	
	DistanceSensor distSensor = new DistanceSensor(this, robotMqttClient);

#### getDistance()

<span style="{{ sub_color }}">Description</span>

Returns double type value for the distance of obstacle or robot in front.
    
<span style="{{ sub_color }}">Syntax</span>
 
	distSensor.getDistance() 

<span style="{{ sub_color }}">Parameter</span>

None

<span style="{{ sub_color }}">Returns</span>

Double 

<span style="{{ sub_color }}">Example Code</span>

<!-- Shall we add some code snippet like this for each method -->

{% highlight java %}
package robotImplementations;
import swarm.robot.VirtualRobot;
public class ObstacleAvoidRobot extends VirtualRobot {

    public ObstacleAvoidRobot(int id, double x, double y, double heading) {
        super(id, x, y, heading);
    }

    public void setup() {
        super.setup();
    }

    public void loop() throws Exception {
        super.loop();

        if(state==robotState.RUN) {
            double dist = distSensor.getDistance();

            if (dist < 15) {

                // Generate a random number in [-1000,1000] range
                // if even, rotate CW, otherwise rotate CCW an angle depends on the random number
                int random = -1000 + ((int) ((Math.random() * 2000)));
                int sign = (random % 2 == 0) ? 1 : -1;

                System.out.println("\t Wall detected, go back and rotate " + ((sign > 0) ? "CW" : "CCW"));

                // Go back a little
                motion.move(-100, -100, 900);

                // rotate
                int loopCount = 0; // to avoid infinity loop
                while (distSensor.getDistance() < 35 && loopCount < 5) {
                    motion.rotate(50 * sign, 1000);
                    loopCount++;
                }
                // TODO: This is a temp update to restrict the robot into arena
                // if (coordinates.getX() >= 90) coordinates.setX(85);
                // if (coordinates.getX() <= -90) coordinates.setX(-85);
                // if (coordinates.getY() >= 90) coordinates.setY(85);
                // if (coordinates.getY() <= -90) coordinates.setY(-85);

                // rotate a little
                motion.rotate(50 * sign, 500);

            } else {
                motion.move(100, 100, 1000);
            }
        }
    }
}
{% endhighlight %}


### ProximitySensor(Robot robot, RobotMqttClient m) 

    ProximitySensor proximitySensor = new ProximitySensor(this, robotMqttClient);

#### getProximity()

<span style="{{ sub_color }}">Description</span>

Returns ProximityReadingType value indicating .......
    
<span style="{{ sub_color }}">Syntax</span>

	proximitySensor.getProximity();

<span style="{{ sub_color }}">Parameter</span>

None

<span style="{{ sub_color }}">Returns</span>

swarm.robot.types.ProximityReadingType

### ColorSensor(Robot robot, RobotMqttClient m) 

    ColorSensor colorSensor = new ColorSensor(this, robotMqttClient);

#### getColor() 

<span style="{{ sub_color }}">Description</span>

Returns RGBColor type value indicating the color detected at the front of the robot.
    
<span style="{{ sub_color }}">Syntax</span>
 
	colorSensor.getColor() 

<span style="{{ sub_color }}">Parameter</span>

None

<span style="{{ sub_color }}">Returns</span>

swarm.robot.types.RGBColorType 

## Communication


### SimpleCommunication(int robotId, RobotMqttClient m)

	SimpleCommunication simpleComm = new SimpleCommunication(id, robotMqttClient);

#### sendMessage(String msg, int distance)


<span style="{{ sub_color }}">Description</span>

Broadcasts message to robots within the defined radius.

<span style="{{ sub_color }}">Syntax</span>
 
	simpleComm.sendMessage(String msg, int distance);
	simpleComm.sendMessage(String msg);


<span style="{{ sub_color }}">Parameter</span>

	String msg   : message to be passed
	int distance : radius that will receive the broadcasted message

<span style="{{ sub_color }}">Returns</span>

Void


### DirectedCommunication(int robotId, RobotMqttClient m)

    DirectedCommunication directedComm = new DirectedCommunication(id, robotMqttClient);

#### sendMessage(String msg, int distance)


<span style="{{ sub_color }}">Description</span>

Sends a broadcast type message to robots at front within [-15,15] angle

<span style="{{ sub_color }}">Syntax</span>
 
	directedComm.sendMessage(String msg, int distance);
	directedComm.sendMessage(String msg);


<span style="{{ sub_color }}">Parameter</span>

	String msg   : message to be passed
	int distance : radius that will receive the broadcasted message.

<span style="{{ sub_color }}">Returns</span>

Void
## Indicators
Indicators used signify various states of the robots. 


### NeoPixel(Robot robot, RobotMqttClient m)

	NeoPixel neoPixel = new NeoPixel(this, robotMqttClient);

#### changeColor(int r, int g, int b)

<span style="{{ sub_color }}">Description</span>

Used to change colors of the neopixel by inputing RGB values as integers.

<span style="{{ sub_color }}">Syntax</span>
 
	neoPixel.changeColor(int r,int g,int b);

<span style="{{ sub_color }}">Parameter</span>

	int r : red 
	int g : green
	int b : blue

<span style="{{ sub_color }}">Returns</span>

Void




## Helpers

Helper and Controller objects

### Coordinate(int robotId, double x, double y, double heading, RobotMqttClient m)

    Coordinate coordinates = new Coordinate(int robotId, double x, double y, double heading, RobotMqttClient m);

#### getX()

<span style="{{ sub_color }}">Description</span>

Get x coordinate of the robot.


<span style="{{ sub_color }}">Syntax</span>

	cordinates.getX()

<span style="{{ sub_color }}">Parameter</span>

None

<span style="{{ sub_color }}">Returns</span>

double

#### getY()

<span style="{{ sub_color }}">Description</span>

Get y coordinate of the robot.


<span style="{{ sub_color }}">Syntax</span>

	cordinates.getY()

<span style="{{ sub_color }}">Parameter</span>

None

<span style="{{ sub_color }}">Returns</span>

double

#### setX(double x)

<span style="{{ sub_color }}">Description</span>

Set x coordinate of the robot.


<span style="{{ sub_color }}">Syntax</span>

	cordinates.setX(double x)

<span style="{{ sub_color }}">Parameter</span>

double

<span style="{{ sub_color }}">Returns</span>

Void


#### setY(double y)

<span style="{{ sub_color }}">Description</span>

Set y coordinate of the robot.


<span style="{{ sub_color }}">Syntax</span>

	cordinates.setY(double y)

<span style="{{ sub_color }}">Parameter</span>

double

<span style="{{ sub_color }}">Returns</span>

Void


#### getHeading()

<span style="{{ sub_color }}">Description</span>

Get heading of the robot.


<span style="{{ sub_color }}">Syntax</span>

	cordinates.getHeading()

<span style="{{ sub_color }}">Parameter</span>

Void

<span style="{{ sub_color }}">Returns</span>

double


#### getHeadingRad()

<span style="{{ sub_color }}">Description</span>

Get heading of the robot in Radians.


<span style="{{ sub_color }}">Syntax</span>

	cordinates.getHeadingRad()

<span style="{{ sub_color }}">Parameter</span>

Void

<span style="{{ sub_color }}">Returns</span>

double


#### setHeading(double heading)

<span style="{{ sub_color }}">Description</span>

Set heading of the robot.


<span style="{{ sub_color }}">Syntax</span>

	cordinates.setHeading(double heading)

<span style="{{ sub_color }}">Parameter</span>

double

<span style="{{ sub_color }}">Returns</span>

Void


#### setHeadingRad(double heading)

<span style="{{ sub_color }}">Description</span>

Set heading of the robot in Radians.


<span style="{{ sub_color }}">Syntax</span>

	cordinates.setHeadingRad(double heading)

<span style="{{ sub_color }}">Parameter</span>

double

<span style="{{ sub_color }}">Returns</span>

Void


#### setCoordinate(double x, double y, double heading)

<span style="{{ sub_color }}">Description</span>

Set x and y cordinates.

<span style="{{ sub_color }}">Syntax</span>

	cordinates.setCoordinate(ddouble x, double y)
	cordinates.setCoordinate(ddouble x, double y, double heading)

<span style="{{ sub_color }}">Parameter</span>

	double x : x cordinate
	double y : y cordinate
	double heading : heading of cordinate

<span style="{{ sub_color }}">Returns</span>

Void

#### toString()

<span style="{{ sub_color }}">Description</span>

return string of x , y and heading.

<span style="{{ sub_color }}">Syntax</span>

	cordinate.toString()

<span style="{{ sub_color }}">Parameter</span>

Void

<span style="{{ sub_color }}">Returns</span>

String

#### publishCoordinate()


<span style="{{ sub_color }}">Description</span>

Publish cordinate details under topic <b>localization/update</b>.

<span style="{{ sub_color }}">Syntax</span>

	cordinate.publishCoordinate()

<span style="{{ sub_color }}">Parameter</span>

Void

<span style="{{ sub_color }}">Returns</span>

Void


### MotionController(Coordinate c)

	MotionController motion = new MotionController(Communication(c));

#### rotate(int speed, int interval)

<span style="{{ sub_color }}">Description</span>

Rotate virtual roboot with a given speed and interval.

<span style="{{ sub_color }}">Syntax</span>

	motion.rotate(int speed)
	motion.rotate(int speed, int interval)

<span style="{{ sub_color }}">Parameter</span>

	int speed : speed of roataion
	int interval : time interval for all steps to occur? 

<span style="{{ sub_color }}">Returns</span>

Void

#### move(int leftSpeed, int rightSpeed, int interval)

<span style="{{ sub_color }}">Description</span>

Move virtual roboot with a given speed and interval.

<span style="{{ sub_color }}">Syntax</span>

	motion.move(int leftSpeed, int rightSpeed, int interval)
	motion.move(int leftSpeed, int rightSpeed)

<span style="{{ sub_color }}">Parameter</span>

	int leftSpeed : speed of left motor?
	int rightSpeed : speed of right motor?
	int interval : ................... 

<span style="{{ sub_color }}">Returns</span>

Void


#### rotateDegree(int speed, float degree)

//To be implemented

#### moveDistance(int speed, float distance)

//To be implemented

#### goToGoal(double targetX, double targetY, int velocity)

<span style="{{ sub_color }}">Description</span>

Move virtual robot to defined location

<span style="{{ sub_color }}">Syntax</span>

	motion.gotoGoal(double targetX, int targetY, int velocity,in t interval )
	motion.gotoGoal(double targetX, int targetY, int velocity)

<span style="{{ sub_color }}">Parameter</span>

	double targetX : target x coordinate
	double targetY : target y coordinate
	int velocity   : velcoity of robot
	int interval   : ............................   

<span style="{{ sub_color }}">Returns</span>

boolean

#### isSpeedInRange(int speed)

<span style="{{ sub_color }}">Description</span>

Check if given speed is in acceptable range (if speed within ROBOT_SPEED_MIN && ROBOT_SPEED_MAX).

<span style="{{ sub_color }}">Syntax</span>

	motion.isSpeedInRange(int speed)

<span style="{{ sub_color }}">Parameter</span>

	int speed : Speed of the robot 

<span style="{{ sub_color }}">Returns</span>

boolean

#### delay(int interval)

<span style="{{ sub_color }}">Description</span>

Delay to hold thread.

<span style="{{ sub_color }}">Syntax</span>

	motion.delay(int interval)

<span style="{{ sub_color }}">Parameter</span>

	int interval : sleep for a defined interval  

<span style="{{ sub_color }}">Returns</span>

Void

<!------ Is this definiton correct? ----->
#### getSlope(double x1, double y1, double x2, double y2)

<span style="{{ sub_color }}">Description</span>

Angle in degrees between two points.

<span style="{{ sub_color }}">Syntax</span>

	motion.getSlop(idouble x1, double y1, double x2, double y2)

<span style="{{ sub_color }}">Parameter</span>

	double x1 : start x cordinate
	double y1 : start y cordinate
	double x2 : goal x cordinate
	double y2 : goal y cordinate

<span style="{{ sub_color }}">Returns</span>

double

#### debug(String msg, int level)
<!--------Is this part of the documentation--------->



### RobotMqtt(int robotId,RobotMqttClient mqtt, char reality)
    
	RobotMQTT robotMQTT = new RobotMqtt(int robotId,RobotMqttClient mqtt, char reality)

#### robotCreate(double x, double y, double heading)


<span style="{{ sub_color }}">Description</span>

Create a robot in the simulator.

<span style="{{ sub_color }}">Syntax</span>

	robotMQTT.robotCreate(double x, double y,double heading)

<span style="{{ sub_color }}">Parameter</span>

	double x : position x cordinate
	double y : position y cordinate
	double heading : heading of the robot

<span style="{{ sub_color }}">Returns</span>

Void

#### subscribe(mqttTopic key, String topic) 

<span style="{{ sub_color }}">Description</span>

Subsribe to a topic.

<span style="{{ sub_color }}">Syntax</span>

	robotMQTT.subscribe(mqttTopic key, String topic)

<span style="{{ sub_color }}">Parameter</span>

	mqttTopic key :...... 
	String topic  : topic to subscribe 

<span style="{{ sub_color }}">Returns</span>

Void

#### handleSubscription(Robot r, MqttMsg m)


<span style="{{ sub_color }}">Description</span>

Handle the mqtt subsription of the robots.

<span style="{{ sub_color }}">Syntax</span>

	robotMQTT.handleSubscription(Robot r, MqttMsg m)

<span style="{{ sub_color }}">Parameter</span>

	Robot r : considerd robot
	Mqttmsg m: topic and message (Calling out various functions through MQTT)

<span style="{{ sub_color }}">Returns</span>

Void




