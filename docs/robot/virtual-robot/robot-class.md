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

<span style="{{%sub_color%}}">Description</span>

Returns double type value for the distance of obstacle or robot in front.
    
<span style="{{%sub_color%}}">Syntax</span>
 
	distSensor.getDistance() 

<span style="{{%sub_color%}}">Parameter</span>

None

<span style="{{%sub_color%}}">Returns</span>

Double 

<span style="{{%sub_color%}}">Example Code</span>

<----------Shall we add some code snippet like this for each method ?------------->


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

<span style="{{%sub_color%}}">Description</span>

Returns ProximityReadingType value indicating .......
    
<span style="{{%sub_color%}}">Syntax</span>

	proximitySensor.getProximity();

<span style="{{%sub_color%}}">Parameter</span>

None

<span style="{{%sub_color%}}">Returns</span>

swarm.robot.types.ProximityReadingType

### ColorSensor(Robot robot, RobotMqttClient m) 

    ColorSensor colorSensor = new ColorSensor(this, robotMqttClient);

#### getColor() 

<span style="{{%sub_color%}}">Description</span>

Returns RGBColor type value indicating the color detected at the front of the robot.
    
<span style="{{%sub_color%}}">Syntax</span>
 
	colorSensor.getColor() 

<span style="{{%sub_color%}}">Parameter</span>

None

<span style="{{%sub_color%}}">Returns</span>

swarm.robot.types.RGBColorType 

## Communication

### DirectedCommunication(int robotId, RobotMqttClient m)

    DirectedCommunication directedComm = new DirectedCommunication(id, robotMqttClient);

#### sendMessage(String msg, int distance)


<span style="{{%sub_color%}}">Description</span>

Sends message through MQTT.

<span style="{{%sub_color%}}">Syntax</span>
 
	directedComm.sendMessage(String msg, int distance);
	directedComm.sendMessage(String msg);


<span style="{{%sub_color%}}">Parameter</span>

	String msg   : message to be passed
	int distance : distance  

<span style="{{%sub_color%}}">Returns</span>

Void

### SimpleCommunication(int robotId, RobotMqttClient m)

	SimpleCommunication simpleComm = new SimpleCommunication(id, robotMqttClient);

#### sendMessage(String msg, int distance)


<span style="{{%sub_color%}}">Description</span>

Sends message through MQTT.

<span style="{{%sub_color%}}">Syntax</span>
 
	simpleComm.sendMessage(String msg, int distance);
	simpleComm.sendMessage(String msg);


<span style="{{%sub_color%}}">Parameter</span>

	String msg   : message to be passed
	int distance : distance  

<span style="{{%sub_color%}}">Returns</span>

Void


## Indicators
Indicators used signify various states of the robots. 


### NeoPixel(Robot robot, RobotMqttClient m)

	NeoPixel neoPixel = new NeoPixel(this, robotMqttClient);

#### changeColor(int r, int g, int b)

<span style="{{%sub_color%}}">Description</span>

Used to change colors of the neopixel by inputing RGB values as integers.

<span style="{{%sub_color%}}">Syntax</span>
 
	neoPixel.changeColor(int r,int g,int b);

<span style="{{%sub_color%}}">Parameter</span>

	int r : red 
	int g : green
	int b : blue

<span style="{{%sub_color%}}">Returns</span>

Void




## Helpers

Helper and Controller objects

### MotionController(int robotId, double x, double y, double heading, RobotMqttClient m)

	MotionController motion = new MotionController;

### RobotMqttClient(int robotId, double x, double y, double heading, RobotMqttClient m)
    
	RobotMQTT robotMQTT = new RobotMQTT;

### Coordinate(int robotId, double x, double y, double heading, RobotMqttClient m)

    Coordinate coordinates = new Coordinate;


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



