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
The Robot Class implements a collection of sensors, communication methods, output devices, Helper functions to emulate a real hardware robot in the virtual space.

### Robot(int id, double x, double y, double heading, char reality)
<br>

	id      - id of the robot (unique in virtual and real)
	x       - x cordinates on the arena
	y       - y cordinates on the arena
	heading - 
	reality - specify whether real or virtual
</br>	

Defines <b>robotMqttClient</b> for MQTT connection to create a robot instance in the Simulator.


## Sensors

Sensor modules are written with physical hardware implementations in mind. The Sensors available can be used as direct inputs in designing the robot logic.


### DistanceSensor(Robot robot, RobotMqttClient m) 

#### getDistance()

<span style="color: orange;">Description</span>

Returns double type value for the distance of obstacle or robot in front.
    
<span style="color: orange;">Syntax</span>
 
	distSensor.getDistance() 



<span style="color: orange;">Parameter</span>

None

<span style="color: orange;">Returns</span>

Double 

<span style="color: orange;">Example Code</span>

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



